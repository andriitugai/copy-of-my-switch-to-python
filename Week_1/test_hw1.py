import unittest
import hw1

input_dict2 = {
    'key1': 74,
    'key2': "admamention",
    'key3': "s",
    'key4': "undersCore",
    'key5': ['Billable', 'opportunity', 'negotiation', 'durable']
}


class TestHomeWork1(unittest.TestCase):

    def test_rule1(self):
        self.assertEqual(hw1.rule1(73), 'I')
        self.assertNotEqual(hw1.rule1(68), 'H')

    def test_rule2(self):
        self.assertEqual(hw1.rule2('Collaboration'), 'lab')
        self.assertNotEqual(hw1.rule2('intRoduce'), 'rod')
        self.assertNotEqual(hw1.rule2('lab'), 'lab')
        self.assertEqual(hw1.rule2('lab'), '')

    def test_rule3(self):
        self.assertEqual(hw1.rule3('@'), '@')
        self.assertEqual(hw1.rule3('Hi'), 'Hi')

    def test_rule4(self):
        self.assertEqual(hw1.rule4('comma'), ',')
        self.assertEqual(hw1.rule4('semicolon'), ';')
        self.assertEqual(hw1.rule4('Semicolon'), ';')
        self.assertNotEqual(hw1.rule4('SemiCoolon'), ';')
        self.assertEqual(hw1.rule4('SemiCoolon'), '')

    def test_rule5(self):
        self.assertEqual(
            hw1.rule5(['Wine', 'Love', 'Corporation', 'Billboard', 'Cloud']), 'World')
        self.assertEqual(hw1.rule5(
            ['Wine', 'Love', 'Corporation', 'Billboard', 'Cloud', 'Weapon']), 'WLCBCW')

    def test_hw_1(self):
        self.assertEqual(hw1.hw_1(input_dict2), 'James_Bond')


if __name__ == '__main__':
    unittest.main()
