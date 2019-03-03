def parse(iterator):
    for command in iterator:
        parts = command.split(' ')
        command_name = parts.pop(0)
        cls = Command.find_subclass_by_command_name(command_name)
        yield cls(*parts)


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


class SubCommand(Command):
    command_name = 'sub'


class AddCommand(Command):
    command_name = 'add'


class PushCommand(Command):
    command_name = 'push'

    def __init__(self, *args):
        self.segment = args[0]
        self.index = int(args[1])


class PopCommand(Command):
    command_name = 'pop'

    def __init__(self, *args):
        self.segment = args[0]
        self.index = int(args[1])
