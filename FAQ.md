# Frequently Asked Questions

## What is AI-CAE?

AI-CAE (Artificial Intelligence for Computer-Aided Engineering) is the application of AI and machine learning to engineering simulation, design, and manufacturing. It includes AI agents that automate CFD and FEA workflows, physics-informed neural networks (PINNs) that solve PDEs without mesh generation, neural operators like Fourier Neural Operator (FNO) that learn to predict simulation results in milliseconds, and differentiable simulation frameworks that enable gradient-based optimization through physics.

## What are MCP servers for engineering?

Model Context Protocol (MCP) servers allow AI agents like Claude, ChatGPT, and GitHub Copilot to directly control engineering software. As of 2026, MCP servers exist for OpenFOAM (CFD simulation), ParaView (scientific visualization via LLNL's ParaView-MCP), and VTK (rendering via viznoir). These enable AI agents to set up simulations, run solvers, and render results without human GUI interaction.

## What is the best open-source AI tool for CFD?

OpenFOAM is the most AI-ready CFD solver, with three LLM agent frameworks: Foam-Agent (88% success rate, MCP-native), MetaOpenFOAM (multi-agent from natural language), and an OpenFOAM MCP server. For differentiable CFD, JAX-CFD provides auto-differentiable Navier-Stokes solvers, and JAXFLUIDS offers fully-differentiable 3D compressible flow simulation. For ML-accelerated CFD, NVIDIA PhysicsNeMo includes neural operators and PINNs.

## What is the best PINN library?

DeepXDE is the most widely used physics-informed neural network library, supporting TensorFlow, PyTorch, JAX, and PaddlePaddle backends. It implements PINNs, DeepONet, and handles inverse problems and fractional PDEs. For PyTorch-specific workflows, pinns-torch provides a production-ready implementation, while PINA offers PyTorch Lightning integration with multi-device training.

## How do AI agents run simulations?

AI agents use MCP (Model Context Protocol) or Python APIs to control simulation software. For example, an agent can use Foam-Agent to set up an OpenFOAM case from a natural language description, execute the solver, then use viznoir or ParaView-MCP to visualize results. The [Core Engine Readiness](README.md#core-engine-readiness) table assesses which foundational solvers support this workflow.

## What is the difference between this list and awesome-scientific-computing?

[awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing) lists general numerical computing tools. awesome-ai-cae focuses specifically on the intersection of AI and engineering simulation, evaluating every tool for AI-readiness — whether an AI agent can call it via MCP, API, or CLI.
