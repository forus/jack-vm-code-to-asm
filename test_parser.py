import unittest
from parser import *

class Parser(unittest.TestCase):

    def test_parse_empty_input(self):
        inp = []
        out = list(parse(inp))
        self.assertEqual(out, [])

    def test_parse_sub(self):
        inp = [
            'sub',
        ]
        out = list(parse(inp))
        self.assertEqual(out, [
            SubCommand(),
        ])

    def test_parse_add(self):
        inp = [
            'add',
        ]
        out = list(parse(inp))
        self.assertEqual(out, [
            AddCommand(),
        ])

    def test_parse_push(self):
        inp = [
            'push constant 1',
        ]
        out = list(parse(inp))
        self.assertEqual(out, [
            PushCommand('constant', 1),
        ])

    def test_parse_pop(self):
        inp = [
            'pop constant 1',
        ]
        out = list(parse(inp))
        self.assertEqual(out, [
            PopCommand('constant', 1),
        ])


if __name__ == '__main__':
    unittest.main()
