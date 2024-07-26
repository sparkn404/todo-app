from functions import get_todos, write_todos
import time

now = time.strftime("%a %b %d, %Y %H:%M:%S")
print(now)

while True:
    user_input = input("Type (add), (show), (edit), (complete) or (exit): ").strip()
    user_action = user_input.split(" ", 1)
    user_action[0] = user_action[0].lower()

    if 'add' in user_action[0]:
        if len(user_action) > 1:
            todo = user_action[1]
        else:
            todo = input("Enter todo to add: ")
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif 'show' in user_action[0]:
        todos = get_todos()
        for i, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{i + 1}. {item}"
            print(row)

    elif 'edit' in user_action[0]:
        try:
            if len(user_action) > 1:
                number = int(user_action[1]) - 1
            else:
                number = int(input("Which todo do you want to edit: ")) - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            write_todos(todos)
        except Exception as e:
            print(e)
            continue

    elif 'complete' in user_action[0]:
        try:
            if len(user_action) > 1:
                number = int(user_action[1]) - 1
            else:
                number = int(input("Choose todo to complete: ")) - 1
            todos = get_todos()
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            write_todos(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except Exception as e:
            print(e)
            print("Expected format style such as 'Complete 1'")
            continue

    elif 'exit' in user_action[0]:
        break

    else:
        print("The command is not valid")

print("Bye!")


