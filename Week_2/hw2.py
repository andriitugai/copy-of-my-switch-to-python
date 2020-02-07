import string
import random

from itertools import count

RAND_INTERVAL = (257, 1000)


# 1)	Напишите coroutine, которая на вход будет принимать сообщение,
#       и возвращать последние 5 сообщений.
#       Допустим, это будут выполненные задачи или имена отработанных функций
def buffered(size=5):
    buffer = [''] * size
    idx = 0
    while True:
        buffer[idx] = yield buffer[idx:]+buffer[:idx]
        idx = (idx+1) % size


b = buffered()
next(b)  # or b.send(None)

for num in range(15):
    print(b.send(f'message #{num}'))


# 2)	Создать 10к объектов, замерять потребляемое кол-во памяти (memory_profiler).
#       Удалить каждый второй элемент, замерять потребляемое кол-во памяти.
#       Вывести кол-во ссылок в каждом из случаев

# *************************
# see memory-profiler.py
# *************************


# 3)	Возвести в степень элементы одного итерируемого объекта,
#       взяв степень из другого итерируемого объекта с помощью map
gen_power = (2 if i % 2 == 0 else 3 for i in range(1, 8))
base = [i*4 for i in range(1, 8)]
powered_base = map(lambda b, p: b**p, base, gen_power)

# 4)	Сделать словарь с помощью zip с 2х lists
lst_upper = [ch for ch in string.ascii_uppercase]
lst_lower = [ch for ch in string.ascii_lowercase]
upper_to_lower = {k: v for k, v in zip(lst_upper, lst_lower)}

# 5)	Сделать словарь с помощью zip с 2х tuples
t_lower = tuple([ch for ch in string.ascii_lowercase])
t_upper = tuple([ch for ch in string.ascii_uppercase])
lower_to_upper = {k: v for k, v in zip(t_lower, t_upper)}

# 6)	Сделать словарь с помощью zip с 2итерируемых объектов
alpha_dict = {k: v for k, v in zip(
    string.ascii_lowercase, count(start=11, step=23))}
