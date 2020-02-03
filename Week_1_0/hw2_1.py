from pprint import pprint

arr = [
    {"name": "Jack", "age": 20},
    {"name": "Mike", "age": 22},
    {"name": "Paul", "age": 10},
    {"name": "Sergii", "age": 50},
    {"name": "James", "age": 5}
]


def filter_by_age(members_list, age_limit):
    ''' Return list of members whose age gretaer or equal to age_limit'''

    return [member for member in members_list if member["age"] >= age_limit]


def sort_and_modify(members_list, field_to_reverse):
    ''' Return list of members sorted by age (in descending order). 
    Add new field "reversed" which contains reversed value of ["field_to_reverse"]'''

    new_list = sorted(members_list, key=lambda item: item["age"], reverse=True)
    for member in new_list:
        member["reversed"] = member[field_to_reverse][::-1]
    return new_list


if __name__ == '__main__':

    print('arr, init values:')
    pprint(arr)
    # --------------
    print('='*60)
    print('arr, filtered, min age = 20:')
    pprint(filter_by_age(arr, 20))
    # --------------
    print('='*60)
    print('arr, sorted and modified:')
    pprint(sort_and_modify(arr, "name"))
