import unittest
from parser import *

class Parser(unittest.TestCase):

    def assertParsesInto(self, inp, expected_result):
        out = list(parse(inp))
        self.assertEqual(out, expected_result)

    def test_parse_empty_input(self):
        self.assertParsesInto([], [])

    def test_parse_sub(self):
        self.assertParsesInto(
            [
                'sub'
            ],
            [
                Sub(),
            ])

    def test_parse_add(self):
        self.assertParsesInto(
            [
                'add'
            ],
            [
                Add(),
            ])

    def test_parse_push(self):
        self.assertParsesInto(
            [
                'push constant 1',
            ],
            [
                Push('constant', 1),
            ])

    def test_parse_pop(self):
        self.assertParsesInto(
            [
                'pop constant 1',
            ],
            [
                Pop('constant', 1),
            ])


if __name__ == '__main__':
    unittest.main()
