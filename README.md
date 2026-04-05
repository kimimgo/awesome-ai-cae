<!--lint disable awesome-heading awesome-github awesome-toc double-link-->

<div align="center">

<img src="media/banner.svg" alt="Awesome AI-CAE" width="800">

<br><br>

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/kimimgo/awesome-ai-cae)

**A curated list of AI-ready tools for Computer-Aided Engineering.**<br>
Every tool is programmable via Python API, CLI, or MCP — no GUI-only tools.

[한국어](docs/README.ko.md) · [中文](docs/README.zh.md) · [日本語](docs/README.ja.md) · [Deutsch](docs/README.de.md) · [Français](docs/README.fr.md) · [Español](docs/README.es.md) · [Português](docs/README.pt.md)

</div>

## Contents

- [Core Engine Readiness](#core-engine-readiness)
- [MCP Servers](#mcp-servers)
- [CFD — Computational Fluid Dynamics](#cfd--computational-fluid-dynamics)
- [FEA — Finite Element Analysis](#fea--finite-element-analysis)
- [SPH — Smoothed Particle Hydrodynamics](#sph--smoothed-particle-hydrodynamics)
- [DEM — Discrete Element Method](#dem--discrete-element-method)
- [Visualization & Post-processing](#visualization--post-processing)
- [CAD & Geometry](#cad--geometry)
- [Mesh Generation](#mesh-generation)
- [Differentiable Simulation](#differentiable-simulation)
- [AI/ML for Simulation](#aiml-for-simulation)
- [Surrogate Models & PINNs](#surrogate-models--pinns)
- [Optimization](#optimization)
- [Data Formats & I/O](#data-formats--io)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Learning Resources](#learning-resources)

## Core Engine Readiness

> AI-readiness of 17 foundational CAE solvers. Only 2 have MCP integration today.

<table>
<tr><th>Engine</th><th>Domain</th><th>⭐</th><th>Python API</th><th>Headless</th><th>Docker</th><th>🤖 AI-Native</th></tr>
<tr><td><a href="https://github.com/OpenFOAM/OpenFOAM-dev">OpenFOAM</a></td><td>CFD</td><td><img src="https://img.shields.io/github/stars/OpenFOAM/OpenFOAM-dev?style=flat-square&label=" alt="stars"></td><td>PyFoam</td><td>✅</td><td>✅</td><td>✅ Foam-Agent, MCP</td></tr>
<tr><td><a href="https://github.com/FEniCS/dolfinx">FEniCS</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/FEniCS/dolfinx?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://gitlab.onelab.info/gmsh/gmsh">Gmsh</a></td><td>Mesh</td><td>—</td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/Kitware/VTK">VTK</a> / <a href="https://github.com/Kitware/ParaView">ParaView</a></td><td>Viz</td><td><img src="https://img.shields.io/github/stars/Kitware/VTK?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>✅ ParaView-MCP</td></tr>
<tr><td><a href="https://github.com/su2code/SU2">SU2</a></td><td>CFD</td><td><img src="https://img.shields.io/github/stars/su2code/SU2?style=flat-square&label=" alt="stars"></td><td>pySU2</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/mfem/mfem">MFEM</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/mfem/mfem?style=flat-square&label=" alt="stars"></td><td>PyMFEM</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/dealii/dealii">deal.II</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/dealii/dealii?style=flat-square&label=" alt="stars"></td><td>Limited</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/DualSPHysics/DualSPHysics">DualSPHysics</a></td><td>SPH</td><td><img src="https://img.shields.io/github/stars/DualSPHysics/DualSPHysics?style=flat-square&label=" alt="stars"></td><td>Inductiva API</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/taichi-dev/taichi">Taichi</a></td><td>Diff. Sim</td><td><img src="https://img.shields.io/github/stars/taichi-dev/taichi?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/PyFR/PyFR">PyFR</a></td><td>CFD</td><td><img src="https://img.shields.io/github/stars/PyFR/PyFR?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="http://www.calculix.de/">CalculiX</a></td><td>FEA</td><td>—</td><td>pycalculix</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/ElmerCSC/elmerfem">Elmer</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/ElmerCSC/elmerfem?style=flat-square&label=" alt="stars"></td><td>PyElmer</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/Open-Cascade-SAS/OCCT">OpenCASCADE</a></td><td>CAD</td><td><img src="https://img.shields.io/github/stars/Open-Cascade-SAS/OCCT?style=flat-square&label=" alt="stars"></td><td>pythonOCC</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/idaholab/moose">MOOSE</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/idaholab/moose?style=flat-square&label=" alt="stars"></td><td>Python</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/FreeFem/FreeFem-sources">FreeFEM</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/FreeFem/FreeFem-sources?style=flat-square&label=" alt="stars"></td><td>FreeFem++</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/sfepy/sfepy">SfePy</a></td><td>FEA</td><td><img src="https://img.shields.io/github/stars/sfepy/sfepy?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
<tr><td><a href="https://github.com/google-deepmind/mujoco">MuJoCo</a></td><td>Diff. Sim</td><td><img src="https://img.shields.io/github/stars/google-deepmind/mujoco?style=flat-square&label=" alt="stars"></td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td></tr>
</table>

<sup>[back to top](#contents)</sup>

## MCP Servers

> AI agents call these directly via [Model Context Protocol](https://modelcontextprotocol.io/).

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` - Cinema-quality science visualization. 22 tools for rendering, slicing, contouring, volume rendering, and animating OpenFOAM/VTK/CGNS data via VTK. Headless EGL/OSMesa.
- [llnl/paraview_mcp](https://github.com/llnl/paraview_mcp) `Python` `MCP` - Natural language control of ParaView via MCP. Multimodal LLM observes viewport for visual feedback (LLNL).
- [webworn/openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) `C++` `MCP` - OpenFOAM MCP server with Socratic questioning for CFD education and expert error resolution.

<sup>[back to top](#contents)</sup>

## CFD — Computational Fluid Dynamics

> Open-source solvers for fluid flow, heat transfer, and multiphysics.

- [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) `C++` - The open source CFD toolbox. Finite volume solvers for incompressible/compressible flow, multiphase, combustion, heat transfer.
- [su2code/SU2](https://github.com/su2code/SU2) `C++` `Python` - Multiphysics simulation and design optimization. Compressible/incompressible flow, structural analysis, adjoint-based design.
- [LLNL/Nek5000](https://github.com/Nek5000/Nek5000) `Fortran` - High-order spectral element CFD solver. DNS/LES of turbulent flows. Scalable to millions of cores.
- [Nek5000/nekRS](https://github.com/Nek5000/nekRS) `C++` `CUDA` - GPU-accelerated spectral element CFD. Successor to Nek5000 with native CUDA/HIP/OpenCL support.
- [precice/precice](https://github.com/precice/precice) `C++` `Python` - Coupling library for multi-physics simulations. Fluid-structure interaction, conjugate heat transfer.
- [PyFR/PyFR](https://github.com/PyFR/PyFR) `Python` - High-order flux reconstruction CFD on mixed unstructured grids. GPU-accelerated (CUDA/OpenCL/HIP).

<sup>[back to top](#contents)</sup>

## FEA — Finite Element Analysis

> Structural, thermal, and multiphysics FEM solvers.

- [CalculiX](http://www.calculix.de/) `Fortran` `C` - Free 3D structural FEM. Linear/nonlinear static, dynamic, thermal analysis. Abaqus INP compatible.
- [dealii/dealii](https://github.com/dealii/dealii) `C++` - Adaptive finite elements. Supports hp-refinement, multigrid, and parallel distributed computing.
- [ElmerCSC/elmerfem](https://github.com/ElmerCSC/elmerfem) `Fortran` `C++` - Multiphysics FEM solver. Fluid dynamics, structural mechanics, electromagnetics, heat transfer. CSC Finland.
- [FEniCS/dolfinx](https://github.com/FEniCS/dolfinx) `C++` `Python` - Next-generation FEniCS. Automated PDE solving with high-level Python/C++ interface. Parallel, scalable.
- [firedrakeproject/firedrake](https://github.com/firedrakeproject/firedrake) `Python` - Automated FEM with code generation from high-level problem descriptions. UFL domain-specific language.
- [FreeFem/FreeFem-sources](https://github.com/FreeFem/FreeFem-sources) `C++` - Partial differential equation solver using finite element method. High-level scripting language for 2D/3D problems.
- [idaholab/moose](https://github.com/idaholab/moose) `C++` `Python` - Multiphysics Object-Oriented Simulation Environment. Coupled physics FEM framework from Idaho National Lab.
- [KratosMultiphysics/Kratos](https://github.com/KratosMultiphysics/Kratos) `C++` `Python` - Framework for multi-physics FEM. Structural, fluid, thermal, contact, FSI.
- [mfem/mfem](https://github.com/mfem/mfem) `C++` - High-order finite element library. Supports GPU acceleration, AMR, and dozens of physics applications.
- [OpenSees/OpenSees](https://github.com/OpenSees/OpenSees) `C++` - Open system for earthquake engineering simulation. Structural and geotechnical response analysis. Berkeley.
- [sfepy/sfepy](https://github.com/sfepy/sfepy) `Python` - Simple Finite Elements in Python. Solve PDEs by FEM in 1D, 2D, and 3D with plain Python scripting.

<sup>[back to top](#contents)</sup>

## SPH — Smoothed Particle Hydrodynamics

> Meshless particle methods for free-surface flows and fluid-structure interaction.

- [DualSPHysics/DualSPHysics](https://github.com/DualSPHysics/DualSPHysics) `C++` `CUDA` - GPU-accelerated SPH solver. Free-surface flows, wave generation, fluid-structure interaction, floating bodies.
- [InteractiveComputerGraphics/SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) `C++` - Physically-based SPH fluid simulation. DFSPH, IISPH, PBF pressure solvers. Viscosity, surface tension.
- [pypr/pysph](https://github.com/pypr/pysph) `Python` `Cython` - SPH framework in Python. Compressible/incompressible flows, solid mechanics, coupled problems.

<sup>[back to top](#contents)</sup>

## DEM — Discrete Element Method

> Particle-based simulation of granular materials, powders, and coupled particle-fluid systems.

- [CFDEMproject/LIGGGHTS-PUBLIC](https://github.com/CFDEMproject/LIGGGHTS-PUBLIC) `C++` - Industry-standard open-source DEM for granular materials. LAMMPS-based with heat transfer and CFD coupling.
- [lammps/lammps](https://github.com/lammps/lammps) `C++` `Python` - Large-scale Atomic/Molecular Massively Parallel Simulator. Classical MD and DEM with granular package. Sandia National Labs.
- [SudoDEM/SudoDEM](https://github.com/SudoDEM/SudoDEM) `C++` `Python` - DEM for non-spherical particles. Polyhedra, super-ellipsoids, and cylinders for realistic granular simulations.

<sup>[back to top](#contents)</sup>

## Visualization & Post-processing

> Rendering, plotting, and interactive exploration of simulation results.

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` - Cinema-quality science visualization MCP server. 22 tools, EGL/OSMesa headless, cinematic lighting, physics animations.
- [Kitware/VTK](https://github.com/Kitware/VTK) `C++` `Python` - The Visualization Toolkit. 3D computer graphics, image processing, scientific visualization. Industry standard.
- [nmwsharp/polyscope](https://github.com/nmwsharp/polyscope) `C++` `Python` - Lightweight 3D viewer for meshes, point clouds, and scalar fields. One-line visualization for geometry processing.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` - Pythonic VTK. Streamlined 3D plotting, mesh analysis, and interactive visualization.
- [Kitware/ParaView](https://github.com/Kitware/ParaView) `C++` `Python` - Multi-platform data analysis and visualization. VTK-based GUI + Python scripting + client-server architecture.
- [napari/napari](https://github.com/napari/napari) `Python` - Fast n-dimensional image viewer. Plugin ecosystem for biomedical and scientific imaging.
- [marcomusy/vedo](https://github.com/marcomusy/vedo) `Python` - Scientific analysis and visualization of 3D objects and point clouds. VTK-based with simple API.
- [plotly/plotly.py](https://github.com/plotly/plotly.py) `Python` - Interactive, publication-quality graphs. 3D scatter, surface, mesh, volume. Web-based rendering.

<sup>[back to top](#contents)</sup>

## CAD & Geometry

> Parametric modeling, geometry processing, and CAD data exchange.

- [CadQuery/cadquery](https://github.com/CadQuery/cadquery) `Python` - Parametric 3D CAD scripting. Build models with Python, export STEP/STL/IGES. OpenCASCADE kernel.
- [CadQuery/OCP](https://github.com/CadQuery/OCP) `C++` `Python` - Python wrapper for OpenCASCADE via pybind11. Low-level foundation for CadQuery and build123d.
- [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) `C++` `Python` - Open-source parametric 3D CAD modeler. Part design, FEM workbench, BIM, path (CAM).
- [gumyr/build123d](https://github.com/gumyr/build123d) `Python` - Modern Python CAD with algebraic geometry API. Successor to CadQuery with cleaner builder pattern.
- [mikedh/trimesh](https://github.com/mikedh/trimesh) `Python` - Load and manipulate triangular meshes. Boolean operations, ray tracing, convex hulls, format conversion.
- [nschloe/pygmsh](https://github.com/nschloe/pygmsh) `Python` - Python interface for Gmsh. Scripted geometry + mesh generation with parametric control.
- [Open-Cascade-SAS/OCCT](https://github.com/Open-Cascade-SAS/OCCT) `C++` - Open CASCADE Technology. Kernel for 3D surface and solid modeling, CAD data exchange (STEP/IGES).
- [SolidCode/SolidPython](https://github.com/SolidCode/SolidPython) `Python` - Python frontend for OpenSCAD. Generate 3D models programmatically with CSG operations.

<sup>[back to top](#contents)</sup>

## Mesh Generation

> Structured, unstructured, and AI-driven mesh generation for simulation preprocessing.

- [buaacyw/MeshAnything](https://github.com/buaacyw/MeshAnything) `Python` - Artist-quality mesh generation with autoregressive transformers. Any 3D input to mesh (ICLR 2025 spotlight).
- [CGAL/cgal](https://github.com/CGAL/cgal) `C++` - Computational Geometry Algorithms Library. Mesh generation, triangulation, Boolean operations, convex hulls.
- [Gmsh](https://gitlab.onelab.info/gmsh/gmsh) `C++` `Python` - Full-featured 3D finite element mesh generator. CAD engine, structured/unstructured meshing, built-in post-processing.
- [libigl/libigl](https://github.com/libigl/libigl) `C++` `Python` - Header-only geometry processing library. Mesh parameterization, deformation, Boolean ops. Eurographics award winner.
- [MmgTools/mmg](https://github.com/MmgTools/mmg) `C` - Anisotropic mesh adaptation for 2D/3D surface and volume remeshing. Metric-based automatic refinement.
- [NGSolve/netgen](https://github.com/NGSolve/netgen) `C++` `Python` - Automatic 3D tetrahedral mesh generator. CAD (OCC) integration, mesh optimization, parallel meshing.
- [nmwsharp/geometry-central](https://github.com/nmwsharp/geometry-central) `C++` - Applied geometry algorithms for surfaces and volumes. Geodesics, vector fields, intrinsic triangulations.
- [OpenMeshLab/MeshXL](https://github.com/OpenMeshLab/MeshXL) `Python` - Foundation model for 3D mesh generation. Pre-trained on Objaverse, text-to-mesh capable (NeurIPS 2024).
- [PyMesh/PyMesh](https://github.com/PyMesh/PyMesh) `Python` `C++` - Geometry processing library. Boolean, convex hull, remeshing, self-intersection repair.
- [pyvista/tetgen](https://github.com/pyvista/tetgen) `C++` `Python` - Python interface to TetGen tetrahedral mesh generator. Constrained Delaunay tetrahedralization with quality control.
- [wildmeshing/fTetWild](https://github.com/wildmeshing/fTetWild) `C++` - Fast and robust tetrahedral meshing. Handles self-intersections and degenerate input. Ten times faster than TetWild.

<sup>[back to top](#contents)</sup>

## Differentiable Simulation

> GPU-native frameworks for gradient-based optimization through physics.

- [Autodesk/XLB](https://github.com/Autodesk/XLB) `Python` `JAX` - Differentiable Lattice Boltzmann for physics-ML. Scales to billions of cells on multi-GPU.
- [google/brax](https://github.com/google/brax) `Python` `JAX` - Massively parallel rigidbody physics on accelerator hardware. Millions of steps/second on TPU.
- [jax-md/jax-md](https://github.com/jax-md/jax-md) `Python` `JAX` - Differentiable, hardware-accelerated molecular dynamics. Runs on CPU/GPU/TPU via XLA.
- [gbionics/jaxsim](https://github.com/gbionics/jaxsim) `Python` `JAX` - Differentiable multibody dynamics engine. Hardware-accelerated robot learning and control via JAX.
- [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) `C++` `Python` - Multi-joint dynamics with contact. General-purpose physics engine for robotics, biomechanics, and control.
- [NVIDIA/warp](https://github.com/NVIDIA/warp) `Python` `CUDA` - Differentiable simulation and spatial computing. Reverse-mode AD, PyTorch/JAX interop.
- [taichi-dev/taichi](https://github.com/taichi-dev/taichi) `Python` `CUDA` - Productive GPU programming with automatic differentiation. DiffTaichi for differentiable physics.
- [tumaer/JAXFLUIDS](https://github.com/tumaer/JAXFLUIDS) `Python` `JAX` - Fully-differentiable CFD solver for 3D compressible single-phase and two-phase flows.

<sup>[back to top](#contents)</sup>

## AI/ML for Simulation

> Neural operators, LLM agents, and foundation models for computational engineering.

- [csml-rpi/Foam-Agent](https://github.com/csml-rpi/Foam-Agent) `Python` `API` - AI agent for automated CFD workflows. LLM-driven OpenFOAM simulation setup and execution.
- [deepmodeling/deepmd-kit](https://github.com/deepmodeling/deepmd-kit) `Python` `C++` - Deep learning for molecular dynamics. Neural network potentials for large-scale atomistic simulations.
- [dynamicslab/pykoopman](https://github.com/dynamicslab/pykoopman) `Python` - Data-driven Koopman operator approximation. Dynamical system analysis and prediction from time series.
- [dynamicslab/pysindy](https://github.com/dynamicslab/pysindy) `Python` - Sparse Identification of Nonlinear Dynamics. Data-driven discovery of governing equations from measurements.
- [google-deepmind/graphcast](https://github.com/google-deepmind/graphcast) `Python` - Graph neural network for medium-range weather forecasting. Ten-day forecasts in under a minute (Nature 2023).
- [google/jax-cfd](https://github.com/google/jax-cfd) `Python` - JAX-based CFD. Differentiable Navier-Stokes solvers. GPU-accelerated, auto-differentiable.
- [Koopman-Laboratory/KoopmanLab](https://github.com/Koopman-Laboratory/KoopmanLab) `Python` - Koopman Neural Operator for mesh-free nonlinear PDE solving. Multi-scale decomposition.
- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) `Python` - Deep learning library for PDEs. PINNs, DeepONet. Backends: TensorFlow, PyTorch, JAX, PaddlePaddle.
- [microsoft/aurora](https://github.com/microsoft/aurora) `Python` - Foundation model for Earth system prediction. Atmosphere, ocean, air quality. Pre-trained on ERA5 and CMIP6.
- [microsoft/ClimaX](https://github.com/microsoft/ClimaX) `Python` - Foundation model for weather and climate. Pre-trained on CMIP6, fine-tunable for downstream tasks.
- [NeuralOperator/neuraloperator](https://github.com/NeuralOperator/neuraloperator) `Python` - Neural operators in PyTorch. FNO, SFNO, UNO for learning PDE solution operators.
- [NVIDIA/physicsnemo](https://github.com/NVIDIA/physicsnemo) `Python` `CUDA` - Physics-ML framework (formerly Modulus). PINNs, neural operators, GNNs, diffusion models. Apache 2.0.
- [Terry-cyx/MetaOpenFOAM](https://github.com/Terry-cyx/MetaOpenFOAM) `Python` `API` - LLM-based multi-agent framework for CFD. Automated simulation pipeline from natural language.
- [tum-pbs/PhiFlow](https://github.com/tum-pbs/PhiFlow) `Python` - Differentiable PDE simulations. Fluid dynamics with TF/PyTorch/JAX. ML-physics hybrid workflows.

<sup>[back to top](#contents)</sup>

## Surrogate Models & PINNs

> Physics-informed neural networks and data-driven reduced-order models for fast PDE solving.

- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) `Python` - Physics-informed neural networks for PDEs. Multi-backend (TF, PyTorch, JAX). Inverse problems, fractional PDEs.
- [mathLab/PINA](https://github.com/mathLab/PINA) `Python` - Physics-Informed Neural networks for Advanced modeling. PyTorch Lightning-based with multi-device training.
- [mathLab/PyDMD](https://github.com/mathLab/PyDMD) `Python` - Dynamic Mode Decomposition. Data-driven reduced-order modeling for fluid dynamics and beyond.
- [NeuroDiffGym/neurodiffeq](https://github.com/NeuroDiffGym/neurodiffeq) `Python` - Neural network solver for ODEs and PDEs. Flexible architecture with native boundary condition handling.
- [NVIDIA/physicsnemo-sym](https://github.com/NVIDIA/physicsnemo-sym) `Python` - Symbolic AI for physics. Physics-informed neural networks with symbolic equation definition.
- [rezaakb/pinns-torch](https://github.com/rezaakb/pinns-torch) `Python` `PyTorch` - Production-ready PINNs in PyTorch. Multi-physics support, inverse problems, uncertainty quantification.
- [sciann/sciann](https://github.com/sciann/sciann) `Python` - Neural networks for scientific computing. Keras-based PINNs with custom loss and constraints.
- [thuml/Neural-Solver-Library](https://github.com/thuml/Neural-Solver-Library) `Python` - Library for advanced neural PDE solvers. Benchmarking Transolver, FNO, and variants on diverse PDE families.

<sup>[back to top](#contents)</sup>

## Optimization

> Bayesian, topology, and multidisciplinary design optimization.

- [meta-pytorch/botorch](https://github.com/meta-pytorch/botorch) `Python` `PyTorch` - Bayesian optimization in PyTorch. Sequential decision making, multi-objective optimization, batch acquisition.
- [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) `Python` - Multidisciplinary design optimization. NASA-developed. Gradient-based + surrogate-assisted optimization.
- [anyoptimization/pymoo](https://github.com/anyoptimization/pymoo) `Python` - Multi-objective optimization. NSGA-II/III, reference directions, constraint handling, parallelization.
- [dl4to/dl4to](https://github.com/dl4to/dl4to) `Python` `PyTorch` - Deep learning for 3D topology optimization. Autograd + adjoint method for efficient neural optimization.
- [williamhunter/topy](https://github.com/williamhunter/topy) `Python` - Topology optimization with Python. Minimum compliance, heat conduction, mechanism design.
- [mdolab/OpenAeroStruct](https://github.com/mdolab/OpenAeroStruct) `Python` - Aerostructural optimization. VLM aerodynamics + beam FEM structures + ply-level composites.

<sup>[back to top](#contents)</sup>

## Data Formats & I/O

> Libraries for reading, writing, and converting simulation data across mesh and field formats.

- [nschloe/meshio](https://github.com/nschloe/meshio) `Python` - I/O for mesh formats. Abaqus, CGNS, Gmsh, VTK, XDMF, Exodus, and 30+ more.
- [h5py/h5py](https://github.com/h5py/h5py) `Python` - Pythonic interface to HDF5. Read/write large numerical datasets efficiently.
- [Unidata/netcdf4-python](https://github.com/Unidata/netcdf4-python) `Python` - Python/NumPy interface to NetCDF. Climate, ocean, atmospheric simulation data.
- [CGNS/CGNS](https://github.com/CGNS/CGNS) `C` `Fortran` - CFD General Notation System. Standard for CFD data storage and exchange. HDF5-based.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` - Read/write VTK formats (VTI, VTP, VTU, VTS, VTR), STL, OBJ, PLY, glTF, and more.

<sup>[back to top](#contents)</sup>

## Datasets & Benchmarks

> Standardized datasets and benchmarks for training and evaluating scientific ML models.

- [divelab/AIRS](https://github.com/divelab/AIRS) `Python` - AI for science benchmarks. Molecular, protein, climate, physics datasets.
- [Extrality/AirfRANS](https://github.com/Extrality/AirfRANS) `Python` - RANS simulation dataset for airfoils. 1000 simulations with Reynolds-averaged fields (NeurIPS 2022).
- [Mohamedelrefaie/DrivAerNet](https://github.com/Mohamedelrefaie/DrivAerNet) `Python` - Large-scale automotive CFD dataset. 4000+ car designs with drag coefficients and surface fields.
- [i207M/PINNacle](https://github.com/i207M/PINNacle) `Python` - Comprehensive PINN benchmark with 20 PDE problems across difficulty levels (NeurIPS 2024).
- [NASA TMR](https://turbmodels.larc.nasa.gov/) - Turbulence Modeling Resource. Validation cases for CFD turbulence models with experimental data.
- [pdebench/PDEBench](https://github.com/pdebench/PDEBench) `Python` - Benchmarks for scientific ML. Standardized PDE datasets with baseline models.
- [PolymathicAI/the_well](https://github.com/PolymathicAI/the_well) `Python` - Large-scale collection of diverse physics simulations for ML. Fifteen-plus PDE systems (NeurIPS 2024).

<sup>[back to top](#contents)</sup>

## Learning Resources

> Tutorials, courses, and curated reference lists for computational engineering and AI for science.

- [barbagroup/CFDPython](https://github.com/barbagroup/CFDPython) `Python` - Classic "12 Steps to Navier-Stokes" tutorial. Learn CFD fundamentals with Python step by step.
- [ikespand/awesome-machine-learning-fluid-mechanics](https://github.com/ikespand/awesome-machine-learning-fluid-mechanics) - Curated list of ML applications in fluid mechanics. Papers, code, and tutorials.
- [jxx123/simglucose](https://github.com/jxx123/simglucose) `Python` - Type 1 diabetes simulator. Example of AI-in-the-loop biomedical simulation.
- [kks32/phd-thesis-template](https://github.com/kks32/phd-thesis-template) `LaTeX` - Clean PhD thesis template. Widely used in computational mechanics community.
- [maziarraissi/PINNs](https://github.com/maziarraissi/PINNs) `Python` - The foundational PINN reference implementation. Data-driven PDE solutions and discovery (JCP 2019).
- [thunil/Physics-Based-Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning) - Comprehensive collection of physics-based deep learning resources. Papers, code links, and tutorials from TUM.
- [WillDreamer/Awesome-AI4CFD](https://github.com/WillDreamer/Awesome-AI4CFD) - Survey of ML for CFD covering data-driven surrogates, PINNs, and ML-assisted numerical solvers.

<sup>[back to top](#contents)</sup>

## Contributing

Contributions welcome! Read the [contributing guidelines](CONTRIBUTING.md) first.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [kimimgo](https://github.com/kimimgo) has waived all copyright and related or neighboring rights to this work.
