from commands import *

def translate(commands):
    for command in commands:
        cls = type(command)
        if cls in _command_to_translation:
            translation = _command_to_translation[cls]
            for asm_line in translation(command):
                yield asm_line


def _push_command(command):
    if command.segment in _segment_to_address:
        return _push(_segment_to_address[command.segment], command.index)
    elif command.segment == 'constant':
        return _push_constant(command.index)
    else:
        raise ValueError('Unknown segment %s' % command.segment)


def _pop_command(command):
    if command.segment in _segment_to_address:
        return _pop(_segment_to_address[command.segment], command.index)
    else:
        raise ValueError('Unknown segment %s' % command.segment)


def _sub_command(command):
    return (_pop_from_stack_to_d_register() +
        [
            '@R5',
            'M=D',
        ] + _pop_from_stack_to_d_register() +
        [
            '@R5',
            'D=M-D',
        ] + _push_d_register_to_stack())


def _add_command(command):
    return (_pop_from_stack_to_d_register() +
        [
            '@R5',
            'M=D',
        ] + _pop_from_stack_to_d_register() +
        [
            '@R5',
            'D=D+M',
        ] + _push_d_register_to_stack())


_command_to_translation = {
    Push: _push_command,
    Pop: _pop_command,
    Sub: _sub_command,
    Add: _add_command,
}


_segment_to_address = {
    'argument': 'ARG',
    'local': 'LCL',
    'static': 'R16',
    'this': 'THIS',
    'that': 'THAT',
    'temp': 'R5',
}


def _push_constant(const):
    return [
        # save const to D register
        '@' + str(const),
        'D=A',
    ] + _push_d_register_to_stack()


def _push(segment, index):
   if index == 0:
       return [
            # save value of the first segment memory cell to D register
            '@' + segment,
            'D=M',
       ] + _push_d_register_to_stack()
   return [
        # save value of the n-th segment memory cell to D register
        '@' + str(index),
        'D=A',
        '@' + segment,
        'A=D+A',
        'D=M',
   ] + _push_d_register_to_stack()


def _push_d_register_to_stack():
    return [
        # write constant from D register to the stack.
        '@SP',
        'A=M',
        'M=D',
        # increase the stack pointer: SP++
        '@SP',
        'M=M+1',
    ]


def _pop(segment, index):
   if index == 0:
       return [
            '@' + segment,
            'D=M',
            '@R13',
            'M=D',
       ] + _pop_from_stack_to_r13_ref()
   return [
        '@' + str(index),
        'D=A',
        '@' + segment,
        'D=D+A',
        '@R13',
        'M=D',
   ] + _pop_from_stack_to_r13_ref()


def _pop_from_stack_to_r13_ref():
    return _pop_from_stack_to_d_register() + [
        '@R13',
        'A=M',
        'M=D',
    ]


def _pop_from_stack_to_d_register():
    return [
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
    ]
