# Flatten Wood Slabs

This project is a CLI tool for generating G-code for flattening wood slabs on a CNC machine. It allows users to specify the width, length, stepover, depth, and other parameters to generate G-code to flatten a given slab.

## Usage

To use the CLI tool, follow these steps:

1. Run the CLI tool by executing the command `python flatten.py`, setting slab parameters as documented below.

1. Copy the output of the program to your clipbboard

1. Paste the G-code into your CNC controller, such as Mach4

1. Zero your axes
    1. Set your Z-axis zero to the upper-most height of the slab
    1. Set your X-axis zero to the side of the slab closest to true X0
    1. Set your Y-Axis zero to the side of the slab closest to true Y0

1. Run the program to flatten your slab

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

## Web App

Prefer a UI? Install Django (`python -m pip install django`) and run:

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/ and fill in the form to generate G-code without the CLI prompts.

## Development

- Install dependencies: `python -m pip install -r requirements.txt`
- Run tests: `pytest`

## Deploying to Dokku (flattener.ryanlee.site)

- Ensure DNS: `A flattener.ryanlee.site -> <dokku-server-ip>`
- Add domain: `dokku domains:add flattener flattener.ryanlee.site`
- Remove default internal host: `dokku domains:remove flattener flattener.dokku0214onubuntu2004-s-1vcpu-1gb-sfo3-01`
- Enable TLS: `dokku letsencrypt:enable flattener`
- Verify: `dokku domains:report flattener` shows only your real domain

## License

This project is licensed under the [MIT License](LICENSE.txt).
