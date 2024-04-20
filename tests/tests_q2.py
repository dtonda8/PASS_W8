import unittest
from Q2 import is_power_of_three
from ed_utils.decorators import number


class Test_Q2(unittest.TestCase):
    @number("2.1")
    def test_examples(self):
        self.assertTrue(is_power_of_three(27))
        self.assertFalse(is_power_of_three(0))
        self.assertFalse(is_power_of_three(-1))

    @number("2.2")
    def test_extra(self):
        self.assertTrue(is_power_of_three(1))
        self.assertTrue(is_power_of_three(3**19))
        self.assertFalse(is_power_of_three(2))
        self.assertFalse(is_power_of_three(-27))
        

if __name__ == '__main__':
    unittest.main()