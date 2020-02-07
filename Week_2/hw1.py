from hw1_data import dict_1, list_1


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 1) Cписок квадратов всех позитивных значений типа int, которые делятся на 2 без остатка
# используя List Comprehensions-> list
int_squares = [n**2 for n in list_1 if type(n) is int and n > 0 and n % 2 == 0]


# 2) Cписок кубов всех негативных значений типа float, которые НЕ делятся на 2 без остатка,
# количество знаков после запятой: 2 используя List Comprehensions -> list
positive_float_cubes = [
    round(n**3, 2) for n in list_1 if type(n) is float and n < 0 and n % 2 != 0]


# 3) Cобрать предложение из слов используя ф-ю is_number
# используя List Comprehensions -> str sentence
sentence = ' '.join([w for w in list_1 if not is_number(w)])


# 4) Посчитать сумму всех негативных значений используя ф-ю is_number
# используя List Comprehensions -> float
negative_sum = sum([float(num)
                    for num in list_1 if is_number(num) and float(num) < 0])


# 5) Используя dict comprehensions получить словарь из dict_1, в котором ключом будет имя,
# а значением будет строка, которая содержит через запятую два последних скила
# в случае если персонаж является джедаем, в обратном случае значением должна быть роль.
dict_2 = {k: v["skills"][-2:] if v["role"] == 'jedi' else v["role"]
          for k, v in dict_1.items()}


# 7) Используя ф-ю sorter, отсортировать данные из словаря dict_1 в переменную sort_by_height_desc,
# значения должны быть отсортированы по росту в порядке убывания.
# I suppose they meant function sorted instead, and a list of tuples as a result of operation
sort_by_height_desc = sorted(
    dict_1.items(), key=lambda item: item[1]["height"], reverse=True)


# 8) Написать генератор, который будет принимать на вход переменную
# sort_by_height_desc и итерировать ее содержимое, генератор должен быть написан двух видах:
#     - в виде функции
#     - используя generator expression
# присвоить генераторы переменным gen_1, gen_2
def gen_1(list_of_tuples):
    for item in list_of_tuples:
        yield item


gen_2 = (item for item in sort_by_height_desc)


# 9) Используя цикл for, вывести содержимое обоих генераторов в консоль.
def print_hero(hero):
    print(f'\n{hero[0]}')
    for key in hero[1]:
        if type(hero[1][key]) == list:
            print(f'   {key:<9}: {", ".join(hero[1][key])}')
        else:
            print(f'   {key:<9}: {hero[1][key]}')


for hero in gen_1(sort_by_height_desc):
    print_hero(hero)

for hero in gen_2:
    print_hero(hero)
