from config import (
    RESTAURANT_NAME,
    RESTAURANT_ADDRESS,
    RECEIPT_WIDTH
)

from menu import print_divider


def print_receipt(orders, menu_dict, subtotal, discount_amount):

    total = subtotal - discount_amount

    print()

    print_divider("=")
    print(f"{RESTAURANT_NAME:^{RECEIPT_WIDTH}}")
    print(f"{RESTAURANT_ADDRESS:^{RECEIPT_WIDTH}}")
    print_divider("=")

    print(
        f"{'ITEM':<18}"
        f"{'QTY':>5}"
        f"{'PRICE':>9}"
        f"{'TOTAL':>10}"
    )

    print_divider("-")

    for order in orders:

        item_name, quantity = order[0], order[1]
        price = menu_dict[item_name]
        line_total = price * quantity

        print(
            f"{item_name:<18}"
            f"{quantity:>5}"
            f"{price:>9.2f}"
            f"{line_total:>10.2f}"
        )

    print_divider("-")

    print(f"{'Subtotal:':<32}P{subtotal:>8.2f}")

    if discount_amount > 0:
        print(
            f"{'Discount (20%):':<31}"
            f"-P{discount_amount:>7.2f}"
        )

    print_divider("-")

    print(f"{'TOTAL:':<32}P{total:>8.2f}")

    print_divider("=")
    print(f"{'Thank you, come again!':^{RECEIPT_WIDTH}}")
    print_divider("=")