# MRGFY-8629 e2e: ordinary tests every leg runs.
import pytest


@pytest.mark.parametrize("n", range(8))
def test_fill(n):
    assert n >= 0
