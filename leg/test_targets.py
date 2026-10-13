# MRGFY-8629 e2e: a pull request adds these flags. `break_z` breaks test_z on
# every leg; `break_m` breaks test_m on macOS only.
import pathlib
import sys

FLAGS = pathlib.Path(__file__).parent / "flags"


def test_m():
    assert not ((FLAGS / "break_m").exists() and sys.platform == "darwin"), "broken on macOS"


def test_z():
    assert not (FLAGS / "break_z").exists(), "broken everywhere"
