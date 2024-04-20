import unittest
from Q1 import valid_anagram 
from ed_utils.decorators import number

class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertTrue(valid_anagram("anagram", "nagaram"))
        self.assertFalse(valid_anagram("rat", "car"))
        
    @number("1.2")
    def test_extra(self):
        self.assertTrue(valid_anagram("", ""))
        self.assertTrue(valid_anagram("listen", "silent"))
        self.assertFalse(valid_anagram("aabbcc", "aabbc"))

if __name__ == '__main__':
    unittest.main()