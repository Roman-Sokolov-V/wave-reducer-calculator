# Wave Reducer Calculator

A desktop engineering application for calculating, visualizing, and exporting **wave (harmonic) reducer geometry** based on user-defined parameters.

The project combines numerical geometry calculation, 2D visualization, CAD export, and a graphical user interface into a single standalone application.

---

## Core Functionality

The application provides a complete workflow:

1. **Geometric calculation** of wave reducer components  
2. **Interactive visualization** of calculated geometry  
3. **Export to DXF format** for CAD software  
4. **Graphical user interface** with validation and error handling  

---

## Main Features

### Geometry Calculation
- Parametric calculation of wave reducer geometry
- Implemented using **NumPy**
- Validation of geometric constraints
- Custom exceptions for invalid configurations

### Visualization
- 2D visualization using **Matplotlib**
- Embedded directly into the Qt interface (no external plot window)
- Selective rendering of components:
  - wave profile
  - separator
  - balls
  - eccentric
- Automatic redraw on valid input
- Visualization reset on invalid input

### DXF Export
- Export of calculated geometry to **DXF** format
- Implemented using **ezdxf**
- Compatible with CAD software (AutoCAD, SolidWorks, Fusion 360, etc.)

### Graphical User Interface
- Built with **PySide6 (Qt for Python)**
- Responsive and structured layout
- Input validation with user notifications
- Clear separation between UI, logic, and services
- Uses Qt **Fusion** style for consistent cross-platform appearance

### Standalone Application
- Windows executable generated using **PyInstaller**
- No Python installation required to run the application

---

## Technologies Used

- **Python 3.12+**
- **NumPy** — numerical geometry calculations
- **Matplotlib** — 2D visualization
- **ezdxf** — DXF export
- **PySide6** — GUI
- **PyInstaller** — standalone Windows executable

---

## Project Structure
project/   
├── main.py # Application entry point   
├── ui/   
│ └── ui_main_window.py # Qt Designer UI
├── reducer/  
│ ├── geometry.py # Geometry calculations (NumPy)  
│ ├── reducer_params.py # Input parameters  
│ └── exceptions.py # Custom exceptions  
├── services/  
│ ├── reducervisualizer.py # Matplotlib visualization  
│ └── dxf_exporter.py # DXF export (ezdxf)  
├── requirements.txt  
└── README.md  


---

## Error Handling

- All geometric constraints are validated before visualization or export
- Invalid configurations raise explicit custom exceptions
- GUI behavior on error:
  - user notification message
  - prevention of invalid drawing
  - visualization area reset to default state

---

## Running from Source

```bash
  pip install -r requirements.txt
  python main.py
```


Windows Executable

The application can be packaged as a standalone Windows executable using PyInstaller.

The resulting .exe:

runs without Python installed

behaves like a native Windows application

Intended Use

This project is intended for:

engineering calculations

educational purposes

prototyping wave reducer geometry

preparation of CAD-ready DXF files

License

This project is provided for educational and engineering demonstration purposes.
You are free to modify and adapt it for your own use.

## Windows Executable

The application is distributed as a **standalone Windows application** built with **PyInstaller** using the `--onedir` mode.

Prebuilt Windows binaries are available on the **Releases** page.  
➡️ Download: `WaveReducer_Windows_x64_v1.0.0.zip`

### Running the Application

1. Open the generated application directory
2. Run the main executable (`.exe`)
3. No Python installation is required

---

## Intended Use

This project is intended for:
- engineering calculations
- educational purposes
- prototyping wave reducer geometry
- preparation of CAD-ready DXF files

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  


## Author

- **Project Maintainer**: Roman Sokolov
- **Email**: [gnonasis@gmail.com]
- **GitHub**: [@Roman-Sokolov-V](https://github.com/Roman-Sokolov-V)
