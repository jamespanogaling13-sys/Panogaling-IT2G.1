def ask_yes_no(question_text):
    while True:
        answer = input(f"{question_text} (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print(" Invalid input. Please type 'y' or 'n'.\n")


def get_valid_item(menu_dict):
    while True:
        item_name = input(" Item name: ").strip().title()

        if item_name in menu_dict:
            return item_name

        print(" Item not found on the menu. Please try again.\n")


def get_valid_quantity():
    while True:
        quantity_input = input(" Quantity: ").strip()

        if quantity_input.isdigit() and int(quantity_input) > 0:
            return int(quantity_input)

        print(" Invalid quantity. Enter a whole number greater than 0.\n")


def take_orders(menu_dict):
    orders = []
    ordering = True

    while ordering:
        print("\n--- New Item ---")

        item_name = get_valid_item(menu_dict)
        quantity = get_valid_quantity()

        orders.append([item_name, quantity])

        print(f" Added: {quantity} x {item_name}")

        ordering = ask_yes_no("\nOrder another item?")

    return orders


def calculate_subtotal(orders, menu_dict):
    subtotal = 0.0

    for order in orders:
        item_name, quantity = order[0], order[1]
        subtotal += menu_dict[item_name] * quantity

    return subtotal