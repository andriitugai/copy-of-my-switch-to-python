# 2)	Создать 10к объектов, замерять потребляемое кол-во памяти (memory_profiler).
#       Удалить каждый второй элемент, замерять потребляемое кол-во памяти.
#       Вывести кол-во ссылок в каждом из случаев

# for CPython
# def ref_count(address: int):
#     return ctypes.c_long.from_address(address).value

import random

from collections.abc import Mapping, Iterable
from sys import getsizeof, getrefcount
from contextlib import contextmanager


RAND_INTERVAL = (257, 1000)
LIST_SIZE = 10_000


def get_size_refcount(obj, seen=None):
    """Return total size and reference count for object of any of Python's basic types:
    int, float, boolean, str, list, tuple, set, dictionary (may be more).
    Objects of <collections> can contain other collections.
    """
    # Auxilary class for processing results of recursive calls
    class Result(object):
        def __init__(self, size, refcount):
            self.size = size
            self.refcount = refcount

        def __iter__(self):
            yield self.size
            yield self.refcount

        def __add__(self, r2):
            return Result(self.size + r2.size, self.refcount + r2.refcount)

        @staticmethod
        def sum(iterable_of_result):
            return Result(*[sum(col) for col in zip(*iterable_of_result)])

    if seen is None:
        seen = set()

    # one reference was added as an argument of getrefcount
    result = Result(getsizeof(obj), getrefcount(obj) - 1)

    if id(obj) in seen:
        return Result(0, 0)

    seen.add(id(obj))

    if isinstance(obj, Mapping):
        result = result + Result.sum(
            get_size_refcount(k, seen) + get_size_refcount(v, seen)
            for k, v in obj.items()
        )
    elif isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)):
        result = result + Result.sum(get_size_refcount(item, seen) for item in obj)

    return tuple(result)


def generate_list(size, level=0, limit=3):
    """
    Generate random list of random lists of numbers
    size of list of level n+1 25 times less
    param: limit - maximum deep
    """

    randlist = random.choices(range(*RAND_INTERVAL), k=size)

    if level < limit:
        # 4% of elements becomes random lists with the length of 4%
        # hardcode, I know
        subset_size = size // 25
        for idx in random.sample(range(size), subset_size):
            randlist[idx] = generate_list(subset_size, level + 1, limit)

    return randlist


@contextmanager
def header(hdr):
    print()
    print(hdr)
    yield
    print("." * 60)


ROW_TEMPLATE = "Memory consumed: {0}, Number of references: {1}"


def main():

    print("Task # 2:")
    a = generate_list(LIST_SIZE)

    with header(f"For random list of {LIST_SIZE} numbers:"):
        result = ROW_TEMPLATE.format(*get_size_refcount(a))
        print(result)

    del a[::2]

    with header(f"For random list of {LIST_SIZE} numbers:"):
        result = ROW_TEMPLATE.format(*get_size_refcount(a))
        print(result)


if __name__ == "__main__":
    main()
