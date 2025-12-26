tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} [{status}]")
    print()

while True:
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})
        print("Task added!")

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                num = int(input("Enter task number: "))
                tasks[num-1]["done"] = True
                print("Task marked as done!")
            except:
                print("Invalid input!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
