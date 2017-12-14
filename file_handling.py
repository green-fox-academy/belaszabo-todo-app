import sys

class Argument(object):

    def __init__(self):
        # argument = Argument()
        pass

    def arg_without_arguments(self):
        print("\nCommand Line Todo application\n=============================\n\nCommand Line arguments:\n-l Lists all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

    def list_all(self):
        todo_list = open("todo_list.txt", "r")
        print(todo_list.read())

    def add_task(self, item):
        todo_list = open("todo_list.txt", "a")
        num_lines = sum(1 for line in open("todo_list.txt"))
        if num_lines == 0:
            todo_list.write(str(num_lines + 1) + " - " + item)
        else:
            todo_list.write("\n" + str(num_lines + 1) + " - " + item)
        todo_list.close()
        print("Task added succesfully!")

    def remove_task(self, item):
        pass
    
    def complete_task(self, item):
        pass
