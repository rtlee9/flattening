import math
from typing import Optional

SAFE_DISTANCE = 0.1


def generate_gcode(
    *,
    width: float,
    length: float,
    stepover: float,
    depth: float,
    passes: int,
    feed_rate: float,
    spindle_speed: float,
    skip_direction: Optional[str] = None,
) -> str:
    """Generate G-code for flattening slabs."""
    step = abs(stepover)
    if step == 0:
        raise ValueError("Stepover must be non-zero.")
    num_x_steps = math.ceil(width / step / 2)
    if skip_direction:
        num_x_steps *= 2

    lines: list[str] = [
        "G90",
        f"F{feed_rate}",
        f"G0 Z{SAFE_DISTANCE}",
        "G0 X0 Y0",
        f"S{spindle_speed} M3",
    ]

    for i in range(passes):
        pass_num = i + 1
        lines.append(f"(Pass number {pass_num})")
        lines.append("G0 X0 Y0")
        lines.append(f"G1 Z-{(pass_num) * depth}")
        for x_step in range(num_x_steps):
            step_index = x_step / 2 if skip_direction else x_step
            start_x = step * step_index * 2
            lines.append(f"X{start_x}")
            lines.append(f"Y{length}")
            next_x = step * (step_index * 2 + (0 if skip_direction == 'backwards' else 1))
            lines.append(f"X{next_x}")
            lines.append("Y0")
        lines.append(f"Z{SAFE_DISTANCE - i * depth}")

    lines.append("M30")
    return "\n".join(lines)

