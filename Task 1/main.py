from task import *
from utils import *

class Task(object):
    def __init__(self):
        self.title = str(console.input("[b][i]Enter title:[/b][/i] "))
        while self.title == "":
            self.title = str(console.input("[b][i]Enter title:[/b][/i] "))
        self.description = str(console.input("[b][i]Enter description:[/b][/i] "))
        print()

def main():
    db = Database("tasks")
    while True:
        todos = db.query()
        
        clear_terminal()
        print()
        printMenu()
        print()
        choice = console.input(("[b][i]Enter your choice:[/i][/b] "))
        
        if choice == "1":
            clear_terminal()
            printTask(db)
            wait_for_enter()
            
        elif choice == "2":
            task = Task()
            db.add_task(task)
            
        elif choice == "3":
            printToDo(todos)
            id = console.input("[b][i]Enter id to remove:[/i][/b] ")
            db.remove_task(id)
            
        elif choice == "4":
            printToDo(todos)
            id = console.input("[b][i]Enter id to update description:[/i][/b] ")
            description = console.input("[b][i]Enter new description:[/i][/b] ")
            db.update_description(id, description)
            
        elif choice == "5":
            printToDo(todos)
            id = console.input("[b][i]Enter id to mark as completed:[/i][/b] ")
            db.update_completed(id, completed=True)
            
        elif choice == "6":
            printToDo(todos)
            ids = console.input("[b][i]Enter id to mass remove:[/i][/b] ")
            for id in ids:
                db.remove_task(id)
        
        elif choice == "7":
            printToDo(todos)
            ids = console.input("[b][i]Enter id to mass update:[/i][/b] ")
            for id in ids:
                db.update_completed(id)
            
        elif choice == "8":
            db.exit()
            break
        
        else:
            pass

if __name__ == "__main__":
    main()
    clear_terminal()