import os
import io
import hashlib

from functools import wraps


class PseudoFile(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode if mode in ('r', 'w', 'a') else 'r'
        self.pos = 0
        self.is_open = False
        self.content = []

    def __hash__(self):
        return int(hashlib.md5(os.linesep.join(self.content).encode('utf-8')).hexdigest(),16)

    def close(self):
        self.is_open = False

    def open(self, mode='r'):
        self.is_open = True
        self.mode = mode

        if self.mode == 'w':
            self.content = []
        if self.mode in ('r', 'w'):
            self.pos = 0

        return self

    def write(self, buffer):
        if self.mode in ('a', 'w'):
            self.content.extend(buffer.split(os.linesep))
        else:
            raise io.UnsupportedOperation("not writable")

    def __repr__(self):
        return "<  Pseudo-File {0}, hash {1!r}  >".format(self.filename, hex(self.__hash__())[2:])

    def __str__(self):
        return repr(self)

    def readlines(self):
        if not self.is_open:
            raise ValueError("I/O operation on closed file.")

        if self.mode == 'r':
            result = os.linesep.join(self.content[self.pos:])
            self.pos = len(self.content)-1
            return result
        else:
            raise io.UnsupportedOperation("not readable")

    def readline(self):
        if not self.is_open:
            raise ValueError("I/O operation on closed file.")

        if self.mode == 'r':
            if self.pos < len(self.content):
                result = self.content[self.pos]
                self.pos += 1
                return result
            else:
                return ""
        else:
            raise io.UnsupportedOperation("not readable")
