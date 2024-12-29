from parsing import *
import unittest


class TestParsing(unittest.TestCase):
    def test_var_end(self):
        self.assertFalse(is_end_of_variable('_'))
        self.assertTrue(is_end_of_variable('-'))
        self.assertTrue(is_end_of_variable(')'))
        self.assertTrue(is_end_of_variable('('))


if __name__ == '__main__':
    unittest.main()
