import math
import click

SAFE_DISTANCE = 0.1

@click.command()
@click.option("--feed-rate", default=250, help="Feed rate in IPM")
@click.option("--spindle-speed", default=12000, help="Spindle speed in RPM")
@click.option(
    "--passes", default=1, help="Number of passes at a specific Z coordinate to take"
)
@click.option("--depth", default=0.125, help="Depth of cut")
@click.option("--stepover", default=1.24, help="Stepover")
@click.option(
    "--width",
    type=float,
    prompt="Workpiece width",
    help="Width (X axis) of the workpiece to flatten",
)
@click.option(
    "--length",
    type=float,
    prompt="Workpiece length",
    help="Length (Y axis) of the workpiece to flatten",
)
def gen_gcode(width, length, stepover, depth, passes, feed_rate, spindle_speed):
    """Generate g code for flattening slabs."""
    gcode = f"\nG90\nF{feed_rate}\nG0 Z{SAFE_DISTANCE}\nG0 X0 Y0\nS{spindle_speed} M3"
    num_x_steps = math.ceil(width / max(stepover, -stepover) / 2)
    for i in range(passes):
        gcode += f"\n(Pass number {i + 1})\n"
        # move spindle down
        gcode += f"\nG0 X0 Y0\nG1 Z-{(i + 1) * depth}\n"
        for x_step in range(num_x_steps):
            gcode += f"\nX{stepover * x_step * 2}\nY{length}\nX{stepover * (x_step * 2 + 1)}\nY0\n"
        # move spindle up safe distance
        gcode += f"\nZ{SAFE_DISTANCE - i * depth}\M2"

    # TODO: save g code to disk
    print(gcode)


if __name__ == "__main__":
    gen_gcode()
