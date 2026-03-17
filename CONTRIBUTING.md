# Contributing to Awesome AI-CAE

Thank you for your interest in contributing! This list curates the intersection of **AI and Computer-Aided Engineering** — tools that AI agents can call directly (MCP/API/CLI), and AI/ML tools that are transforming how engineers simulate, design, and manufacture.

## What makes this list different?

Unlike general-purpose CAE lists, every tool here must be **AI-ready**: programmable, automatable, or an AI/ML tool itself. GUI-only tools without API access are out of scope.

## AI-Readiness Tiers

We evaluate tools on a 3-tier AI-readiness scale:

| Tier | Definition | Examples |
|------|-----------|----------|
| **T1 — AI-Native** | MCP server, REST/gRPC API, or LLM-agent framework | viznoir, Foam-Agent, MetaOpenFOAM |
| **T2 — AI-Compatible** | Python API + CLI for scripted automation | OpenFOAM (PyFoam), CadQuery, PyVista |
| **T3 — AI-Enabling** | AI/ML library that accelerates CAE workflows | PySINDy, FNO, Taichi, DeepXDE |

Tools that don't fit T1-T3 are not in scope.

## Quality requirements

- **Open source** with code on GitHub (or similar public hosting).
- **Clear README** with installation and usage instructions.
- **Actively maintained** — commit within the last 12 months. Exception: foundational tools with 3000+ stars may be included even if archived.
- **Installable** — `pip install`, `docker run`, or documented build process. Benchmarks/datasets need a download path.
- **Minimum stars** — 50+ on GitHub. Exception: T1 (AI-Native) tools have no star minimum since they are newer.

## Libraries vs. paper code

| Type | Placement |
|------|-----------|
| **Library** (pip-installable, ongoing releases) | Relevant category (AI/ML, Surrogate, etc.) |
| **Paper reference implementation** (one-off, no maintenance) | Learning Resources only. Exception: 1000+ stars |
| **Curated list** (awesome-* style) | Learning Resources only |

## Entry format

```markdown
- [owner/repo](https://github.com/owner/repo) `Language` `Tag` - Description starting with capital letter, ending with period.
```

**Language tags:** `Python`, `C++`, `Fortran`, `Rust`, `CUDA`, `JAX`, etc.
**Special tags:** `MCP` (Model Context Protocol), `API` (REST/gRPC), `PyTorch`, `JAX`.

## Submitting a PR

1. Fork this repository.
2. Add your item to the appropriate section in `README.md`.
3. Keep entries in **alphabetical order** within each section.
4. Submit a pull request with a clear title: `Add owner/repo`.
5. Ensure the PR passes CI checks (awesome-lint + link checker).

## Featured badge

If your project is listed, you can add this badge to your README:

```markdown
[![Awesome AI-CAE](https://img.shields.io/badge/Awesome-AI--CAE-blue?logo=awesomelists&logoColor=white)](https://github.com/kimimgo/awesome-ai-cae)
```

Preview: [![Awesome AI-CAE](https://img.shields.io/badge/Awesome-AI--CAE-blue?logo=awesomelists&logoColor=white)](https://github.com/kimimgo/awesome-ai-cae)

## Suggesting a new category

Open an [issue](https://github.com/kimimgo/awesome-ai-cae/issues/new) with the `enhancement` label to propose a new category. Include at least 3 items that would belong in it.

## Reporting broken links

Use the [broken link issue template](https://github.com/kimimgo/awesome-ai-cae/issues/new?template=report-broken-link.md) or submit a PR fixing the link.

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be kind, be constructive.

## License

By contributing, you agree that your contributions will be licensed under CC0 1.0 Universal.
