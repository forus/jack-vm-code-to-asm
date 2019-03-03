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

    def test_parse_neg(self):
        self.assertParsesInto(
            [
                'neg'
            ],
            [
                Negate(),
            ])

    def test_parse_eq(self):
        self.assertParsesInto(
            [
                'eq'
            ],
            [
                Equals(),
            ])

    def test_parse_gt(self):
        self.assertParsesInto(
            [
                'gt'
            ],
            [
                GreaterThan(),
            ])

    def test_parse_lt(self):
        self.assertParsesInto(
            [
                'lt'
            ],
            [
                LessThan(),
            ])

    def test_parse_and(self):
        self.assertParsesInto(
            [
                'and'
            ],
            [
                And(),
            ])

    def test_parse_or(self):
        self.assertParsesInto(
            [
                'or'
            ],
            [
                Or(),
            ])

    def test_parse_not(self):
        self.assertParsesInto(
            [
                'not'
            ],
            [
                Not(),
            ])

    def test_parse_unknown(self):
        with self.assertRaises(ValueError) as ve:
            next(parse([ 'unknown' ]))
        self.assertEqual(str(ve.exception), "Unknown command 'unknown'.")

    def test_parse_push(self):
        self.assertParsesInto(
            [
                'push constant 1',
            ],
            [
                Push('constant', 1),
            ])

    def test_parse_push_to_unknown_segment(self):
        with self.assertRaises(ValueError) as ve:
            next(parse([ 'push unknown 1' ]))
        self.assertEqual(str(ve.exception), "Unknown segment 'unknown'.")

    def test_parse_pop(self):
        self.assertParsesInto(
            [
                'pop constant 1',
            ],
            [
                Pop('constant', 1),
            ])

    def test_parse_pop_to_unknown_segment(self):
        with self.assertRaises(ValueError) as ve:
            next(parse([ 'pop unknown 1' ]))
        self.assertEqual(str(ve.exception), "Unknown segment 'unknown'.")

    def test_parse_empty_line(self):
        self.assertParsesInto(
            [
                '',
            ],
            [])

    def test_parse_blank_line(self):
        self.assertParsesInto(
            [
                ' ',
            ],
            [])

    def test_parse_line_comment(self):
        self.assertParsesInto(
            [
                '//Comment comes here',
            ],
            [])

    def test_parse_line_with_extra_spaces_and_comment(self):
        self.assertParsesInto(
            [
                ' push  constant  1 //Comment comes here',
            ],
            [
                Push('constant', 1)
            ])


if __name__ == '__main__':
    unittest.main()
