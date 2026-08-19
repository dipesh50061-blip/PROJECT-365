import json
import task_manager


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(task_manager.tasks, file, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            task_manager.tasks = json.load(file)

    except FileNotFoundError:
        task_manager.tasks = []


def show_menu():
    print("\n" + "=" * 40)
    print("             TASKFLOW")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Statistics")
    print("10. Exit")
    print("=" * 40)


def main():

    load_tasks()

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_manager.add_task()
            save_tasks()

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_manager.complete_task()
            save_tasks()

        elif choice == "4":
            task_manager.delete_task()
            save_tasks()

        elif choice == "5":
            task_manager.edit_task()
            save_tasks()

        elif choice == "6":
            task_manager.search_tasks()

        elif choice == "7":
            task_manager.filter_tasks()

        elif choice == "8":
            task_manager.sort_tasks()

        elif choice == "9":
            task_manager.show_statistics()

        elif choice == "10":
            save_tasks()
            print("\nThank you for using TASKFLOW!")
            print("Goodbye 👋")
            break

        else:
            print("\nInvalid choice. Please select 1-10.")


if __name__ == "__main__":
    main()