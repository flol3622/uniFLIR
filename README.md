# Rescale FLIR Images to get consistent temperature values

## 💾 Installation and Usage

1. Download the [latest version of FLIRtoTIFF](https://github.com/flol3622/uniFLIR/releases/latest).
2. Unzip the downloaded package.
3. Move both `.exe` files into the folder with your FLIR `.jpg` images.
4. Double-click `uniFLIR.exe` to start the conversion process (note: startup may be slow).
5. Enter the minimum and maximum temperature values you want to use for rescaling. (press `Enter` after each value)
6. Wait for the conversion to finish. A countdown of the remaining images will be displayed.
7. Find the converted images in the newly created `out/` subfolder.


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