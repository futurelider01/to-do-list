from todo import ToDoApp
print('Welcome to "To-do" application\nWhat kind of task do you want to add?\n')
print('Func : add, discard, list, status')
con = ToDoApp()
def add(var):
    con.add_task([var])
def discard(var):
    con.discard_task([var])
def show_list():
    return con.list()
def status():
    con.show_status()
while True:
    req = input()
    if req == 'add':
        add(input())
        print('Added\n')
        print('Func : add, discard, list, status')
    elif req == 'discard':
        discard(input())
        print('Discarded\n')
        print('Func : add, discard, list, status')
    elif req == 'list':
        print(show_list())
        print('Func : add, discard, list, status')
    elif req == "status":
        status()
    elif req == 'quit':
        break
    else:
        print("error")
