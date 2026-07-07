"""Deliberately mixed test results to exercise the failing-test set derivation."""


def test_login_ok() -> None:
    assert 1 + 1 == 2


def test_signup_ok() -> None:
    assert "mergify".upper() == "MERGIFY"


def test_checkout_broken() -> None:
    assert 2 + 2 == 5, "intentional failure: checkout math is wrong"


def test_payment_broken() -> None:
    raise RuntimeError("intentional failure: payment gateway exploded")
