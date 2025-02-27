import random
import sys


PARAMS_LIST = ["ingredients", "measurement units", "preparation ways"]


def receipts_input(input_set_name: str) -> set:
    """ Just a shell to improve communication with user
    and let him a chance to avoid empty input.
    input_set_name is needed to communicate with user.
    input_set_name should be a noun describing content of the set in plural form.
    """

    def user_input_(input_set_name: str) -> set:
        """ returns set from user input."""

        input_set_ = set()
        while True:
            print(f"There are {len(input_set_)} {input_set_name} in the set")
            input_item = input(
                f"Enter another {input_set_name[:-1]} (empty input for exit): "
            )
            if not input_item:
                break

            input_set_.add(input_item)

        return input_set_

    print()
    print(input_set_name.upper(), "="*20, sep='\n')

    # Cycle to avoid empty input
    while True:
        input_set = user_input_(input_set_name)

        if not input_set:
            print(
                f"""
            Your list of {input_set_name} is empty.
            No receipts can be generated."""
            )
            doit_again = input("Are you sure to quit? (YES/no)")
            if not doit_again or doit_again.lower()[0] == "y":
                sys.exit(1)
        else:
            break

    return input_set


def create_receipt(ingredients, ways, units):
    # number ingredients in the receipt:
    random.seed(300)
    num_i = random.randrange(1, len(ingredients) + 1)

    random.shuffle(ingredients)
    receipt_ingredients = ingredients[:num_i]

    # create random receipt as a list of dicts:
    receipt = []
    random.seed(321)
    for ingredient in receipt_ingredients:
        item = {
            "ingredient": ingredient,
            "unit": random.choice(units),
            "qty": random.randint(1, 100),
        }
        receipt.append(item)
    way_to_prepare = random.choice(ways)

    return receipt, way_to_prepare


def print_receipt(receipt, way_to_prepare):
    divider = "=" * 52
    print("RECEIPT")
    print(divider)
    for item in receipt:
        print("{ingredient:<30} {unit:^12} {qty:>8}".format(**item))

    print(divider)
    print(f"Way to prepare: {way_to_prepare}")


def main():

    ingredients, units, ways = [list(receipts_input(param))
                                for param in PARAMS_LIST]

    print()
    print()
    print_receipt(*create_receipt(ingredients, ways, units))


if __name__ == "__main__":
    main()
