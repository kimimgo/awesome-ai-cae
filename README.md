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

<sub>AI can theoretically handle <a href="https://www.anthropic.com/research/labor-market-impacts">94% of computational tasks — but only 33% is actually used</a> (Anthropic, 2026).<br>In CAE, this gap is even wider. This list curates tools that close it:<br><b>tools that agents can call</b> (MCP/API/CLI), and <b>AI/ML that transforms how we simulate</b>.</sub>

<br>

<sub>104 open-source tools across 16 categories. Every tool is AI-ready: programmable via Python API, CLI, or MCP.</sub>

<br>

[한국어](docs/README.ko.md) · [中文](docs/README.zh.md) · [日本語](docs/README.ja.md) · [Deutsch](docs/README.de.md) · [Français](docs/README.fr.md) · [Español](docs/README.es.md) · [Português](docs/README.pt.md)

</div>

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## Contents

- [Core Engine Readiness](#core-engine-readiness) — AI-readiness of foundational solvers
- [MCP Servers](#mcp-servers) — AI-native tool interfaces
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

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## Core Engine Readiness

> How AI-ready are the foundational CAE solvers? Each engine is assessed on Python API maturity, headless operation, and AI agent integration status.

<table>
<tr><th>Engine</th><th>Domain</th><th>Python API</th><th>Headless</th><th>Docker</th><th>🤖 AI-Native</th><th>Paper</th><th>Citations</th></tr>
<tr><td><a href="https://github.com/OpenFOAM/OpenFOAM-dev">OpenFOAM</a></td><td>CFD</td><td>PyFoam, PythonFOAM</td><td>✅</td><td>✅</td><td>✅ Foam-Agent, MetaOpenFOAM, MCP</td><td>Weller 1998</td><td>4500+</td></tr>
<tr><td><a href="https://github.com/FEniCS/dolfinx">FEniCS</a></td><td>FEA</td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td><td>Baratta 2023</td><td>—</td></tr>
<tr><td><a href="https://gitlab.onelab.info/gmsh/gmsh">Gmsh</a></td><td>Mesh</td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td><td>Geuzaine 2009</td><td>5100+</td></tr>
<tr><td><a href="https://github.com/Kitware/VTK">VTK</a> / <a href="https://github.com/Kitware/ParaView">ParaView</a></td><td>Viz</td><td>✅ Native</td><td>✅</td><td>✅</td><td>✅ ParaView-MCP (LLNL)</td><td>Schroeder 2006</td><td>3500+</td></tr>
<tr><td><a href="https://github.com/su2code/SU2">SU2</a></td><td>CFD/MDO</td><td>pySU2 (SWIG)</td><td>✅</td><td>✅</td><td>—</td><td>Economon 2016</td><td>—</td></tr>
<tr><td><a href="https://github.com/mfem/mfem">MFEM</a></td><td>FEA</td><td>PyMFEM</td><td>✅</td><td>✅</td><td>—</td><td>Kolev 2024</td><td>—</td></tr>
<tr><td><a href="https://github.com/dealii/dealii">deal.II</a></td><td>FEA</td><td>Limited</td><td>✅</td><td>✅</td><td>—</td><td>Arndt 2020</td><td>510+</td></tr>
<tr><td><a href="https://github.com/DualSPHysics/DualSPHysics">DualSPHysics</a></td><td>SPH</td><td>Inductiva API</td><td>✅</td><td>✅</td><td>—</td><td>Crespo 2015</td><td>746</td></tr>
<tr><td><a href="https://github.com/taichi-dev/taichi">Taichi</a></td><td>Diff. Sim</td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td><td>Hu 2020 (ICLR)</td><td>—</td></tr>
<tr><td><a href="https://github.com/PyFR/PyFR">PyFR</a></td><td>CFD</td><td>✅ Native</td><td>✅</td><td>✅</td><td>—</td><td>Witherden 2014</td><td>202</td></tr>
<tr><td><a href="http://www.calculix.de/">CalculiX</a></td><td>FEA</td><td>pycalculix</td><td>✅</td><td>✅</td><td>—</td><td>Dhondt 2004</td><td>—</td></tr>
<tr><td><a href="https://github.com/ElmerCSC/elmerfem">Elmer</a></td><td>FEA</td><td>PyElmer</td><td>✅</td><td>✅</td><td>—</td><td>Malinen 2013</td><td>—</td></tr>
<tr><td><a href="https://github.com/Open-Cascade-SAS/OCCT">OpenCASCADE</a></td><td>CAD</td><td>pythonOCC</td><td>✅</td><td>✅</td><td>—</td><td>—</td><td>—</td></tr>
</table>

**Legend:** ✅ Available — 🤖 AI-Native = MCP server or LLM agent framework exists — Citations from Google Scholar

<sup>[back to top](#contents)</sup>

## MCP Servers

> Tools that AI agents can call directly via [Model Context Protocol](https://modelcontextprotocol.io).

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` - Cinema-quality science visualization. 22 tools for rendering, slicing, contouring, volume rendering, and animating OpenFOAM/VTK/CGNS data via VTK. Headless EGL/OSMesa.
- [llnl/paraview_mcp](https://github.com/llnl/paraview_mcp) `Python` `MCP` - Natural language control of ParaView via MCP. Multimodal LLM observes viewport for visual feedback (LLNL).
- [webworn/openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) `C++` `MCP` - OpenFOAM MCP server with Socratic questioning for CFD education and expert error resolution.

<sup>[back to top](#contents)</sup>

## CFD — Computational Fluid Dynamics

> Open-source solvers for fluid flow, heat transfer, and multiphysics simulation.

- [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) `C++` - The open source CFD toolbox. Finite volume solvers for incompressible/compressible flow, multiphase, combustion, heat transfer.
- [su2code/SU2](https://github.com/su2code/SU2) `C++` `Python` - Multiphysics simulation and design optimization. Compressible/incompressible flow, structural analysis, adjoint-based design.
- [LLNL/Nek5000](https://github.com/Nek5000/Nek5000) `Fortran` - High-order spectral element CFD solver. DNS/LES of turbulent flows. Scalable to millions of cores.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` - Pythonic VTK interface for 3D plotting and mesh analysis. CFD post-processing, streamlines, glyphs.
- [PyFR/PyFR](https://github.com/PyFR/PyFR) `Python` - High-order flux reconstruction CFD on mixed unstructured grids. GPU-accelerated (CUDA/OpenCL/HIP).
- [precice/precice](https://github.com/precice/precice) `C++` `Python` - Coupling library for multi-physics simulations. Fluid-structure interaction, conjugate heat transfer.

<sup>[back to top](#contents)</sup>

## FEA — Finite Element Analysis

> Structural, thermal, and multiphysics solvers using the finite element method.

- [FEniCS/dolfinx](https://github.com/FEniCS/dolfinx) `C++` `Python` - Next-generation FEniCS. Automated PDE solving with high-level Python/C++ interface. Parallel, scalable.
- [CalculiX](http://www.calculix.de/) `Fortran` `C` - Free 3D structural FEM. Linear/nonlinear static, dynamic, thermal analysis. Abaqus INP compatible.
- [mfem/mfem](https://github.com/mfem/mfem) `C++` - High-order finite element library. Supports GPU acceleration, AMR, and dozens of physics applications.
- [dealii/dealii](https://github.com/dealii/dealii) `C++` - Adaptive finite elements. Supports hp-refinement, multigrid, and parallel distributed computing.
- [ElmerCSC/elmerfem](https://github.com/ElmerCSC/elmerfem) `Fortran` `C++` - Multiphysics FEM solver. Fluid dynamics, structural mechanics, electromagnetics, heat transfer. CSC Finland.
- [Kratos-Multiphysics](https://github.com/KratosMultiphysics/Kratos) `C++` `Python` - Framework for multi-physics FEM. Structural, fluid, thermal, contact, FSI.
- [nschloe/meshio](https://github.com/nschloe/meshio) `Python` - I/O for mesh formats. Convert between Abaqus, Gmsh, VTK, XDMF, Exodus, and 30+ formats.
- [OpenSees/OpenSees](https://github.com/OpenSees/OpenSees) `C++` - Open system for earthquake engineering simulation. Structural and geotechnical response analysis. Berkeley.

<sup>[back to top](#contents)</sup>

## SPH — Smoothed Particle Hydrodynamics

> Meshless particle methods for free-surface flows, fluid-structure interaction, and wave dynamics.

- [DualSPHysics/DualSPHysics](https://github.com/DualSPHysics/DualSPHysics) `C++` `CUDA` - GPU-accelerated SPH solver. Free-surface flows, wave generation, fluid-structure interaction, floating bodies.
- [SPlisHSPlasH/SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH) `C++` - Physically-based SPH fluid simulation. DFSPH, IISPH, PBF pressure solvers. Viscosity, surface tension.
- [pypr/pysph](https://github.com/pypr/pysph) `Python` `Cython` - SPH framework in Python. Compressible/incompressible flows, solid mechanics, coupled problems.

<sup>[back to top](#contents)</sup>

## DEM — Discrete Element Method

> Particle-based simulation of granular materials, powders, and coupled particle-fluid systems.

- [CFDEMproject/LIGGGHTS-PUBLIC](https://github.com/CFDEMproject/LIGGGHTS-PUBLIC) `C++` - Industry-standard open-source DEM for granular materials. LAMMPS-based with heat transfer and CFD coupling (CFDEM).
- [SudoDEM/SudoDEM](https://github.com/SudoDEM/SudoDEM) `C++` `Python` - DEM for non-spherical particles. Polyhedra, super-ellipsoids, and cylinders for realistic granular simulations.

<sup>[back to top](#contents)</sup>

## Visualization & Post-processing

> Rendering, plotting, and interactive exploration of simulation results.

- [kimimgo/viznoir](https://github.com/kimimgo/viznoir) `Python` `MCP` - Cinema-quality science visualization MCP server. 22 tools, EGL/OSMesa headless, cinematic lighting, physics animations.
- [Kitware/VTK](https://github.com/Kitware/VTK) `C++` `Python` - The Visualization Toolkit. 3D computer graphics, image processing, scientific visualization. Industry standard.
- [pyvista/pyvista](https://github.com/pyvista/pyvista) `Python` - Pythonic VTK. Streamlined 3D plotting, mesh analysis, and interactive visualization.
- [Kitware/ParaView](https://github.com/Kitware/ParaView) `C++` `Python` - Multi-platform data analysis and visualization. VTK-based GUI + Python scripting + client-server architecture.
- [napari/napari](https://github.com/napari/napari) `Python` - Fast n-dimensional image viewer. Plugin ecosystem for biomedical and scientific imaging.
- [marcomusy/vedo](https://github.com/marcomusy/vedo) `Python` - Scientific analysis and visualization of 3D objects and point clouds. VTK-based with simple API.
- [plotly/plotly.py](https://github.com/plotly/plotly.py) `Python` - Interactive, publication-quality graphs. 3D scatter, surface, mesh, volume. Web-based rendering.

<sup>[back to top](#contents)</sup>

## CAD & Geometry

> Parametric modeling, geometry processing, and CAD data exchange tools.

- [CadQuery/cadquery](https://github.com/CadQuery/cadquery) `Python` - Parametric 3D CAD scripting. Build models with Python, export STEP/STL/IGES. OpenCASCADE kernel.
- [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) `C++` `Python` - Open-source parametric 3D CAD modeler. Part design, FEM workbench, BIM, path (CAM).
- [OpenCASCADE/OCCT](https://github.com/Open-Cascade-SAS/OCCT) `C++` - Open CASCADE Technology. Kernel for 3D surface and solid modeling, CAD data exchange (STEP/IGES).
- [mikedh/trimesh](https://github.com/mikedh/trimesh) `Python` - Load and manipulate triangular meshes. Boolean operations, ray tracing, convex hulls, format conversion.
- [pygmsh/pygmsh](https://github.com/nschloe/pygmsh) `Python` - Python interface for Gmsh. Scripted geometry + mesh generation with parametric control.

<sup>[back to top](#contents)</sup>

## Mesh Generation

> Structured, unstructured, and AI-driven mesh generation for simulation preprocessing.

- [gmsh](https://gitlab.onelab.info/gmsh/gmsh) `C++` `Python` - Full-featured 3D finite element mesh generator. CAD engine, structured/unstructured meshing, built-in post-processing.
- [CGAL/cgal](https://github.com/CGAL/cgal) `C++` - Computational Geometry Algorithms Library. Mesh generation, triangulation, Boolean operations, convex hulls.
- [NETGEN/NETGEN](https://github.com/NGSolve/netgen) `C++` `Python` - Automatic 3D tetrahedral mesh generator. CAD (OCC) integration, mesh optimization, parallel meshing.
- [buaacyw/MeshAnything](https://github.com/buaacyw/MeshAnything) `Python` - Artist-quality mesh generation with autoregressive transformers. Any 3D input to mesh (ICLR 2025 spotlight).
- [OpenMeshLab/MeshXL](https://github.com/OpenMeshLab/MeshXL) `Python` - Foundation model for 3D mesh generation. Pre-trained on Objaverse, text-to-mesh capable (NeurIPS 2024).
- [PyMesh/PyMesh](https://github.com/PyMesh/PyMesh) `Python` `C++` - Geometry processing library. Boolean, convex hull, remeshing, self-intersection repair.

<sup>[back to top](#contents)</sup>

## Differentiable Simulation

> GPU-native, auto-differentiable frameworks designed for ML-physics integration.

- [Autodesk/XLB](https://github.com/Autodesk/XLB) `Python` `JAX` - Differentiable Lattice Boltzmann for physics-ML. Scales to billions of cells on multi-GPU (CPC 2024).
- [google/brax](https://github.com/google/brax) `Python` `JAX` - Massively parallel rigidbody physics on accelerator hardware. Millions of steps/second on TPU (NeurIPS 2021).
- [jax-md/jax-md](https://github.com/jax-md/jax-md) `Python` `JAX` - Differentiable, hardware-accelerated molecular dynamics. Runs on CPU/GPU/TPU via XLA.
- [gbionics/jaxsim](https://github.com/gbionics/jaxsim) `Python` `JAX` - Differentiable multibody dynamics engine. Hardware-accelerated robot learning and control via JAX.
- [NVIDIA/warp](https://github.com/NVIDIA/warp) `Python` `CUDA` - Differentiable simulation and spatial computing. Reverse-mode AD, PyTorch/JAX interop.
- [taichi-dev/taichi](https://github.com/taichi-dev/taichi) `Python` `CUDA` - Productive GPU programming with automatic differentiation. DiffTaichi for differentiable physics (ICLR 2020).
- [tumaer/JAXFLUIDS](https://github.com/tumaer/JAXFLUIDS) `Python` `JAX` - Fully-differentiable CFD solver for 3D compressible single-phase and two-phase flows.

<sup>[back to top](#contents)</sup>

## AI/ML for Simulation

> Neural networks that learn physics: operator learning, foundation models, and ML-accelerated solvers.

- [csml-rpi/Foam-Agent](https://github.com/csml-rpi/Foam-Agent) `Python` `API` - AI agent for automated CFD workflows. LLM-driven OpenFOAM simulation setup and execution.
- [dynamicslab/pykoopman](https://github.com/dynamicslab/pykoopman) `Python` - Data-driven Koopman operator approximation. Dynamical system analysis and prediction from time series.
- [dynamicslab/pysindy](https://github.com/dynamicslab/pysindy) `Python` - Sparse Identification of Nonlinear Dynamics. Data-driven discovery of governing equations from measurements.
- [google/jax-cfd](https://github.com/google/jax-cfd) `Python` - JAX-based CFD. Differentiable Navier-Stokes solvers. GPU-accelerated, auto-differentiable.
- [Koopman-Laboratory/KoopmanLab](https://github.com/Koopman-Laboratory/KoopmanLab) `Python` - Koopman Neural Operator for mesh-free nonlinear PDE solving. Multi-scale decomposition.
- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) `Python` - Deep learning library for PDEs. PINNs, DeepONet. Backends: TensorFlow, PyTorch, JAX, PaddlePaddle.
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

<sup>[back to top](#contents)</sup>

## Optimization

> Topology optimization, multidisciplinary design, and gradient-based engineering optimization.

- [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) `Python` - Multidisciplinary design optimization. NASA-developed. Gradient-based + surrogate-assisted optimization.
- [airbus/pymoo](https://github.com/anyoptimization/pymoo) `Python` - Multi-objective optimization. NSGA-II/III, reference directions, constraint handling, parallelization.
- [dl4to/dl4to](https://github.com/dl4to/dl4to) `Python` `PyTorch` - Deep learning for 3D topology optimization. Autograd + adjoint method for efficient neural optimization.
- [topology-opt/topy](https://github.com/williamhunter/topy) `Python` - Topology optimization with Python. Minimum compliance, heat conduction, mechanism design.
- [M2DOLab/OpenAeroStruct](https://github.com/mdolab/OpenAeroStruct) `Python` - Aerostructural optimization. VLM aerodynamics + beam FEM structures + ply-level composites.

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
- [DrivAerNet](https://github.com/Mohamedelrefaie/DrivAerNet) `Python` - Large-scale automotive CFD dataset. 4000+ car designs with drag coefficients and surface fields.
- [i207M/PINNacle](https://github.com/i207M/PINNacle) `Python` - Comprehensive PINN benchmark with 20 PDE problems across difficulty levels (NeurIPS 2024).
- [NASA TMR](https://turbmodels.larc.nasa.gov/) - Turbulence Modeling Resource. Validation cases for CFD turbulence models with experimental data.
- [pdebench/PDEBench](https://github.com/pdebench/PDEBench) `Python` - Benchmarks for scientific ML. Standardized PDE datasets with baseline models.
- [PolymathicAI/the_well](https://github.com/PolymathicAI/the_well) `Python` - Large-scale collection of diverse physics simulations for ML. Fifteen-plus PDE systems (NeurIPS 2024).

<sup>[back to top](#contents)</sup>

## Learning Resources

> Tutorials, courses, and templates for learning computational engineering and scientific computing.

- [Barba-group/CFDPython](https://github.com/barbagroup/CFDPython) `Python` - Classic "12 Steps to Navier-Stokes" tutorial. Learn CFD fundamentals with Python step by step.
- [ikespand/awesome-machine-learning-fluid-mechanics](https://github.com/ikespand/awesome-machine-learning-fluid-mechanics) - Curated list of ML applications in fluid mechanics. Papers, code, and tutorials.
- [jxx123/simglucose](https://github.com/jxx123/simglucose) `Python` - Type 1 diabetes simulator. Example of AI-in-the-loop biomedical simulation.
- [kks32/phd-thesis-template](https://github.com/kks32/phd-thesis-template) `LaTeX` - Clean PhD thesis template. Widely used in computational mechanics community.
- [maziarraissi/PINNs](https://github.com/maziarraissi/PINNs) `Python` - The foundational PINN reference implementation. Data-driven PDE solutions and discovery (JCP 2019).
- [thunil/Physics-Based-Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning) - Comprehensive collection of physics-based deep learning resources. Papers, code links, and tutorials from TUM.
- [WillDreamer/Awesome-AI4CFD](https://github.com/WillDreamer/Awesome-AI4CFD) - Survey of ML for CFD covering data-driven surrogates, PINNs, and ML-assisted numerical solvers.

<sup>[back to top](#contents)</sup>

<!-- DIVIDER -->
<img src="media/divider.svg" alt="" width="100%">

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [kimimgo](https://github.com/kimimgo) has waived all copyright and related or neighboring rights to this work.
