from os.path import exists
file_exists = exists("To do list.txt")
if file_exists == False:
    open("To do list.txt", "x")

user_choice = -1

list = {}

def show_list():
    for task in list:
            print(task.rstrip())

def task_add():
    task = input("Type the task: ")
    list.append(task)
    print("Task added")

def task_delete():
    option_number = 1

    print("[-1]back <---")

    for task in list:
        print("[" + str(option_number) + "]" + task.rstrip())
        option_number = option_number + 1

    task_del = int(input("Select the option to delete, enter the number: ")) 
    task_del -= 1
    if task_del == -1:
        list.pop(task_del)
        print("Task deleted")

def save_list():
    file = open("To do list.txt", "w")
    for task in list:
        file.write(task + "\n")
    file.close()

def load_list():
    file = open("To do list.txt")
    for line in file.readlines():
        list.append(line)

    file.close()

load_list()

while user_choice != 5:

    try:
        
        if user_choice == 1:
            show_list()

        if user_choice == 2:
            task_add()

        if user_choice == 3:
            task_delete()
        
        if user_choice == 4:
            save_list()


        print("1. Show 'To do list'")
        print("2. Add task")
        print("3. Delete task")
        print("4. Save")
        print("5. Close")
        user_choice = int(input("Choose option: "))

        if user_choice > 5 or user_choice < 1:
            print("There is no option with this number")
            continue

    except ValueError:
        print("Type number, not letters!")
        continue
