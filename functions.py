FILEPATH = 'todos.txt'


def getdata(filepath=FILEPATH):
    """ Read the to_do list from the text file"""
    with open(filepath, 'r') as file_local:
        new_todos_local = [line.strip() for line in file_local.readlines()]
        return new_todos_local


def write_todo(todos, filepath=FILEPATH):
    """ Write the to_do list to the text file return"""
    with open(filepath, 'w') as file_local:
        file_local.writelines('\n'.join(todos))

