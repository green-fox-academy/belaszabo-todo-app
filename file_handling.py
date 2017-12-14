import sys

class Argument(object):

    def __init__(self):
        self.num_lines = sum(1 for line in open("todo_list.txt"))

    def arg_without_arguments(self):
        print("\nCommand Line Todo application\n=============================\n\nCommand Line arguments:\n\n-la Lists all the tasks\n-l Lists undone tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

    def list_all(self):
        if self.num_lines == 0:
            print("\nYou don't have any tasks for today! :)\n")
        else:
            print("\nYour tasks are:\n")
            todo_list = open("todo_list.txt", "r")
            line_count = 1
            for _ in range(self.num_lines):
                print(str(line_count) + " - " + str(todo_list.readline()))
                line_count += 1
            todo_list.close()

    def add_task(self, item):
        if len(item) > 0:
            todo_list = open("todo_list.txt", "a")
            todo_list.write("[ ] " + item + "\n")
            todo_list.close()
            print("Task added succesfully!")
        else:
            print("Unable to add: no task provided.")

    def remove_task(self, item):
        if len(item) == 0:
            print("Unable to remove: no index provided.")
        elif not item.isnumeric():
            print("Unable to remove: index is not a number.")
        elif int(item) > self.num_lines:
            print("Unable to remove: index is out of bound.")
        elif len(item) > 0:
            todo_list = open("todo_list.txt", "r+")
            lines = todo_list.readlines()
            item = int(item)
            todo_list.seek(0)
            for i in range(self.num_lines):
                if i + 1 != item:
                    todo_list.write(lines[i])
            todo_list.truncate()
            todo_list.close()
            print("Task removed successfully!")
    
    def complete_task(self, item):
        if len(item) == 0:
            print("Unable to check: no index provided.")
        elif not item.isnumeric():
            print("Unable to check: index is not a number.")
        elif int(item) > self.num_lines or int(item) == 0:
            print("Unable to check: index is out of bound.")
        else:
            todo_list = open("todo_list.txt", "r+")
            lines = todo_list.readlines()
            item = int(item)
            todo_list.seek(0)
            for i in range(self.num_lines):
                if i + 1 != item:
                    todo_list.write(lines[i])
                else:
                    todo_list.write("[x]" + lines[i][3:])
            todo_list.truncate()
            todo_list.close()
            print("Task checked successfully!")

    def list_undone(self):
        if self.num_lines == 0:
            print("\nYou don't have any tasks for today! :)\n")
        else:
            print("\nAll your tasks are:\n")
            todo_list = open("todo_list.txt", "r")
            line_count = 1
            for i in range(self.num_lines):
                is_checked = todo_list.readline()
                if is_checked[1] != "x":
                    print(str(line_count) + " - " + is_checked)
                    line_count += 1
            todo_list.close()
