from functools import wraps

from .hw3_pseudo_file import PseudoFile

def open_decorator(func):
    '''
    Returns decorator for the resource manager 'open' 
    '''
    if func.__name__ != 'open':
        raise AttributeError("Can't decorate any objects except 'open'")

    filesystem = {}

    @wraps(func)
    def wrapper(filename, mode='r'):
        if filename.startswith("test:"):

            nonlocal filesystem
            if filename not in filesystem:  # New pseudo-file, register it                
                filesystem[filename] = PseudoFile(filename, mode)

            return filesystem[filename].open(mode)

        else:
            return func(filename, mode)

    return wrapper