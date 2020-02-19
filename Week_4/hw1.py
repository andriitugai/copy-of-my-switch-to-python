import sys, traceback

from datetime import datetime
from functools import wraps


class CustomException(Exception):
    
    def __init__(self, message):
        self._message = message   
        
    def __repr__(self):
        return "{0}\n\tMessage: {1}\n\tTimestamp: {2}"\
            .format(self.__class__.__name__, self._message,datetime.now().isoformat())

    def __str__(self):
        return self.__repr__()


def retry(exception, tries=3):
    def dec(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal tries

            while True:
                try:
                    return func(*args, **kwargs)
                except exception as ex:
                    if tries > 0:
                        print("The function {0} has raised exception".format(func.__name__))
                        print(ex)
                        tries -= 1
                        print("Tries left: {0}".format(tries))                        
                        continue
                    else:
                        # exc_type, exc_value, exc_traceback = sys.exc_info()
                        exc_traceback = sys.exc_info()[2]
                        traceback.print_tb(exc_traceback, limit=None, file=sys.stdout)
                        print(ex)
                        break
        return wrapper
    return dec


@retry(CustomException, tries=2)    
def make_trouble():
    raise CustomException("This is description of the custom exception")


def main():    
    make_trouble()


if __name__ == '__main__':
    main()