from commands import *


def parse(iterator):
    for command in iterator:
        command = _normalize_command(command)
        if not command:
            continue
        parts = command.split(' ')
        command_name = parts.pop(0)
        cls = find_subclass_by_command_name(command_name)
        if cls:
            yield cls(*parts)
        else:
            raise ValueError("Unknown command '%s'." % command_name)


def _normalize_command(command):
    return _remove_extra_spaces(_remove_comments(command))


def _remove_extra_spaces(command):
    return ' '.join(command.split())


def _remove_comments(command):
    if '//' in command:
        indx = command.index('//')
        return command[:indx]
    return command
