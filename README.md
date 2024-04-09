# 🌡️ Flir Image Converter for Photogrammetry

Transform FLIR thermal images into a format suitable for photogrammetry with ease.

![image (1)](https://github.com/flol3622/FLIRjpegTOtiff/assets/93721496/80bfa60e-43b6-4053-aff8-bbe392417dfb)


## Introduction

This tool enables the conversion of thermal images from FLIR cameras into TIFF format, making them compatible with photogrammetry software. Designed for flexibility, it can be integrated into Python pipelines or used as standalone software.

## Key Features

- **Standalone Conversion:** No need for complex setups—convert images with a simple double-click.🖱️
- **Python Integration:** Seamlessly integrate with your existing Python workflows for automated processing.🐍
- **Tailored for FLIR C3:** Optimized for the FLIR C3 camera, but adaptable for other FLIR camera models with minimal adjustments.
- **Visualization in Agisoft Metashape:** Visualize infrared (IR) values at any stage of your photogrammetry workflow, from image to mesh.

## 💾 Installation and Usage

### Standalone Version

1. Download the [latest version of FLIRtoTIFF](https://github.com/flol3622/FLIRjpegTOtiff/releases/latest).
2. Unzip the downloaded package.
3. Move both `.exe` files into the folder with your FLIR `.jpg` images.
4. Double-click `flir_C3.exe` to start the conversion process (note: startup may be slow).
5. Find the converted images in the newly created `multispectral/` subfolder.

### Use in Agisoft Metashape

Enhance your photogrammetry workflow in Metashape by visualizing IR values:

1. Begin with your standard workflow in Metashape.
2. To visualize IR values:
   - Navigate to `Tools > Set Raster Transform...`.
   - In the `Transform tab`, add `B4/10` into the first output band.
   - In the `Palette tab`, select the "heat" colormap for band B1.
   - Click `↻ update > Auto > Apply` to apply changes.✅

Toggle between RGB and IR values via `Tools > Set Raster Transform...` in the `Transform tab` by enabling or disabling the transform.

## Tailored for Specific Cameras

While optimized for the Flir C3 camera, which combines thermal and RGB capabilities, this tool can be adjusted to accommodate other FLIR cameras. Adjustments may be necessary to cater to the unique raw data formats embedded in different camera models.

## 🙏 Credits

This tool incorporates and adapts valuable work from several sources:
- Raw value to temperature conversion inspired by an [R package by gtatters](https://github.com/gtatters/Thermimage/blob/master/R/raw2temp.R).
- Original Python code contributions from:
  - [Nervengift's read_thermal.py](https://github.com/Nervengift/read_thermal.py)
  - [ITVRoC's FlirImageExtractor](https://github.com/ITVRoC/FlirImageExtractor)


## UV package managing
### Getting started

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv
```

### Create virtual environment

```bash
uv venv  # Create a virtual environment at .venv.
```

### Activate virtual environment

```bash
# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
```

# Install packages

```bash
uv pip install flask                # Install Flask.
uv pip install -r requirements.txt  # Install from a requirements.txt file.
uv pip install -e .                 # Install the current project in editable mode.
uv pip install "package @ ."        # Install the current project from disk.
uv pip install "flask[dotenv]"      # Install Flask with "dotenv" extra.
```

### Generate requirements.txt

```bash
uv pip freeze | uv pip compile - -o requirements.txt  # Lock the current environment.
```