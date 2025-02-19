#to do list Nicholas Larsen

#Marks a task as complete
def mark_done(to_dos):
    pass

#Adds an item with the proper formatting to the list of to-dos.
def add_item(to_dos):
    with open('To-Do list/task.txt', 'a') as file:
        while True:
            task = input("What would you like to add? Use 'e' to exit to main menu.")
            file.write(f'{task}:Incomplete ')
            to_dos = sync()
            display(to_dos)

def remove_item(to_dos):
    pass

#Prints the to-dos in a nice way.
def display(applicable):
    print("Tasks:")
    for i in applicable:
        if i[1] == 'Incomplete':
            print(f'\nTo-do:{i[0]}')
        else:
            print(f'\nDone:{i[0]}')

def view_tasks(to_dos):
    pass

#Syncs the list 'to_dos' with the txt files that stores the to-do list.
def sync():
    with open('To-Do list/task.txt', 'r') as file:
            to_dos = []
            text = file.read().split()
            for i in text():
                i = i.split(':')
                to_dos.append(i)
    return to_dos

def main():
    print("Welcome to your to-do list manager!")
    while True:
        to_dos = sync()
        choice = input("Would you like to\n1:Add a task to your to-do list\n2:Remove an item from your to-do list\n3:Mark an item as complete on your to-do list\n4:View your to-do list\n5:Exit (To-do list will be saved.)\n").strip()
        if choice == '1':
            add_item(to_dos)
        elif choice == '2':
            remove_item(to_dos)
        elif choice == '3':
                mark_done(to_dos)
        elif choice == '4':
            view_tasks(to_dos)
        elif choice == '5':
            print("Goodbye!")
            exit()
        else:
            print("Please enter 1, 2, 3, 4, or 5.")

main()