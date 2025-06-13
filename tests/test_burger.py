"""Unit tests for the burger module."""

from developpement_logiciel import burger


def test_get_order_timestamp_format():
    """Test the timestamp format."""
    timestamp = burger.get_order_timestamp()
    assert isinstance(timestamp, str)
    assert "-" in timestamp
    assert ":" in timestamp


def test_calculate_burger_price():
    """Test burger price calculation."""
    ingredients = ["cheddar", "white", "bbq"]
    price = burger.calculate_burger_price(ingredients)
    assert isinstance(price, float)
    assert price > 0
