from ._formatter import get_master_help
from ._messages import DescriptionMsg, ErrorMsg
from .base import Base


class Master(Base):
    """
    Global CLI configuration.
    """

    version = "0.1.0"

    def __init__(self):
        self._command = self.parse.get_command()
        self._commands = {}

    def mod_main_help(self):
        """
        Generate the Info message for the CLI app.
        """
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description()

        return get_master_help(description, self._commands)

    def _execute_command(self):
        if self._command in self._commands.keys():
            return self._commands[self._command]()

        print(ErrorMsg.wrong_command(self._command))

    def register(self, *args):
        """
        Register all the commands.

        Arguments:
            *args {class} -- Classes that inherit from Command
        """
        [self._commands.setdefault(command.command_name, command) for command in args]

    def run(self):
        """
        Execute the Command Line App.
        """
        if self._command:
            return self._execute_command()

        print(self.mod_main_help())
