import sys
from collections import namedtuple

_argv = namedtuple("argvs", ["name", "commands", "flags", "arguments"])
_options = namedtuple("options", ["name", "long_flag", "short_flag", "description"])


class Parser:
    def __init__(self):
        self.argv = sys.argv
        self.parsed_argv = self.parse()

    def parse(self):
        """
        Given an iterable of arguments, it returns a namedtuple class with the
        name of the of the script at `parsed_argv.name`, the commands at
        `parsed_argv.commands`, the flags at `parsed_argv.flags` and the rest of
        the arguments at `parsed_argv.arguments`.

        Missing items are filled with `None`.
        """
        name = self.argv[0]

        commands = None
        if len(self.argv) > 1:
            commands = self.argv[1]

        flags = [arg for arg in self.argv if arg.startswith("-")]
        arguments = [arg for arg in self.argv[2:] if not arg.startswith("-")]

        # print(_argv(name, commands, flags, arguments))
        return _argv(name, commands, flags, arguments)

    @property
    def get_command(self):
        return self.parsed_argv.commands

    @property
    def get_argument(self):
        return self.parsed_argv.arguments

    @property
    def get_flags(self):
        return self.parsed_argv.flags

    @property
    def get_app_name(self):
        return self.parsed_argv.name

    def parse_options(self, options):
        """
        Given an iterable of arguments that represents the default and user
        declared options, it returns a namedtuple class with the name of the
        command at `parsed_options.name`, the full flag at `parsed_options.long_flag`,
        the short flags at `parsed_options.short_flag` and the description at
        `parsed_options.description`.
        """
        parsed_options = []
        for name, description in options.items():
            name = name
            long_flag = f"--{name}"
            short_flag = f"-{name[0]}"
            description = description
            parsed_options.append(_options(name, long_flag, short_flag, description))

        return parsed_options
