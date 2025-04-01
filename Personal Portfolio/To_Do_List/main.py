#to do list Nicholas Larsen

#Marks a task as complete
def mark_done(to_dos):
    while True:
        task = input('What task would you like to change the status of? Use e to exit to main menu.\n').strip()
        if task != 'e' and task != 'E':
            success = False
            with open('To-Do list/task.txt', 'w') as file:
                for i in to_dos:
                    if i[0].upper() == task.upper():
                        if i[1] == 'Incomplete':
                            file.write(f'{i[0]}:Complete ')
                            success = True
                        else:
                            file.write(f'{i[0]}:Incomplete ')
                            success = True
                    else:
                        file.write(f'{i[0]}:{i[1]} ')
                if success == True:
                    print("Success!")
                else:
                    print("Sorry, didn't find a task of that name.")
        else:
            break

#Adds an item with the proper formatting to the list of to-dos.
def add_item(to_dos):
    with open('To-Do list/task.txt', 'a') as file:
        while True:
            task = input("What would you like to add? Use 'e' to exit to main menu.\n").strip()
            if task != 'e' and task != 'E':
                file.write(f'{task}:Incomplete ')
                to_dos = sync()
            else:
                return to_dos

#Permenantly removes an item from the to-do list.
def remove_item(to_dos):
        while True:
            to_dos = sync()
            task = input('What task would you like to remove? Use e to exit to main menu.\n').strip()
            if task != 'e' and task != 'E':
                with open('To-Do list/task.txt', 'w') as file:
                    success = False
                    for i in to_dos:
                        if i[0].upper() != task.upper():
                                file.write(f'{i[0]}:{i[1]} ')
                        else:
                            success = True
                    if success == True:
                        print("Success!")
                    else:
                        print("Sorry, didn't find a task of that name.")
            else:
                break

#Prints the to-dos in a nice way.
def display(applicable):
    print("\nTasks:")
    for i in applicable:
        if i[1] == 'Incomplete':
            print(f'\nTo-do:{i[0]}')
        else:
            print(f'\nDone:{i[0]}')
    print('\n')

def view_tasks(to_dos):
    while True:
        choice = input("Would you like to:\n1:View all tasks\n2:View incomplete tasks\n3:Leave\n").strip()
        if choice == '1':
            display(to_dos)
        elif choice == '2':
            applicable = []
            for i in to_dos:
                if i[1] == 'Incomplete':
                    applicable.append(i)
            display(applicable)
        elif choice == '3':
            break
        else:
            print("Please enter 1, 2, or 3.")
        

#Syncs the list 'to_dos' with the txt files that stores the to-do list.
def sync():
    with open('To-Do list/task.txt', 'r') as file:
            to_dos = []
            text = file.read()
            for i in text.split(' '):
                i = i.split(':')
                try:
                    i[1]
                except:
                    pass
                else:
                    to_dos.append(i)
    return to_dos

def to_do_main():
    print("Welcome to your to-do list manager!")
    while True:
        to_dos = sync()
        choice = input("Would you like to:\n1:Add a task to your to-do list\n2:Remove an item from your to-do list\n3:Mark an item as complete or incomplete on your to-do list\n4:View your to-do list\n5:Exit (To-do list will be saved.)\n").strip()
        if choice == '1':
            add_item(to_dos)
        elif choice == '2':
            remove_item(to_dos)
        elif choice == '3':
            mark_done(to_dos)
        elif choice == '4':
            view_tasks(to_dos)
        elif choice == '5':
            return
        else:
            print("Please enter 1, 2, 3, 4, or 5.")