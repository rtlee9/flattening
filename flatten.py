import math
import click


@click.command()
@click.option("--feed-rate", default=250, help="Feed rate in IPM")
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
def gen_gcode(width, length, stepover, depth, passes, feed_rate):
    """Generate g code for flattening slabs."""
    # TODO: incorporate passes and dpeth
    gcode = f"\nG91\nF{feed_rate}\n"
    num_x_steps = math.ceil(width / stepover / 2)
    for i in range(passes):
        gcode += f"\n(Pass number {i + 1})\n"
        if i > 0:
            # move spindle down after the first pass
            gcode += f"\nZ-{depth}\n"
        for x_step in range(num_x_steps):
            if x_step > 0:
                # no need to move spindle to the right on first move
                gcode += f"\nG1 X{stepover}"
            gcode += f"\nG1 Y{length}\nG1 X{stepover}\nG1 Y-{length}\n"


    # TODO: save g code to disk
    print(gcode)


if __name__ == "__main__":
    gen_gcode()
