"""Test A and test Z of the plan's worked example; collected last on purpose."""

from ff import flags


def test_a() -> None:
    assert not flags.broken("a"), f"A broken by {flags.broken('a')}"


def test_z() -> None:
    assert not flags.broken("z"), f"Z broken by {flags.broken('z')}"
