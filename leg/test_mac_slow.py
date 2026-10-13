# MRGFY-8629 e2e: the macOS leg is slower, so with fail-fast on, the Linux
# leg's failure cancels it before it reports anything.
import sys
import time


def test_slow_on_macos():
    if sys.platform == "darwin":
        time.sleep(150)
