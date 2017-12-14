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
        elif "-l" in arguments:
            argument.list_all()
        elif "-a" in arguments:
            argument.add_task(task_string)
        elif "-r" in arguments:
            argument.remove_task(task_string)
        elif "-c" in arguments:
            argument.complete_task(task_string)
        else:
            print ("\nUnsupported argument, please see the information on how to use the program below:\n")
            argument.arg_without_arguments()

cont = Controller()
cont.check_arguments()