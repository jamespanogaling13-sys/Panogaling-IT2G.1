from config import RESTAURANT_NAME, RECEIPT_WIDTH


menu = {
    "Burger": 89.00,
    "Cheeseburger": 99.00,
    "Fried Chicken": 109.00,
    "Spaghetti": 69.00,
    "Fries": 49.00,
    "Soda": 35.00,
    "Iced Tea": 39.00,
    "Sundae": 45.00,
}


def print_divider(character="="):
    print(character * RECEIPT_WIDTH)


def display_menu(menu_dict):
    print_divider("=")
    print(f"{RESTAURANT_NAME:^{RECEIPT_WIDTH}}")
    print_divider("=")

    print(f"{'MENU':^{RECEIPT_WIDTH}}")
    print_divider("-")

    for item_name in menu_dict:
        price = menu_dict[item_name]
        print(f" {item_name:<28}P{price:>8.2f}")

    print_divider("=")