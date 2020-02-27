import io

from text_generator import TextGenerator
from hw3_decorator import open_decorator


def main():

    open = open_decorator(io.open)    

    open("test:21.txt")
    open("test:22.txt")

    # with open("Week_5\hw3_pseudo_file.py") as a:
    #     print(a.readline(), a.readline(), a.readline(), a.readline(), sep = '\r')

    a = open("test:21.txt")
    print("\n------->>> Check pseudo-file representation:")
    print(a)
    a.close()

    # ----------------------------------------------------------
    print("\n------->>> Check writing mode (80):")
    a = open("test:21.txt", "w")

    para = TextGenerator.get_formatted_para_as_str(80)

    print("\n------->>> Random text #1:")
    print(para)
    a.write(para)
    a.close()

    # ----------------------------------------------------------
    print("\n------->>> Read 2 first lines from 'test:21.txt':")
    a = open("test:21.txt", "r")
    print(a.readline())
    print(a.readline())
    a.close()

    # ----------------------------------------------------------
    print("\n------->>> Check 'adding' mode:")
    a = open("test:21.txt", "a")

    para = TextGenerator.get_formatted_para_as_str(40)

    print("\n------->>> Random text #2 (40):")
    print(para)
    a.write(para)
    a.close()

    # ----------------------------------------------------------
    print("\n------->>> Read all from 'test:21.txt'")
    a = open("test:21.txt")
    content = a.readlines()
    print(content)
    a.close()

    # ----------------------------------------------------------
    print("\n------->>> Add another file:")
    b = open("test:22.txt", "a")

    para = TextGenerator.get_formatted_para_as_str(60)

    print("\n------->>> Random text #3 (60):")
    print(para)
    b.write(para)
    b.close()

    # ----------------------------------------------------------
    print("\n------->>> Read 2 first lines from the second file 'test:22.txt':")
    b = open("test:22.txt", "r")
    print(b.readline())
    print(b.readline())
    b.close()

    # ----------------------------------------------------------
    print("\n------->>> Read 2 first lines from the first file 'test:21.txt':")
    a = open("test:21.txt", "r")
    print(a.readline())
    print(a.readline())
    a.close()


if __name__ == '__main__':
    main()








