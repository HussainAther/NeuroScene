# 🧠 NeuroScene

> **A modular, extensible 3D scene framework for scientific visualization and artistic rendering.**
> Inspired by Pixar’s OpenUSD/Hydra pipeline — reimagined for solo creators and systems thinkers.

---

## 🚀 Overview

**NeuroScene** is a real-time, hybrid creative-technical engine for building, rendering, and animating spatial systems from scientific or abstract data.

It’s a personal pipeline — part renderer, part simulator, part sketchbook — that merges scientific insight with artistic storytelling. Built using C++ and Python with GPU rendering via OpenGL, NeuroScene borrows architectural ideas from Pixar’s **Hydra** and NVIDIA’s **Omniverse**, then adapts them into a more expressive, modular sandbox.

---

## 🎯 What It’s For

- 🎨 Visualize **neuroscience**, **physics**, or **cell simulations** with GPU rendering
- 🎥 Animate and stage data as if it were characters in a film
- 🧪 Build plugins for **simulation**, **visual abstraction**, or **creative tooling**
- 🛠️ Prototype **artist/scientist workflows** with Hydra-inspired modularity

---

## 📁 Project Structure

```

NeuroScene/
├── core/
│   └── SceneGraph/
│       └── SceneNode.hpp        # C++ scene node system
├── examples/
│   └── paintable\_brain.py       # Python OpenGL EEG heatmap demo
├── docs/
│   └── WHY.md                   # Vision & motivation
├── CMakeLists.txt               # Build config for C++ core
├── README.md
├── requirements.txt             # Python deps
└── .gitignore

````

---

## 🧩 Features

- 🔧 **Scene Graph Engine** (C++): USD-style nodes, transforms, attributes
- 🎮 **GPU Rendering**: Python + OpenGL via `moderngl`
- 🎨 **Stylized Output**: Shaders for data-driven storytelling
- 🧠 **Scientific Input**: Supports EEG, simulation data, spatial time series
- 🧰 **Plugin Architecture**: Extensions for rendering passes, behaviors, exporters
- 🎥 **Camera Paths**: Spline-based cinematic rigging (planned)
- 🌐 **Exporters**: USD-lite, GLTF, PNG sequences (planned)

---

## 🛠️ Tech Stack

| Domain           | Tools                             |
| ----------------| --------------------------------- |
| Core Engine      | C++17, pybind11, GLM              |
| GPU Rendering    | Python, moderngl, PyOpenGL        |
| Build System     | CMake                             |
| GUI / Panels     | (Planned: DearPyGUI, Qt, ImGui)   |
| Web Viewer       | (Planned: React + Three.js)       |
| Formats Support  | JSON, CSV, GLTF, USD-lite         |
| Simulation I/O   | NumPy, BioFormats, HDF5           |

---

## 🧠 Example Plugin Ideas

- `NeuralPainter`: Animate qEEG heatmaps on a cortex mesh
- `TimeMorpher`: Interpolate time-evolving systems (e.g. cell tracking)
- `RaypassStylizer`: Shader hook for stylized neural render
- `USDExporter`: Serialize full scene to USD-lite for compositing

---

## 🧪 Demo: `paintable_brain.py`

```bash
pip install -r requirements.txt
python examples/paintable_brain.py
````

> Visualizes simulated EEG activity over time with a GPU fragment shader using `moderngl` and `pygame`.

---

## 💼 Why This Project Exists

NeuroScene was built as a personal challenge and technical preparation for advanced rendering roles like Pixar's Hydra/Visualization team.

It shows:

* C++ + GPU architectural thinking
* Rendering pipeline design inspired by film production tools
* Creative approaches to simulation and storytelling
* Modular design patterns rooted in real-world production constraints

> It’s not just a renderer. It’s a sketchpad for scientific imagination — and a hands-on way to learn what it means to build pipelines like Pixar’s.

See [docs/WHY.md](docs/WHY.md) for a full vision statement.

---

## 🤝 Contributing

Open to collaborators who want to:

* Build new simulation adapters
* Create custom shader modules or plugins
* Help evolve the GPU pipeline or scene graph core

Fork it, open a PR, or reach out!

---

## 📚 Inspirations

* [OpenUSD](https://openusd.org/)
* [Hydra Renderer](https://graphics.pixar.com/usd/docs/Render-Delegates-in-Hydra.html)
* [Omniverse](https://developer.nvidia.com/omniverse)
* [Embree](https://www.embree.org/)
* Custom research tooling + scientific visualization techniques

---

## 🎬 About the Author

This project was created by \[Your Name] as part of a broader goal:

> To blend full-stack software engineering, computer graphics, and machine learning into a unified creative pipeline — one that empowers science to tell visual stories.

If you’re hiring for a team that builds visual systems, creative tools, or next-generation storytelling infrastructure, let’s talk.

