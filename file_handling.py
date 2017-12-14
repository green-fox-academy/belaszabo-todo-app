import sys

class Argument(object):

    def __init__(self):
        # argument = Argument()
        pass

    def arg_without_arguments(self):
        print("\nCommand Line Todo application\n=============================\n\nCommand Line arguments:\n-l Lists all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

    def list_all(self):
        num_lines = sum(1 for line in open("todo_list.txt"))
        if num_lines == 0:
            print("\nYou don't have any tasks for today! :)\n")
        else:
            print("\nYour tasks are:\n")
            todo_list = open("todo_list.txt", "r")
            line_count = 1
            for _ in range(num_lines):
                print(str(line_count) + " - " + str(todo_list.readline()))
                line_count += 1

    def add_task(self, item):
        todo_list = open("todo_list.txt", "a")
        num_lines = sum(1 for line in open("todo_list.txt"))
        todo_list.write(item + "\n")
        todo_list.close()
        print("Task added succesfully!")

    def remove_task(self, item):
        todo_list = open("todo_list.txt", "r")
        lines = todo_list.readlines()
        todo_list.close()
        todo_list = open("todo_list.txt", "w")
        for line in lines:
            if line != item:
                todo_list.write(line + "\n")
        todo_list.close()
        print("Task removed successfully!")
    
    def complete_task(self, item):
        pass
