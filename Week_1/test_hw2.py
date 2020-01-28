import unittest
import hw2

drinks = [
    {"distillery": "Glenfiddich", "type": "singlemalt", "age": 18},
    {"distillery": "Lauder's", "type": "blended", "age": 6},
    {"distillery": "Wild Turkey", "type": "bourbon", "age": 12},
    {"distillery": "Arberlour", "type": "singlemalt", "age": 15}
]


class TestHomeWork2(unittest.TestCase):

    def test_filter_by_age(self):
        expected_drinks = [
            {"distillery": "Glenfiddich", "type": "singlemalt", "age": 18},
            {"distillery": "Arberlour", "type": "singlemalt", "age": 15}
        ]
        self.assertCountEqual(hw2.filter_by_age(drinks, 15), expected_drinks)

    def test_sort_and_modify(self):
        expected_result = [
            {'age': 18, 'distillery': 'Glenfiddich',
                'reversed': 'hciddifnelG', 'type': 'singlemalt'},
            {'age': 15, 'distillery': 'Arberlour',
                'reversed': 'ruolrebrA', 'type': 'singlemalt'},
            {'age': 12, 'distillery': 'Wild Turkey',
                'reversed': 'yekruT dliW', 'type': 'bourbon'},
            {'age': 6, 'distillery': "Lauder's",
                'reversed': "s'reduaL", 'type': 'blended'}
        ]
        self.assertCountEqual(hw2.sort_and_modify(
            drinks, "distillery"), expected_result)


if __name__ == '__main__':
    unittest.main()
