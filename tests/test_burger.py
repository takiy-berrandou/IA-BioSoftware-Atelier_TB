"""Unit tests for the burger module."""

import unittest

from developpement_logiciel import burger


class TestBurger(unittest.TestCase):
    """Unit tests for functions in the burger module."""

    def test_get_order_timestamp_format(self):
        """Test timestamp is a string with '-' and ':'."""
        timestamp = burger.get_order_timestamp()
        self.assertIsInstance(timestamp, str)
        self.assertIn("-", timestamp)
        self.assertIn(":", timestamp)

    def test_calculate_burger_price(self):
        """Test burger price is a float and > 0."""
        ingredients = ["cheddar", "white", "bbq"]
        price = burger.calculate_burger_price(ingredients)
        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)


if __name__ == "__main__":
    unittest.main()
