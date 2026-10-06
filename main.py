from menu import menu, display_menu
from orders import ask_yes_no, take_orders, calculate_subtotal
from discount import apply_discount
from receipt import print_receipt


def main():

    display_menu(menu)

    wants_to_order = ask_yes_no(
        "\nWould you like to order?"
    )

    if not wants_to_order:
        print("\nThank you for visiting. Goodbye!")
        return

    orders = take_orders(menu)

    subtotal = calculate_subtotal(orders, menu)

    discount_amount = apply_discount(subtotal)

    print_receipt(
        orders,
        menu,
        subtotal,
        discount_amount
    )


if __name__ == "__main__":
    main()