# Wave Reducer Calculator

**Engineering-oriented desktop application for calculating, visualizing, and exporting wave reducer geometry.**

This project focuses on **engineering calculations, geometry modeling, and clean separation between computation, visualization, and UI layers**.

---

## Key Features

- **Wave reducer geometry calculation**
  - Parametric computation of wave profile, balls positions, eccentricity, separators
  - Implemented using **NumPy** for numerical stability and performance

- **2D Visualization**
  - Real-time visualization using **Matplotlib**
  - Embedded directly into a **PySide6 (Qt) GUI**
  - Toggleable visualization layers (wave, balls, eccentric, separators)

- **DXF Export**
  - Export calculated geometry to **DXF format** using `ezdxf`
  - Suitable for further processing in CAD software

- **Desktop GUI Application**
  - Built with **PySide6 (Qt Widgets)**
  - Clear separation between UI logic and computation
  - User input validation and error handling

---

## Architecture Overview

The project is intentionally structured to avoid tight coupling between components:

ReducerParams -> parameter validation and configuration  
ReducerGeometry -> pure geometry & math (NumPy-based)  
ReducerVisualizer -> Matplotlib rendering (GUI or standalone)  
ReducerDXFExporter -> DXF export logic (ezdxf)  
GUI (PySide6) -> user interaction layer  


Key design principles:
- **Single Responsibility**
- **Explicit data flow**
- **Reusable visualization logic (GUI & standalone plot)**

---

## Technologies Used

- **Python**
- **NumPy** — numerical geometry calculations
- **Matplotlib** — engineering visualization
- **PySide6 (Qt)** — desktop GUI
- **ezdxf** — CAD-compatible DXF export
- **PyInstaller** — packaging as a Windows application (`--onedir` mode)

---

## Why This Project Matters

This is not a toy GUI project.  
It demonstrates:

- Applying mathematics to real-world mechanical geometry
- Integrating scientific libraries into a desktop GUI
- Managing state, validation, and rendering correctly
- Designing extensible, modular Python code

---

## Target Audience

- Mechanical / CAD-related tooling
- Engineering utilities
- Python desktop applications with scientific computation

---
### Windows Executable

Prebuilt Windows binaries are available on the **Releases** page.  
➡️ Download: `WaveReducer_Windows_x64_v1.0.0.zip`

## Author

- **Project Maintainer**: Roman Sokolov
- **Email**: [gnonasis@gmail.com]
- **GitHub**: [@Roman-Sokolov-V](https://github.com/Roman-Sokolov-V)

