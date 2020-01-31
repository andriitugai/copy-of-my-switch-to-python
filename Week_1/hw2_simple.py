arr = [
    {"name": "Jack", "age": 20},
    {"name": "Mike", "age": 22},
    {"name": "Paul", "age": 10},
    {"name": "Sergii", "age": 50},
    {"name": "James", "age": 5}
]


def main():

    # we need to create NEW (filtered on "age" >= 20) list
    arr_filtered = [user for user in arr if user["age"] >= 20]

    # print it
    divider = '+ {0:-^20} + {0:-^8} +'.format('')
    header = '| {0:^20} | {1:^8} |'.format("Name", "Age")

    print('arr, filtered, min age = 20:')
    print(divider)
    print(header)
    print(divider)

    for user in arr_filtered:
        print('| {name:<20} | {age:^8} |'.format(**user))

    print(divider)
    print()
    # --------------
    # We don't need to create new list,
    # just print sorted arr with additional field

    divider = '+ {0:-^20} + {0:-^8} + {0:-^20} +'.format('')
    header = '| {0:^20} | {1:^8} | {2:^20} |' \
        .format("Name", "Age", "Name(reversed)")

    print('arr, sorted and modified:')
    print(divider)
    print(header)
    print(divider)

    for user in sorted(arr, key=lambda user: user["age"], reverse=True):
        print(
            '| {name:<20} | {age:>8} | {:>20} |'
            .format(user["name"][::-1], **user)
        )

    print(divider)


if __name__ == '__main__':
    main()
