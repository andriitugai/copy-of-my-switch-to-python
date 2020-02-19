import itertools

class NumberedLinesFileIterator(object):

    def __init__(self, file):
        self._filename = file        

    def __iter__(self):
        cnt = itertools.count()
        with open(self._filename,"r") as input_file:
            while True:
                line = input_file.readline()
                if not line:
                    break
                
                yield f"{next(cnt):<5}|   {line}"        

    def __enter__(self):
        return self.__iter__()

    def __exit__(self, *args):
        pass

def main():
    print("Execution in common way:")
    iterable = NumberedLinesFileIterator(file="file.txt")
    for line in iterable:
        print(line, end="")

    print()

    print("Execution using context manager:")
    with NumberedLinesFileIterator(file="file.txt") as iterable:
        for line in iterable:
            print(line, end="")


if __name__ == '__main__':
    main()

