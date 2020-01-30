import sys

# Manual input:


def receipts_input(input_set_name: str) -> set:
    ''' Just a shell to improve communication with user
    and let him a chance to avoid empty input.
    input_set_name is needed to communicate with user.
    input_set_name should be a noun describing content of the set in plural form.
    '''
    # Cycle to avoid empty input
    while True:
        input_set = user_input_(input_set_name)

        if not input_set:
            print(f"""
            Your list of {input_set_name} is empty.
            No receipts can be generated.""")
            do_it_again = input("Are you sure to quit? (YES/no)")
            if not do_it_again:
                sys.exit(0)
        else:
            break

    return input_set


def user_input_(input_set_name: str) -> set:
    ''' Fills an empty with the values from user input and returns it.'''

    input_set_ = set()
    while True:
        print(f"There are {len(input_set_)} {input_set_name} in the set")
        input_item = input(
            f"Enter another {input_set_name[:-1]} (empty input for exit): ")
        if not input_item:
            break

        input_set_.add(input_item)

    return input_set_


if __name__ == '__main__':

    print('INGREDIENTS:')
    print('='*20)
    ingredients = receipts_input("ingredients")
    print()
    print('MEASUREMENT UNITS:')
    print('='*20)
    units = receipts_input("units")
    print()
    print('PREPARATION WAYS:')
    print('='*20)
    ways = receipts_input("preparation_ways")

    # print(ingredients)
    # print(units)
    # print(ways)
