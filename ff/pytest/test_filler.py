"""Twenty slow tests that collect before the targets: an early red skips them."""

import time

import pytest


@pytest.mark.parametrize("n", range(20))
def test_filler(n: int) -> None:
    time.sleep(3)
