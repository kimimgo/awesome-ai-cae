<!--lint disable awesome-heading awesome-github awesome-toc double-link-->

<div align="center">

<!-- BANNER -->
<img src="media/banner.svg" alt="Awesome AI-CAE" width="800">

<br><br>

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/kimimgo/awesome-ai-cae)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated list of AI-powered tools for Computer-Aided Engineering.**<br>
Simulation · Visualization · Design · Manufacturing

<sub>AI agents run simulations, render results, generate meshes, and optimize designs — no GUI needed.</sub>

<br>

[한국어](docs/README.ko.md) · [中文](docs/README.zh.md) · [日本語](docs/README.ja.md) · [Deutsch](docs/README.de.md) · [Français](docs/README.fr.md) · [Español](docs/README.es.md) · [Português](docs/README.pt.md)

</div>

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## Contents

- [MCP Servers](#mcp-servers) — AI-native tool interfaces
- [CFD — Computational Fluid Dynamics](#cfd--computational-fluid-dynamics)
- [FEA — Finite Element Analysis](#fea--finite-element-analysis)
- [SPH — Smoothed Particle Hydrodynamics](#sph--smoothed-particle-hydrodynamics)
- [Visualization & Post-processing](#visualization--post-processing)
- [CAD & Geometry](#cad--geometry)
- [Mesh Generation](#mesh-generation)
- [AI/ML for Simulation](#aiml-for-simulation)
- [Surrogate Models & PINNs](#surrogate-models--pinns)
- [Optimization](#optimization)
- [Data Formats & I/O](#data-formats--io)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Learning Resources](#learning-resources)

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## MCP Servers

> Tools that AI agents can call directly via [Model Context Protocol](https://modelcontextprotocol.io).

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` — Cinema-quality science visualization. 22 tools for rendering, slicing, contouring, volume rendering, and animating OpenFOAM/VTK/CGNS data via VTK. Headless EGL/OSMesa.

<sup>[back to top](#contents)</sup>

## CFD — Computational Fluid Dynamics

- [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) `C++` — The open source CFD toolbox. Finite volume solvers for incompressible/compressible flow, multiphase, combustion, heat transfer.
- [su2code/SU2](https://github.com/su2code/SU2) `C++` `Python` — Multiphysics simulation and design optimization. Compressible/incompressible flow, structural analysis, adjoint-based design.
- [LLNL/Nek5000](https://github.com/Nek5000/Nek5000) `Fortran` — High-order spectral element CFD solver. DNS/LES of turbulent flows. Scalable to millions of cores.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` — 3D plotting and mesh analysis. Pythonic VTK interface for CFD post-processing, streamlines, glyphs.
- [PyFR/PyFR](https://github.com/PyFR/PyFR) `Python` — High-order flux reconstruction CFD on mixed unstructured grids. GPU-accelerated (CUDA/OpenCL/HIP).
- [precice/precice](https://github.com/precice/precice) `C++` `Python` — Coupling library for multi-physics simulations. Fluid-structure interaction, conjugate heat transfer.

<sup>[back to top](#contents)</sup>

## FEA — Finite Element Analysis

- [FEniCS/dolfinx](https://github.com/FEniCS/dolfinx) `C++` `Python` — Next-generation FEniCS. Automated PDE solving with high-level Python/C++ interface. Parallel, scalable.
- [calculix/CalculiX](https://github.com/calculix/ccx) `Fortran` `C` — Free 3D structural FEM. Linear/nonlinear static, dynamic, thermal analysis. Abaqus INP compatible.
- [mfem/mfem](https://github.com/mfem/mfem) `C++` — High-order finite element library. Supports GPU acceleration, AMR, and dozens of physics applications.
- [dealii/dealii](https://github.com/dealii/dealii) `C++` — Adaptive finite elements. Supports hp-refinement, multigrid, and parallel distributed computing.
- [nschloe/meshio](https://github.com/nschloe/meshio) `Python` — I/O for mesh formats. Convert between Abaqus, Gmsh, VTK, XDMF, Exodus, and 30+ formats.
- [Kratos-Multiphysics](https://github.com/KratosMultiphysics/Kratos) `C++` `Python` — Framework for multi-physics FEM. Structural, fluid, thermal, contact, FSI.

<sup>[back to top](#contents)</sup>

## SPH — Smoothed Particle Hydrodynamics

- [DualSPHysics/DualSPHysics](https://github.com/DualSPHysics/DualSPHysics) `C++` `CUDA` — GPU-accelerated SPH solver. Free-surface flows, wave generation, fluid-structure interaction, floating bodies.
- [SPlisHSPlasH/SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) `C++` — Physically-based SPH fluid simulation. DFSPH, IISPH, PBF pressure solvers. Viscosity, surface tension.
- [pypr/pysph](https://github.com/pypr/pysph) `Python` `Cython` — SPH framework in Python. Compressible/incompressible flows, solid mechanics, coupled problems.

<sup>[back to top](#contents)</sup>

## Visualization & Post-processing

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` — Cinema-quality science visualization MCP server. 22 tools, EGL/OSMesa headless, cinematic lighting, physics animations.
- [Kitware/VTK](https://github.com/Kitware/VTK) `C++` `Python` — The Visualization Toolkit. 3D computer graphics, image processing, scientific visualization. Industry standard.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` — Pythonic VTK. Streamlined 3D plotting, mesh analysis, and interactive visualization.
- [Kitware/ParaView](https://github.com/Kitware/ParaView) `C++` `Python` — Multi-platform data analysis and visualization. VTK-based GUI + Python scripting + client-server architecture.
- [napari/napari](https://github.com/napari/napari) `Python` — Fast n-dimensional image viewer. Plugin ecosystem for biomedical and scientific imaging.
- [marcomusy/vedo](https://github.com/marcomusy/vedo) `Python` — Scientific analysis and visualization of 3D objects and point clouds. VTK-based with simple API.
- [plotly/plotly.py](https://github.com/plotly/plotly.py) `Python` — Interactive, publication-quality graphs. 3D scatter, surface, mesh, volume. Web-based rendering.

<sup>[back to top](#contents)</sup>

## CAD & Geometry

- [CadQuery/cadquery](https://github.com/CadQuery/cadquery) `Python` — Parametric 3D CAD scripting. Build models with Python, export STEP/STL/IGES. OpenCASCADE kernel.
- [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) `C++` `Python` — Open-source parametric 3D CAD modeler. Part design, FEM workbench, BIM, path (CAM).
- [OpenCASCADE/OCCT](https://github.com/Open-Cascade-SAS/OCCT) `C++` — Open CASCADE Technology. Kernel for 3D surface and solid modeling, CAD data exchange (STEP/IGES).
- [mikedh/trimesh](https://github.com/mikedh/trimesh) `Python` — Load and manipulate triangular meshes. Boolean operations, ray tracing, convex hulls, format conversion.
- [pygmsh/pygmsh](https://github.com/nschloe/pygmsh) `Python` — Python interface for Gmsh. Scripted geometry + mesh generation with parametric control.

<sup>[back to top](#contents)</sup>

## Mesh Generation

- [gmsh/gmsh](https://github.com/gmsh/gmsh) `C++` `Python` — 3D finite element mesh generator. CAD engine, structured/unstructured meshing, built-in post-processing.
- [CGAL/cgal](https://github.com/CGAL/cgal) `C++` — Computational Geometry Algorithms Library. Mesh generation, triangulation, Boolean operations, convex hulls.
- [NETGEN/NETGEN](https://github.com/NGSolve/netgen) `C++` `Python` — Automatic 3D tetrahedral mesh generator. CAD (OCC) integration, mesh optimization, parallel meshing.
- [PyMesh/PyMesh](https://github.com/PyMesh/PyMesh) `Python` `C++` — Geometry processing library. Boolean, convex hull, remeshing, self-intersection repair.

<sup>[back to top](#contents)</sup>

## AI/ML for Simulation

- [NVIDIA/modulus](https://github.com/NVIDIA/modulus) `Python` `CUDA` — Physics-ML framework. Train neural network surrogates for physics simulations with PINNs, FNOs, GNNs.
- [google/jax-cfd](https://github.com/google/jax-cfd) `Python` — JAX-based CFD. Differentiable Navier-Stokes solvers. GPU-accelerated, auto-differentiable.
- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) `Python` — Deep learning library for PDEs. PINNs, DeepONet. Backends: TensorFlow, PyTorch, JAX, PaddlePaddle.
- [tum-pbs/PhiFlow](https://github.com/tum-pbs/PhiFlow) `Python` — Differentiable PDE simulations. Fluid dynamics with TF/PyTorch/JAX. ML-physics hybrid workflows.
- [NeuralOperator/neuraloperator](https://github.com/NeuralOperator/neuraloperator) `Python` — Neural operators in PyTorch. FNO, SFNO, UNO for learning PDE solution operators.
- [microsoft/ClimaX](https://github.com/microsoft/ClimaX) `Python` — Foundation model for weather and climate. Pre-trained on CMIP6, fine-tunable for downstream tasks.

<sup>[back to top](#contents)</sup>

## Surrogate Models & PINNs

- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) `Python` — Physics-informed neural networks for PDEs. Multi-backend (TF, PyTorch, JAX). Inverse problems, fractional PDEs.
- [sciann/sciann](https://github.com/sciann/sciann) `Python` — Neural networks for scientific computing. Keras-based PINNs with custom loss and constraints.
- [NVIDIA/modulus-sym](https://github.com/NVIDIA/modulus-sym) `Python` — Symbolic AI for physics. Physics-informed neural networks with symbolic equation definition.
- [mathLab/PyDMD](https://github.com/mathLab/PyDMD) `Python` — Dynamic Mode Decomposition. Data-driven reduced-order modeling for fluid dynamics and beyond.

<sup>[back to top](#contents)</sup>

## Optimization

- [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) `Python` — Multidisciplinary design optimization. NASA-developed. Gradient-based + surrogate-assisted optimization.
- [airbus/pymoo](https://github.com/anyoptimization/pymoo) `Python` — Multi-objective optimization. NSGA-II/III, reference directions, constraint handling, parallelization.
- [topology-opt/topy](https://github.com/williamhunter/topy) `Python` — Topology optimization with Python. Minimum compliance, heat conduction, mechanism design.
- [M2DOLab/OpenAeroStruct](https://github.com/mdolab/OpenAeroStruct) `Python` — Aerostructural optimization. VLM aerodynamics + beam FEM structures + ply-level composites.

<sup>[back to top](#contents)</sup>

## Data Formats & I/O

- [nschloe/meshio](https://github.com/nschloe/meshio) `Python` — I/O for mesh formats. Abaqus, CGNS, Gmsh, VTK, XDMF, Exodus, and 30+ more.
- [h5py/h5py](https://github.com/h5py/h5py) `Python` — Pythonic interface to HDF5. Read/write large numerical datasets efficiently.
- [Unidata/netcdf4-python](https://github.com/Unidata/netcdf4-python) `Python` — Python/numpy interface to NetCDF. Climate, ocean, atmospheric simulation data.
- [CGNS/CGNS](https://github.com/CGNS/CGNS) `C` `Fortran` — CFD General Notation System. Standard for CFD data storage and exchange. HDF5-based.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` — Read/write VTK formats (VTI, VTP, VTU, VTS, VTR), STL, OBJ, PLY, glTF, and more.

<sup>[back to top](#contents)</sup>

## Datasets & Benchmarks

- [inductiva/datasets-benchmarks](https://github.com/inductiva/datasets-benchmarks) `Python` — Benchmark datasets for ML in physics simulations. Dam break, wind tunnel, airfoil, protein folding.
- [pdebench/PDEBench](https://github.com/pdebench/PDEBench) `Python` — Benchmarks for scientific ML. Standardized PDE datasets with baseline models.
- [divelab/AIRS](https://github.com/divelab/AIRS) `Python` — AI for science benchmarks. Molecular, protein, climate, physics datasets.
- [NASA TMR](https://turbmodels.larc.nasa.gov/) — Turbulence Modeling Resource. Validation cases for CFD turbulence models with experimental data.
- [DrivAerNet](https://github.com/Mohamedelrefaie/DrivAerNet) `Python` — Large-scale automotive CFD dataset. 4000+ car designs with drag coefficients and surface fields.

<sup>[back to top](#contents)</sup>

## Learning Resources

- [Barba-group/CFDPython](https://github.com/barbagroup/CFDPython) `Python` — 12 Steps to Navier-Stokes. Learn CFD fundamentals with Python step by step.
- [kks32/phd-thesis-template](https://github.com/kks32/phd-thesis-template) `LaTeX` — Clean PhD thesis template. Widely used in computational mechanics community.
- [jxx123/simglucose](https://github.com/jxx123/simglucose) `Python` — Type 1 diabetes simulator. Example of AI-in-the-loop biomedical simulation.

<sup>[back to top](#contents)</sup>

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [kimimgo](https://github.com/kimimgo) has waived all copyright and related or neighboring rights to this work.
