import sys
from file_handling import Argument

class Controller(object):

    def check_arguments(self):
        arguments = sys.argv
        argument = Argument()
        task = arguments[2:]
        task_string = " ".join(task)
        if len(arguments) == 1:
            argument.arg_without_arguments()
        if "-l" in arguments:
            argument.list_all()
        if "-a" in arguments:
            argument.add_task(task_string)
        if "-r" in arguments:
            argument.remove_task(task_string)
        if "-c" in arguments:
            argument.complete_task(task_string)

cont = Controller()
cont.check_arguments()