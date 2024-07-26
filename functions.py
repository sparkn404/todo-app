import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """
     Read a text file and return the list todo items
    """
    with open(filepath, 'r') as file_read:
        todos_read = file_read.readlines()
    return todos_read


def write_todos(todos_arg, filepath=FILEPATH):
    """
     Write the todo items list in the text file.
    """
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
