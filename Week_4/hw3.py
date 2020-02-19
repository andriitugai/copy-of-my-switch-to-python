import sys

from datetime import datetime
from types import FunctionType
from typing import List, Dict
from functools import wraps


def call_tracer(func):
    calls = 0
    @wraps(func)
    def on_call(*args, **kwargs):
        nonlocal calls
        calls +=1
        print(f"The {func.__name__} was called {calls} times")
        return func(*args, **kwargs)

    return on_call


def params_logging(func):

    @wraps(func)
    def on_call(*args, **kwargs):
        args_ = ', '.join([str(a) for a in args])
        kwargs_ = ', '.join([f'{key!r}= {val}' for key, val in kwargs.items()])
        
        # According to the task we should show the name of a wrapper!!!
        wrapper_name = sys._getframe(0).f_code.co_name

        print(f"The {wrapper_name} was called with params")
        print(f"     args: ({args_})")
        print(f"     kwargs: {{{kwargs_}}}")

        return func(*args, **kwargs)

    return on_call


def decorate_all(*decorators):
    class MetaDecorate(type):
        def __new__(mcls, clsname, bases, attr_dict):

            for attr, attr_val in attr_dict.items():
                if type(attr_val) is FunctionType and \
                    not attr.startswith('__') and \
                    not attr.endswith('__'):

                    for decorator in decorators:
                        attr_dict[attr] = decorator(attr_dict[attr])

            return type.__new__(mcls, clsname, bases, attr_dict)

    return MetaDecorate


class Module(metaclass=decorate_all(call_tracer, params_logging)):
    NOT_EVALUATED: float = -1.

    def __init__(self, title: str, date: datetime.date):
        self.title: str = title
        self.date: datetime.date = date

    def __hash__(self):
        return hash((self.title, self.date.isoformat()))

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.title}"


class Student(metaclass=decorate_all(call_tracer, params_logging)):

    def __init__(self, name: str, teacher: "Teacher", modules: List[Module]):
        self.name: str = name
        self.teacher: "Teacher" = teacher
        self.modules_table: Dict[Module, float] = {module: Module.NOT_EVALUATED for module in modules}

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def get_mark_by_module(self, module: Module):
        try:
            return self.modules_table[module]
        except KeyError:
            return None

    def set_mark_by_module(self, module: Module, mark: float):
        self.modules_table[module] = mark

    def get_passed_modules(self):
        return list(filter(lambda _, v: v != Module.NOT_EVALUATED, self.modules_table))


class Teacher(metaclass=decorate_all(call_tracer, params_logging)):

    def __init__(self, name: str, level: int):
        self.name: str = name
        self.level: int = level

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def evaluate_student_by_module(self, student: Student, module: Module, mark: float):
        if self is student.teacher:
            student.set_mark_by_module(module=module, mark=mark)


def main():
    mark = 5.

    decorators_module = Module(title="Decorators", date=datetime.today().date())
    metaclasses_module = Module(title="Metaclasses", date=datetime.today().date())

    teacher = Teacher(name="Arthur", level=2)
    rick = Student(name="Rick", teacher=teacher, modules=[decorators_module])
    morty = Student(name="Morty", teacher=teacher, modules=[decorators_module, metaclasses_module])

    teacher.evaluate_student_by_module(student=morty, module=metaclasses_module, mark=mark)
    assert morty.get_mark_by_module(module=metaclasses_module) == mark


if __name__ == '__main__':
    main()
