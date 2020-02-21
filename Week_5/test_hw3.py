import unittest
# import hw3
import io


# from text_generator import TextGenerator
from hw3_decorator import open_decorator

class TestHomeWork3(unittest.TestCase):

    def test_pseudo_file_repr(self):
        open = open_decorator(io.open)

        test_file_name = "test:21.txt"
        repr_regex = r"<  Pseudo-File test:[a-zA-Z0-9-_.]*, hash \'[0-9a-f]{32}\'  >"

        testfile = open(test_file_name)
        file_repr = repr(testfile)
        self.assertRegex(file_repr,repr_regex )

    def test_write_while_read_mode_exception(self):
        open = open_decorator(io.open)

        test_file_name = "test:21.txt"
        testfile = open(test_file_name, 'r')

        with self.assertRaises(io.UnsupportedOperation):
            testfile.write("some info")


if __name__ == '__main__':
    unittest.main()
