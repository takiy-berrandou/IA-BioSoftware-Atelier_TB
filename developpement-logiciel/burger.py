# burger.py

import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_order_timestamp():
    """Return the current timestamp formatted as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_bun():
    """Prompt the user to choose a valid bun option."""
    while True:
        bun = input("Choose your bun (white, whole wheat, gluten-free): ").strip().lower()
        if bun in ["white", "whole wheat", "gluten-free"]:
            return bun
        logging.info("Invalid choice. Try again.")


def get_meat():
    """Prompt the user to choose a meat option."""
    meats = ["beef", "chicken", "veggie"]
    logging.info("Available meats: %s", ", ".join(meats))
    choice = input("Select your meat: ").strip().lower()
    return choice if choice in meats else "beef"


def get_sauce():
    """Prompt the user to enter a sauce."""
    return input("Enter your preferred sauce: ").strip()


def get_cheese():
    """Prompt the user to choose a cheese option."""
    cheeses = ["cheddar", "swiss", "none"]
    choice = input(f"Choose cheese {cheeses}: ").strip().lower()
    return choice if choice in cheeses else "none"


def calculate_burger_price(ingredients):
    """Calculate the total price of a burger based on ingredients."""
    base_price = 5.0
    extras = {
        "cheddar": 0.5,
        "swiss": 0.5,
        "gluten-free": 1.0,
        "sauce": 0.3,
        "veggie": -0.5,
    }
    return base_price + sum(extras.get(i, 0) for i in ingredients)


def assemble_burger():
    """Build the burger step-by-step and return its details."""
    bun = get_bun()
    meat = get_meat()
    sauce = get_sauce()
    cheese = get_cheese()
    timestamp = get_order_timestamp()

    ingredients = [bun, meat, cheese, sauce]
    price = calculate_burger_price(ingredients)

    return {
        "timestamp": timestamp,
        "ingredients": ingredients,
        "price": price,
    }


def save_burger(burger):
    """Save the burger order to a text file."""
    output_file = Path("burger_orders.txt")
    with output_file.open("a") as f:
        f.write(f"{burger['timestamp']}: {', '.join(burger['ingredients'])} - ${burger['price']:.2f}\n")


def main():
    """Build, display, and save a burger order."""
    logging.info("🍔 Welcome to Burger Builder 🍔")
    burger = assemble_burger()
    save_burger(burger)
    logging.info("✅ Order complete: %s", burger)


if __name__ == "__main__":
    main()
