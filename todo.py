def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task(tasks):
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")
def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()