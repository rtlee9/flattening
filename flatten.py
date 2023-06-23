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
    gcode = f"""
G91
{feed_rate}
    """
    num_x_steps = math.ceil(width / stepover / 2)
    for x_step in range(num_x_steps):
        if x_step > 0:
            gcode += f"\nG1 X{stepover}"
        gcode += f"""
G1 Y{length}
G1 X{stepover}
G1 Y-{length}
        """

    # TODO: save g code to disk
    print(gcode)


if __name__ == "__main__":
    gen_gcode()
