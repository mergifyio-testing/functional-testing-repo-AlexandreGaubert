"""Flag files the failure-first e2e pull requests add to break or fix a test.

A run id prefixes every flag (``s1p.break_a``), so a pull request that merges
never changes what a later scenario sees.
"""

import pathlib

FLAGS = pathlib.Path(__file__).parent / "flags"


def broken(test: str) -> list[str]:
    """Run ids whose `break_<test>` flag is present without its `fix_<test>`."""
    runs = []
    for flag in sorted(FLAGS.glob(f"*.break_{test}")):
        run = flag.name.split(".")[0]
        if not (FLAGS / f"{run}.fix_{test}").exists():
            runs.append(run)
    return runs
