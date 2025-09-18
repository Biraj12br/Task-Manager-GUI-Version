FILEPATH="todo.txt"

def todo_read(file_path=FILEPATH):
    """ Reads the content of the file and returns a list """
    with open(file_path) as file:
        todos_read=file.readlines()
    return todos_read

def todo_write(todos_arg,file_path=FILEPATH):
    """ Write the to-do items list """
    with open(file_path,'w') as file:
        file.writelines(todos_arg)

if __name__=='__main__':
    print(todo_read())