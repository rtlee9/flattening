# Flatten Wood Slabs

This project is a CLI tool for generating G-code for flattening wood slabs. It allows users to specify the width, length, stepover, depth, and other parameters to generate customized G-code for their specific flattening needs.

## Usage

To use the tool, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Open your terminal or command prompt and navigate to the project directory.

3. Run the CLI tool by executing the command `python flatten.py`.

4. Follow the prompts to enter the desired values for the width, length, stepover, depth, and other parameters.

5. Once the G-code is generated, copy it to your clipboard.

6. Paste the G-code into your CNC controller, such as Mach4, to execute the flattening process.

## Options

The CLI tool provides several options to customize the flattening process. Here are the available options:

- `--feed-rate`: Specify the feed rate in IPM (Inches Per Minute).

- `--spindle-speed`: Specify the spindle speed in RPM.

- `--skip-direction`: Specify the direction to skip (forward or backwards).

- `--passes`: Specify the number of passes at a specific Z coordinate to take.

- `--depth`: Specify the depth of cut.

- `--stepover`: Specify the stepover.

- `--width`: Specify the width (X axis) of the workpiece to flatten.

- `--length`: Specify the length (Y axis) of the workpiece to flatten.