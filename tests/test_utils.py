import pytest

from slabs.utils import generate_gcode


def test_generate_gcode_basic():
    gcode = generate_gcode(
        width=24,
        length=30,
        stepover=1.2,
        depth=0.125,
        passes=1,
        feed_rate=250,
        spindle_speed=12000,
        skip_direction=None,
    )
    lines = gcode.splitlines()
    assert lines[0] == "G90"
    assert "F250" in lines[1]
    assert "G0 Z0.1" in gcode
    assert "Y30" in gcode
    assert lines[-1] == "M30"


def test_skip_direction_adds_steps():
    base = generate_gcode(
        width=12,
        length=10,
        stepover=1.0,
        depth=0.1,
        passes=1,
        feed_rate=200,
        spindle_speed=10000,
        skip_direction=None,
    )
    skipped = generate_gcode(
        width=12,
        length=10,
        stepover=1.0,
        depth=0.1,
        passes=1,
        feed_rate=200,
        spindle_speed=10000,
        skip_direction="forward",
    )
    base_x_moves = sum(1 for line in base.splitlines() if line.startswith("X"))
    skipped_x_moves = sum(1 for line in skipped.splitlines() if line.startswith("X"))
    assert skipped_x_moves == base_x_moves * 2


def test_stepover_zero_rejected():
    with pytest.raises(ValueError):
        generate_gcode(
            width=10,
            length=10,
            stepover=0,
            depth=0.1,
            passes=1,
            feed_rate=200,
            spindle_speed=10000,
            skip_direction=None,
        )

