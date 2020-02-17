from datetime import datetime
from functools import wraps
from time import time, sleep


class CustomException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        print(f"Timestamp: {datetime.now().isoformat()}")


def retry(t_func, exceptions=ValueError, tries=3):
    @wraps(t_func)
    def wrapped_func(*args, **kwargs):
        nonlocal tries
        try:
            print(f"wrapped by wrapper")
            print(f"{tries} left")
            t_func(*args, **kwargs)
        except exceptions:
            if tries > 0:
                print(datetime.now().isoformat())
                # raise CustomException('This is description of the custom exception')
                tries -= 1
            else:
                print("No more tries left")
                raise exceptions

    return wrapped_func


@retry
def make_trouble():
    print("Hello World!")
    raise ValueError


def main():
    make_trouble()
    sleep(1)
    make_trouble()
    sleep(1)
    make_trouble()
    sleep(1)
    make_trouble()
    sleep(1)
    make_trouble()


if __name__ == '__main__':
    main()