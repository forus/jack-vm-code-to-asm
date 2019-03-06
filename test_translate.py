import unittest
from translate import *

class TranslateTestCase(unittest.TestCase):

    def test_translate_push_min_constant(self):
        # when
        asm_cmds = list(translate([Push('constant', 0)]))
        # then
        self.assertEqual(asm_cmds, [
            # save 0 to D register
            '@0',
            'D=A',
            # write constant from D register to the stack. Effectively *SP=0
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])

    def test_translate_push_max_constant(self):
        # when
        asm_cmds = list(translate([Push('constant', 32767)]))
        # then
        self.assertEqual(asm_cmds, [
            # save 32767 to D register
            '@32767',
            'D=A',
            # write constant from D register to the stack. Effectively *SP=32767
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])

    def test_translate_push_from_0_local_segment(self):
        # when
        asm_cmds = list(translate([Push('local', 0)]))
        # then
        self.assertEqual(asm_cmds, [
            # read first memory cell of local segment value to D register
            '@LCL',
            'D=M',
            # write constant from D register to the stack. Effectively *SP=*LCL
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])

    def test_translate_push_from_10_local_segment(self):
        # when
        asm_cmds = list(translate([Push('local', 10)]))
        # then
        self.assertEqual(asm_cmds, [
            # read 10th memory cell of local segment value to D register
            '@10',
            'D=A',
            '@LCL',
            'A=D+A',
            'D=M',
            # write constant from D register to the stack. Effectively *SP=*LCL
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])

    def test_translate_pop_to_10_local_segment(self):
        # when
        asm_cmds = list(translate([Pop('local', 10)]))
        # then
        self.assertEqual(asm_cmds, [
            # Save LCL+10 to R13 memory cell
            '@10',
            'D=A',
            '@LCL',
            'D=D+A',
            '@R13',
            'M=D',
            # Read value from stack to D register
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            # Record d register to *R13
            '@R13',
            'A=M',
            'M=D',
        ])

if __name__ == '__main__':
    unittest.main()
