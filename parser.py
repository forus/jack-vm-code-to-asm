def parse(iterator):
    for command in iterator:
        parts = command.split(' ')
        command_name = parts.pop(0)
        cls = Command.find_subclass_by_command_name(command_name)
        if cls:
            yield cls(*parts)
        else:
            raise ValueError("Unknown command '%s'." % command_name)


class Command:
    @classmethod
    def find_subclass_by_command_name(cls, command_name):
        for scls in cls.__subclasses__():
            if scls.command_name == command_name:
                return scls

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)

    def __eq__(self, other):
        return type(other) is type(self) and other.__dict__ == self.__dict__


class Sub(Command):
    command_name = 'sub'


class Add(Command):
    command_name = 'add'


class Negate(Command):
    command_name = 'neg'


class Equals(Command):
    command_name = 'eq'


class GreaterThan(Command):
    command_name = 'gt'


class LessThan(Command):
    command_name = 'lt'


class And(Command):
    command_name = 'and'


class Or(Command):
    command_name = 'or'


class Not(Command):
    command_name = 'not'


class Push(Command):
    command_name = 'push'

    def __init__(self, *args):
        self.segment = args[0]
        self.index = int(args[1])


class Pop(Command):
    command_name = 'pop'

    def __init__(self, *args):
        self.segment = args[0]
        self.index = int(args[1])
