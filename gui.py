import functions
import FreeSimpleGUI as sg

sg.theme('DarkBlue')

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add", font=('Helvetica', 15))
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(44, 10))
edit_button = sg.Button("Edit", font=('Helvetica', 15))
complete_button = sg.Button("Complete", font=('Helvetica', 15))
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"].rstrip('\n') + "\n")
            functions.write_todos(todos)
            window['todo'].update(value="")
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.rstrip("\n") + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica", 20'))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                selected_item = list_box.GetIndexes()[0]
                todos = functions.get_todos()
                todos.pop(selected_item)
                functions.write_todos(todos)
                window['todo'].update(value="")
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica", 20'))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

print("Bye")
window.close()

