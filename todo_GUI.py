import todo_function as todo_f
import FreeSimpleGUI as sg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt','w') as file:
        pass

sg.theme('LightBrown10')
label = sg.Text("Type in a task")
input_box= sg.InputText(tooltip="Enter the task here",key='todo_item')
list_box= sg.Listbox(values= todo_f.todo_read(), key='todo_list', enable_events= True, size=(45,10))
add_button= sg.Button("Add")
edit_button= sg.Button("Edit")
delete_button= sg.Button("Delete")
exit_button= sg.Button("Exit")


window=sg.Window("My To-Do App",
                 layout=[[label], [input_box, add_button], [list_box, edit_button,delete_button], [exit_button]])

while True:
    event,values=window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo_list'])

    match event:
        case 'Add':
            todos=todo_f.todo_read()
            new_todos=values['todo_item'] + '\n'
            todos.append(new_todos)
            todo_f.todo_write(todos)
            window['todo_list'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit= values['todo_list'][0]
                new_todo=values['todo_item']

                todos=todo_f.todo_read()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                todo_f.todo_write(todos)
                window['todo_list'].update(values=todos)

            except:
                sg.popup("Select a value from list then write in the item space and click Edit")

        case 'todo_list':

            window['todo_item'].update(value=values['todo_list'][0])

        case "Delete":
            try:
                todo_to_delete=values['todo_list'][0]

                todos=todo_f.todo_read()
                index=todos.index(todo_to_delete)
                todos.remove(todo_to_delete)
                todo_f.todo_write(todos)
                window['todo_list'].update(values=todos)
                window['todo_item'].update(value="")
            except:
                sg.popup("Select an item from the list and click on Delete")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()





