import os
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """get list from file in argument"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write the to do items in the file"""
    with open(filepath, 'w') as file_read:
        file_read.writelines(todos_arg)


if __name__ == ("__main__"):
    print("Hello")
    print(get_todos())