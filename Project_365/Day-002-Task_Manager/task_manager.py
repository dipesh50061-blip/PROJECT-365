from datetime import datetime
import json

tasks = []


def add_task():
    # Validated Title Input
    while True:
        # .strip() prevents them from just hitting the spacebar a bunch of times
        title = input("Enter the task title: ").strip() 
        
        if title:  # This checks if the title is not empty
            break
        else:
            print("Title cannot be empty. Please type something.")


    while True:
        # .strip() removes accidental spaces, .capitalize() makes "high" into "High"
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        
        if priority in ["High", "Medium", "Low"]:
            break # The input is good, break out of the loop and continue
        else:
            print("Invalid input. Please only type High, Medium, or Low.")


    # Validated Deadline Input
    while True:
        deadline = input("Enter a deadline (YYYY-MM-DD): ")
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            
            # Check if the date is in the past
            if deadline_date.date() < datetime.today().date():
                print("Deadline cannot be in the past. Please enter today or a future date.")
                continue # This skips the 'break' and restarts the loop
                
            break # Date is valid AND not in the past, so we exit the loop
            
        except ValueError:
            print("Invalid date. Please use a real date in YYYY-MM-DD format.")

    

    if not tasks:
        new_id = 1

    else:
        new_id = max(t["id"] for t in tasks)+1


    task = {
        "id":new_id,
        "title":title,
        "priority":priority,
        "deadline":deadline_date.strftime("%Y-%m-%d"),
        "status":"pending"
    }

    tasks.append(task)

    print(f"\nSuccess! Task '{title}' (ID: {new_id}) added for {task['deadline']}.")


def display_tasks(task):
    print("\n-----------------")
    print(f'ID         : {task["id"]}')
    print(f'Title      : {task["title"]}')
    print(f'Priority   : {task["priority"]}')
    print(f'Deadline   : {task["deadline"]}')
    print(f'Status     : {task["status"]}')
    print("\n-----------------")


def view_tasks():
    if not tasks:
        print("No task to show")
        return

    for task in tasks:
        print(f'\nTask {task["id"]}')
        display_tasks(task)

def complete_task():
    if not tasks:
        print("No task to show")
        return

    # Validated ID Input Loop
    while True:
        user_input = input("Enter the id of task: ").strip()
        
        # Check if they left it empty
        if not user_input:
            print("ID cannot be empty. Please enter a number.")
            continue # Restart the loop
            
        try:
            # Try to turn their text into a number
            task_id = int(user_input)
            break # It worked! Exit the loop
            
        except ValueError:
            # They typed letters or symbols instead of a number
            print("Please enter a valid numeric ID.")

    # Now the rest of your logic runs perfectly
    found = False

    for task in tasks:
        if task_id == task["id"]:
            task["status"] = "completed"
            print(f"Task {task_id} has been marked as completed!")
            found = True
            break 

    if not found:
        print("Invalid id. No task found with that number.")


def delete_task():
    if not tasks:
        print("No tasks to delete")
        return

    while True:
        user_input = input("Enter the id of the task: ").strip()

        if not user_input:
            print("ID cannot be empty. Please enter a number.")
            continue

        try:
            delete_id = int(user_input)
            break

        except ValueError:
            print("Please enter a valid numeric ID.")

    found = False

    for task in tasks:
        if delete_id == task["id"]:
            tasks.remove(task)

            print(f"Task '{task['title']}' (ID: {delete_id}) has been successfully deleted!")
            found = True
            break

    if not found:
        print("Invalid id. No task found with that number.")


def edit_task():
    # 1. Check if there are tasks
    if not tasks:
        print("No tasks available to edit.")
        return

    # 2. Get the ID safely
    while True:
        user_input = input("Enter the id of the task to edit: ").strip()
        if not user_input:
            print("ID cannot be empty.")
            continue 
        try:
            task_id = int(user_input)
            break 
        except ValueError:
            print("Please enter a valid numeric ID.")

    # 3. Search for the task
    found = False
    for task in tasks:
        if task_id == task["id"]:
            found = True
            print(f"\nEditing Task: '{task['title']}'")
            print("(Press Enter to keep the current value)")

            # --- Edit Title ---
            new_title = input(f"Enter new title (current: {task['title']}): ").strip()
            if new_title:  # If they typed something, update it. Otherwise, do nothing.
                task["title"] = new_title

            # --- Edit Priority ---
            while True:
                new_priority = input(f"Enter new priority (current: {task['priority']}): ").strip().capitalize()
                
                if not new_priority: # If they just hit Enter, skip it
                    break
                    
                if new_priority in ["High", "Medium", "Low"]:
                    task["priority"] = new_priority
                    break
                print("Invalid input. Please type High, Medium, Low, or press Enter to skip.")

            # --- Edit Deadline ---
            while True:
                new_deadline = input(f"Enter new deadline (current: {task['deadline']}) (YYYY-MM-DD): ").strip()
                
                if not new_deadline: # If they just hit Enter, skip it
                    break
                    
                try:
                    parsed_date = datetime.strptime(new_deadline, "%Y-%m-%d")
                    if parsed_date.date() < datetime.today().date():
                        print("Deadline cannot be in the past.")
                        continue 
                    
                    # Update it if it passes all checks
                    task["deadline"] = parsed_date.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid format. Please use YYYY-MM-DD or press Enter to skip.")

            print(f"\nTask {task_id} has been successfully updated!")
            break # Exit the for loop since we found and edited the task

    if not found:
        print("Invalid id. No task found with that number.")

def search_tasks():
    if not tasks:
        print("No tasks available to search")
        return

    while True:
        search = input("Enter a word to search for in the title: ").strip().lower()
        if search:
            break
        print("Search cannot be empty. Please type something.")

    print(f'\n--- Search results for {search} ---')
    found = False

    for task in tasks:
        if search in task["title"].lower():
            print(f"ID: {task['id']} | Title: {task['title']} | Priority: {task['priority']} | Status: {task['status']} | Deadline: {task['deadline']}")

            found = True

    if not found:
        print("No tasks found matching the word.")


def filter_tasks():
    if not tasks:
        print("No tasks availabe to filter")
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
        choice = input("Enter your choice: ").strip()
        if choice in ["1","2","3","4","5","6","7"]:
            break
        print("Invalid choice. Please enter a number between 1 and 7")

    print("\n--- Filter  Results ---")

    today = datetime.today().date()
    found = False

    for task in tasks:
        task_date =datetime.strptime(task["deadline"], "%Y-%m-%d").date()

        filters = False

        if choice == "1" and task["status"] == "pending":
            filters = True
        elif choice == "2" and task["status"] == "completed":
            filters = True
        elif choice == "3" and task["priority"] == "High":
            filters = True
        elif choice == "4" and task["priority"] == "Medium":
            filters = True
        elif choice == "5" and task["priority"] == "Low":
            filters = True
        # For Overdue, we only want tasks that are past the deadline AND still pending!
        elif choice == "6" and task_date < today and task["status"] == "pending":
            filters = True
        elif choice == "7" and task_date == today:
            filters = True

        if filters:
            print(f"ID: {task['id']} | Title: {task['title']} | Priority: {task['priority']} | Status: {task['status']} | Deadline: {task['deadline']}")
            found = True

    if not found:
        print("No task match this filter")


def sort_tasks():
    if not tasks:
        print("No tasks available to sort.")
        return

    # 1. Print the menu
    print("\n--- SORT TASKS ---")
    print("1. Priority: High → Low")
    print("2. Priority: Low → High")
    print("3. Deadline: Earliest → Latest")
    print("4. Deadline: Latest → Earliest")
    print("5. Title: A → Z")
    print("6. Title: Z → A")
    print("7. ID: Low → High")

    # 2. Safely get the user's choice
    while True:
        choice = input("Enter your choice (1-7): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            break
        print("Invalid choice. Please enter a number between 1 and 7.")

    # 3. Create a priority map for sorting
    priority_map = {"High": 1, "Medium": 2, "Low": 3}

    # 4. Sort the list based on the user's choice
    # We use 'sorted()' to make a temporary sorted copy, leaving the original IDs safe
    if choice == "1":
        # Sorts by looking up the priority word in our map
        sorted_tasks = sorted(tasks, key=lambda t: priority_map[t["priority"]])
    
    elif choice == "2":
        sorted_tasks = sorted(tasks, key=lambda t: priority_map[t["priority"]], reverse=True)
    
    elif choice == "3":
        # Because we saved dates as YYYY-MM-DD, alphabetical sorting works perfectly!
        sorted_tasks = sorted(tasks, key=lambda t: t["deadline"])
    
    elif choice == "4":
        sorted_tasks = sorted(tasks, key=lambda t: t["deadline"], reverse=True)
    
    elif choice == "5":
        # .lower() ensures capital and lowercase letters sort correctly
        sorted_tasks = sorted(tasks, key=lambda t: t["title"].lower())
    
    elif choice == "6":
        sorted_tasks = sorted(tasks, key=lambda t: t["title"].lower(), reverse=True)
    
    elif choice == "7":
        sorted_tasks = sorted(tasks, key=lambda t: t["id"])

    # 5. Print out the sorted list
    print("\n--- Sorted Tasks ---")
    for task in sorted_tasks:
        print(f"ID: {task['id']} | Title: {task['title']} | Priority: {task['priority']} | Status: {task['status']} | Deadline: {task['deadline']}")
    print("-" * 40)



def show_statistics():
    # 1. Set all our counters to zero to start
    total = len(tasks)
    completed = 0
    pending = 0
    high = 0
    medium = 0
    low = 0
    overdue = 0
    due_today = 0

    today = datetime.today().date()

    # 2. Loop through the tasks and count everything
    for task in tasks:
        # Count Status
        if task["status"] == "completed":
            completed += 1
        else:
            pending += 1

        # Count Priorities
        if task["priority"] == "High":
            high += 1
        elif task["priority"] == "Medium":
            medium += 1
        elif task["priority"] == "Low":
            low += 1

        # Count Dates (Only checking pending tasks for overdue/due today)
        if task["status"] == "pending":
            task_date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
            if task_date < today:
                overdue += 1
            elif task_date == today:
                due_today += 1

    # 3. Safely calculate the completion rate percentage
    if total > 0:
        completion_rate = (completed / total) * 100
    else:
        completion_rate = 0.0

    # 4. Print everything in your exact layout
    print("══════════════════════════════")
    print("        TASK STATISTICS")
    print("══════════════════════════════\n")
    print(f"Total Tasks       : {total}")
    print(f"Completed         : {completed}")
    print(f"Pending           : {pending}\n")
    
    # :.1f forces Python to round the percentage to exactly 1 decimal place
    print(f"Completion Rate   : {completion_rate:.1f}%\n")
    
    print(f"High Priority     : {high}")
    print(f"Medium Priority   : {medium}")
    print(f"Low Priority      : {low}\n")
    
    print(f"Overdue           : {overdue}")
    print(f"Due Today         : {due_today}\n")
    print("══════════════════════════════")
