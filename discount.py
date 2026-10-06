from config import DISCOUNT_RATE
from orders import ask_yes_no


def apply_discount(subtotal):
    is_eligible = ask_yes_no(
        "\nAre you a Senior Citizen or PWD?"
    )

    if not is_eligible:
        return 0.0

    id_number = input(
        " Please enter your Senior Citizen/PWD ID number: "
    ).strip()

    print(f" ID {id_number} verified. 20% discount applied.")

    return subtotal * DISCOUNT_RATE