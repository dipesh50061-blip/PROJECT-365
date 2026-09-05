from datetime import datetime


PRIORITIES = ["High", "Medium", "Low"]


def get_valid_task_id(tasks, prompt="Enter task ID: "):
    """Keep asking until the user enters a valid existing task ID."""

    if not tasks:
        print("No tasks available.")
        return None

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("ID cannot be empty.")
            continue

        try:
            task_id = int(user_input)
        except ValueError:
            print("Please enter a valid numeric ID.")
            continue

        task = find_task_by_id(tasks, task_id)

        if task is None:
            print("No task found with that ID.")
            continue

        return task


def find_task_by_id(tasks, task_id):
    """Return a task dictionary by ID, or None if not found."""

    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def get_valid_priority(prompt="Enter priority (High/Medium/Low): "):
    """Return a valid priority."""

    while True:
        priority = input(prompt).strip().capitalize()

        if priority in PRIORITIES:
            return priority

        print("Invalid priority. Please choose High, Medium, or Low.")


def get_valid_deadline(prompt="Enter deadline (YYYY-MM-DD): "):
    """Return a valid future/today date as YYYY-MM-DD."""

    while True:
        deadline = input(prompt).strip()

        if not deadline:
            print("Deadline cannot be empty.")
            continue

        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()

            if deadline_date < datetime.today().date():
                print("Deadline cannot be in the past.")
                continue

            return deadline_date.strftime("%Y-%m-%d")

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def display_task(task):
    """Display one task in a consistent format."""

    print("\n" + "-" * 40)
    print(f"ID       : {task['id']}")
    print(f"Title    : {task['title']}")
    print(f"Priority : {task['priority']}")
    print(f"Deadline : {task['deadline']}")
    print(f"Status   : {task['status']}")
    print("-" * 40)


def display_task_line(task):
    """Display a compact version of a task."""

    print(
        f"ID: {task['id']} | "
        f"Title: {task['title']} | "
        f"Priority: {task['priority']} | "
        f"Status: {task['status']} | "
        f"Deadline: {task['deadline']}"
    )