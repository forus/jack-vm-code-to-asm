import parser
import translate
import sys

for asm in translate.translate(parser.parse(sys.stdin)):
    print(asm)

