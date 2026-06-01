#!/usr/bin/env python3
"""Execution-verified readiness: smoke-test that a tool actually installs + imports.

Turns the AI-Readiness Score's `pip` signal from *declarative* ("a PyPI page
exists") into *verified* ("a clean `uv` venv installs the package and `import`
succeeds"). This is reproducible evidence a fork can't fake by copying a column.

For each (name, pkg, import_name): create an isolated uv venv, `uv pip install`
the package, then run `python -c "import <import_name>"`. Record pass/fail,
installed version, and elapsed seconds into data/verified.json.

Usage: verify_install.py            # run the curated flagship set
Requires: uv (https://docs.astral.sh/uv/). Bounded per-tool timeout.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA = os.path.join(ROOT, "data", "verified.json")
TIMEOUT = 150  # seconds per tool (install + import)

# Curated flagship set: wheel-available pip tools across the categories.
# (name shown in the list, PyPI package, python import name)
TARGETS = [
    ("kimimgo/viznoir", "viznoir", "viznoir"),
    ("pyvista/pyvista", "pyvista", "pyvista"),
    ("mikedh/trimesh", "trimesh", "trimesh"),
    ("nschloe/meshio", "meshio", "meshio"),
    ("CadQuery/cadquery", "cadquery", "cadquery"),
    ("anyoptimization/pymoo", "pymoo", "pymoo"),
    ("Gmsh", "gmsh", "gmsh"),
    ("h5py/h5py", "h5py", "h5py"),
    ("taichi-dev/taichi", "taichi", "taichi"),
    ("lululxvi/deepxde", "deepxde", "deepxde"),
]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def smoke(pkg: str, import_name: str, venv: str) -> dict:
    t0 = time.time()
    res = {"install_ok": False, "import_ok": False, "version": None, "error": None}
    try:
        run(["uv", "venv", venv], timeout=60)
        inst = run(["uv", "pip", "install", "--python", venv, pkg], timeout=TIMEOUT)
        if inst.returncode != 0:
            res["error"] = (inst.stderr or inst.stdout)[-200:].strip()
            return res
        res["install_ok"] = True
        py = os.path.join(venv, "bin", "python")
        imp = run([py, "-c", f"import {import_name} as m; print(getattr(m,'__version__',''))"], timeout=90)
        if imp.returncode == 0:
            res["import_ok"] = True
            res["version"] = imp.stdout.strip() or None
        else:
            res["error"] = (imp.stderr or "")[-200:].strip()
    except subprocess.TimeoutExpired:
        res["error"] = "timeout"
    finally:
        res["secs"] = round(time.time() - t0, 1)
    return res


def main() -> None:
    if not shutil.which("uv"):
        print("uv not found — install from https://docs.astral.sh/uv/", file=sys.stderr)
        sys.exit(1)
    results = []
    tmp = tempfile.mkdtemp(prefix="aac_verify_")
    for name, pkg, imp in TARGETS:
        venv = os.path.join(tmp, pkg)
        r = smoke(pkg, imp, venv)
        verified = r["install_ok"] and r["import_ok"]
        results.append({"name": name, "pkg": pkg, "verified": verified, **r})
        print(f"  {'✓' if verified else '✗'} {name}: install={r['install_ok']} import={r['import_ok']} {r.get('version') or ''} ({r['secs']}s) {r['error'] or ''}", file=sys.stderr)
        shutil.rmtree(venv, ignore_errors=True)
    shutil.rmtree(tmp, ignore_errors=True)

    n_ok = sum(1 for r in results if r["verified"])
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    with open(DATA, "w") as f:
        json.dump({
            "method": "isolated uv venv: `uv pip install <pkg>` then `import` — execution-verified, not declarative",
            "verified": n_ok,
            "total": len(results),
            "results": results,
        }, f, indent=2, ensure_ascii=False)
    print(f"\nWrote data/verified.json — {n_ok}/{len(results)} install+import verified", file=sys.stderr)


if __name__ == "__main__":
    main()
