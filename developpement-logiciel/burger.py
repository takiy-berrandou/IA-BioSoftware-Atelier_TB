# burger.py

from datetime import datetime
import os
from pathlib import Path

def get_order_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_bun():
    while True:
        bun = input("Choose your bun (white, whole wheat, gluten-free): ").strip().lower()
        if bun in ["white", "whole wheat", "gluten-free"]:
            return bun
        print("Invalid choice. Try again.")

def get_meat():
    meats = ["beef", "chicken", "veggie"]
    print("Available meats:", ", ".join(meats))
    choice = input("Select your meat: ").strip().lower()
    return choice if choice in meats else "beef"

def get_sauce():
    return input("Enter your preferred sauce: ").strip()

def get_cheese():
    cheeses = ["cheddar", "swiss", "none"]
    choice = input(f"Choose cheese {cheeses}: ").strip().lower()
    return choice if choice in cheeses else "none"

def calculate_burger_price(ingredients):
    base_price = 5.0
    extras = {
        "cheddar": 0.5,
        "swiss": 0.7,
        "white": 0,
        "whole wheat": 0.2,
        "gluten-free": 0.5,
        "chicken": 1,
        "veggie": -0.5
    }
    return base_price + sum(extras.get(i, 0) for i in ingredients)

def assemble_burger():
    bun = get_bun()
    meat = get_meat()
    sauce = get_sauce()
    cheese = get_cheese()

    ingredients = [bun, meat, sauce, cheese]
    price = calculate_burger_price(ingredients)
    timestamp = get_order_timestamp()

    return {
        "timestamp": timestamp,
        "ingredients": ingredients,
        "price": price
    }

def save_burger(burger):
    output_file = Path("burger_orders.txt")
    with output_file.open("a") as f:
        f.write(f"{burger['timestamp']}: {', '.join(burger['ingredients'])} - ${burger['price']:.2f}\n")

def main():
    print("🍔 Welcome to Burger Builder 🍔")
    burger = assemble_burger()
    save_burger(burger)
    print(f"✅ Order complete: {burger}")

if __name__ == "__main__":
    main()
