arr = [
    {"name": "Jack", "age": 20},
    {"name": "Mike", "age": 22},
    {"name": "Paul", "age": 10},
    {"name": "Sergii", "age": 50},
    {"name": "James", "age": 5}
]


if __name__ == '__main__':

    divider = '+ {0:-^20} + {0:-^8} +'.format('')
    header = '| {0:^20} | {1:^8} |'.format("Name", "Age", "Name(reversed)")
    row_template = '| {0:<20} | {1:^8} |'

    print('arr, init values:')
    print(divider)
    print(header)
    print(divider)
    for member in arr:
        print(row_template.format(
            member["name"], member["age"]))
    print(divider)
    # --------------
    print('arr, filtered, min age = 20:')
    print(divider)
    print(header)
    print(divider)
    for member in arr:
        if member["age"] >= 20:
            print(row_template.format(member["name"], member["age"]))
    print(divider)
    # --------------
    print('arr, sorted and modified:')
    divider = '+ {0:-^20} + {0:-^8} + {0:-^20} +'.format('')
    header = '| {0:^20} | {1:^8} | {2:^20} |' \
        .format("Name", "Age", "Name(reversed)")
    row_template = f'| {name:<20} | {age:^8} | {rev:>20} |'

    new_list = sorted(arr, key=lambda item: item["age"], reverse=True)

    print(divider)
    print(header)
    print(divider)

    for member in new_list:
        print(row_template.format(
            **member, member["name"][::-1]))
    print(divider)
