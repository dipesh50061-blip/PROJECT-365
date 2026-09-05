from datetime import datetime

from core.helper import (
    PRIORITIES,
    display_task,
    display_task_line,
    find_task_by_id,
    get_valid_deadline,
    get_valid_priority,
    get_valid_task_id,
)


tasks = []


# ============================================================
# ADD TASK
# ============================================================

def add_task():
    """Create and store a new task."""

    while True:
        title = input("Enter the task title: ").strip()

        if title:
            break

        print("Title cannot be empty.")

    priority = get_valid_priority()

    deadline = get_valid_deadline()

    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "priority": priority,
        "deadline": deadline,
        "status": "pending",
    }

    tasks.append(task)

    print(
        f"\n✓ Task '{title}' "
        f"(ID: {new_id}) added successfully."
    )


# ============================================================
# VIEW TASKS
# ============================================================

def view_tasks():
    """Display all tasks."""

    if not tasks:
        print("No tasks to show.")
        return

    print("\n" + "=" * 45)
    print("                  YOUR TASKS")
    print("=" * 45)

    for task in tasks:
        display_task(task)


# ============================================================
# COMPLETE TASK
# ============================================================

def complete_task():
    """Mark a task as completed."""

    task = get_valid_task_id(
        tasks,
        "Enter the ID of the task to complete: "
    )

    if task is None:
        return

    if task["status"] == "completed":
        print(f"Task '{task['title']}' is already completed.")
        return

    task["status"] = "completed"

    print(
        f"✓ Task '{task['title']}' "
        f"(ID: {task['id']}) marked as completed."
    )


# ============================================================
# DELETE TASK
# ============================================================

def delete_task():
    """Delete a task."""

    task = get_valid_task_id(
        tasks,
        "Enter the ID of the task to delete: "
    )

    if task is None:
        return

    tasks.remove(task)

    print(
        f"✓ Task '{task['title']}' "
        f"(ID: {task['id']}) deleted successfully."
    )


# ============================================================
# EDIT TASK
# ============================================================

def edit_task():
    """Edit an existing task."""

    task = get_valid_task_id(
        tasks,
        "Enter the ID of the task to edit: "
    )

    if task is None:
        return

    print("\n" + "=" * 45)
    print(f"Editing Task: {task['title']}")
    print("Press Enter to keep the current value.")
    print("=" * 45)

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    new_title = input(
        f"New title [{task['title']}]: "
    ).strip()

    if new_title:
        task["title"] = new_title

    # --------------------------------------------------------
    # PRIORITY
    # --------------------------------------------------------

    while True:
        new_priority = input(
            f"New priority [{task['priority']}]: "
        ).strip().capitalize()

        if not new_priority:
            break

        if new_priority in PRIORITIES:
            task["priority"] = new_priority
            break

        print("Invalid priority. Choose High, Medium, or Low.")

    # --------------------------------------------------------
    # DEADLINE
    # --------------------------------------------------------

    while True:
        new_deadline = input(
            f"New deadline [{task['deadline']}] (YYYY-MM-DD): "
        ).strip()

        if not new_deadline:
            break

        try:
            deadline_date = datetime.strptime(
                new_deadline,
                "%Y-%m-%d"
            ).date()

            if deadline_date < datetime.today().date():
                print("Deadline cannot be in the past.")
                continue

            task["deadline"] = deadline_date.strftime("%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    print(
        f"\n✓ Task {task['id']} updated successfully."
    )


# ============================================================
# SEARCH TASKS
# ============================================================

def search_tasks():
    """Search tasks by title."""

    if not tasks:
        print("No tasks available to search.")
        return

    while True:
        search_query = input(
            "Enter a word to search for: "
        ).strip().lower()

        if search_query:
            break

        print("Search cannot be empty.")

    matches = [
        task
        for task in tasks
        if search_query in task["title"].lower()
    ]

    print(
        f"\n--- Search Results for '{search_query}' ---"
    )

    if not matches:
        print("No tasks found.")
        return

    for task in matches:
        display_task_line(task)


# ============================================================
# FILTER TASKS
# ============================================================

def filter_tasks():
    """Filter tasks by status, priority, or deadline."""

    if not tasks:
        print("No tasks available to filter.")
        return

    print("\n--- FILTER TASKS ---")
    print("1. Pending")
    print("2. Completed")
    print("3. High Priority")
    print("4. Medium Priority")
    print("5. Low Priority")
    print("6. Overdue")
    print("7. Due Today")

    while True:
        choice = input("Enter your choice (1-7): ").strip()

        if choice in "1234567":
            break

        print("Invalid choice. Enter a number from 1 to 7.")

    today = datetime.today().date()

    matches = []

    for task in tasks:

        task_date = datetime.strptime(
            task["deadline"],
            "%Y-%m-%d"
        ).date()

        if choice == "1":
            if task["status"] == "pending":
                matches.append(task)

        elif choice == "2":
            if task["status"] == "completed":
                matches.append(task)

        elif choice == "3":
            if task["priority"] == "High":
                matches.append(task)

        elif choice == "4":
            if task["priority"] == "Medium":
                matches.append(task)

        elif choice == "5":
            if task["priority"] == "Low":
                matches.append(task)

        elif choice == "6":
            if (
                task["status"] == "pending"
                and task_date < today
            ):
                matches.append(task)

        elif choice == "7":
            if task_date == today:
                matches.append(task)

    if not matches:
        print("No tasks match this filter.")
        return

    print("\n--- FILTER RESULTS ---")

    for task in matches:
        display_task_line(task)


# ============================================================
# SORT TASKS
# ============================================================

def sort_tasks():
    """Display tasks in a selected order."""

    if not tasks:
        print("No tasks available to sort.")
        return

    print("\n--- SORT TASKS ---")
    print("1. Priority: High → Low")
    print("2. Priority: Low → High")
    print("3. Deadline: Earliest → Latest")
    print("4. Deadline: Latest → Earliest")
    print("5. Title: A → Z")
    print("6. Title: Z → A")
    print("7. ID: Low → High")

    while True:
        choice = input("Enter your choice (1-7): ").strip()

        if choice in "1234567":
            break

        print("Invalid choice. Enter a number from 1 to 7.")

    priority_map = {
        "High": 1,
        "Medium": 2,
        "Low": 3,
    }

    if choice == "1":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: priority_map[task["priority"]]
        )

    elif choice == "2":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: priority_map[task["priority"]],
            reverse=True
        )

    elif choice == "3":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task["deadline"]
        )

    elif choice == "4":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task["deadline"],
            reverse=True
        )

    elif choice == "5":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task["title"].lower()
        )

    elif choice == "6":
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task["title"].lower(),
            reverse=True
        )

    else:
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task["id"]
        )

    print("\n--- SORTED TASKS ---")

    for task in sorted_tasks:
        display_task_line(task)


# ============================================================
# TASK STATISTICS
# ============================================================

def task_statistics():
    """Display statistics about the current tasks."""

    total = len(tasks)

    if total == 0:
        print("\nNo tasks available.")
        return

    completed = 0
    pending = 0

    priority_counts = {
        "High": 0,
        "Medium": 0,
        "Low": 0,
    }

    overdue = 0
    due_today = 0

    today = datetime.today().date()

    for task in tasks:

        # Status
        if task["status"] == "completed":
            completed += 1

        elif task["status"] == "pending":
            pending += 1

        # Priority
        priority_counts[task["priority"]] += 1

        # Deadline
        if task["status"] == "pending":

            task_date = datetime.strptime(
                task["deadline"],
                "%Y-%m-%d"
            ).date()

            if task_date < today:
                overdue += 1

            elif task_date == today:
                due_today += 1

    completion_rate = (completed / total) * 100

    print("\n" + "=" * 35)
    print("         TASK STATISTICS")
    print("=" * 35)

    print(f"Total Tasks       : {total}")
    print(f"Completed         : {completed}")
    print(f"Pending           : {pending}")
    print(f"Completion Rate   : {completion_rate:.1f}%")

    print()

    print(
        f"High Priority     : "
        f"{priority_counts['High']}"
    )

    print(
        f"Medium Priority   : "
        f"{priority_counts['Medium']}"
    )

    print(
        f"Low Priority      : "
        f"{priority_counts['Low']}"
    )

    print()

    print(f"Overdue           : {overdue}")
    print(f"Due Today         : {due_today}")

    print("=" * 35)