import datetime
import time

focus_sessions = []

def start_focus_session():
    # 1. Ask for Task Name
    while True:
        task_name = input("Enter the task name for the focus session: ").strip()
        if task_name:
            break
        else:
            print("Task name cannot be empty. Please enter a valid task name.")

    # 2. Ask for Category
    while True:
        category = input("Enter the category (e.g., Study, Coding, Admin): ").strip().title()
        if category:
            break
        else:
            print("Category cannot be empty. Please enter a valid category.")

    # 3. Ask for Duration
    while True:
        duration = input("Enter the duration of the focus session (in minutes): ").strip()
        if duration:
            try:
                duration = int(duration)
                if duration <= 0:
                    print("Duration must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the duration.")
        else:
            print("Duration cannot be empty. Please enter a valid duration.")

    # 4. NEW: Hybrid Time Input
    while True:
        print("\nWhen did this session start?")
        time_input = input("Enter time (YYYY-MM-DD HH:MM) OR press Enter to start NOW: ").strip()

        if not time_input:
            # They pressed Enter! Start the clock right now.
            start_time = datetime.datetime.now()
            is_completed = False 
            break
        
        try:
            # They typed a custom time. Let's parse it.
            start_time = datetime.datetime.strptime(time_input, "%Y-%m-%d %H:%M")
            is_completed = True 
            break
        except ValueError:
            print("Invalid format. Please use exactly YYYY-MM-DD HH:MM, or press Enter.")

    # 5. Generate ID
    if not focus_sessions:
        new_id = 1
    else:
        new_id = max(session["id"] for session in focus_sessions) + 1

    # 6. Calculate End Time Automatically
    end_time = start_time + datetime.timedelta(minutes=duration)

    # 7. Build the Dictionary
    focus_session = {
        "id": new_id,
        "task_name": task_name,
        "category": category,
        "duration": duration,
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "completed": is_completed 
    }

    focus_sessions.append(focus_session)
    
    # 8. Smart Confirmation Messages
    if is_completed:
        # Message for a retroactively logged session
        print(f"\nSuccess! Past session '{task_name}' [{category}] (ID: {new_id}) logged for {duration} minutes.")
    else:
        # Message for a live session happening right now
        clock_time = end_time.strftime("%I:%M %p")
        print(f"\nFocus session '{task_name}' [{category}] (ID: {new_id}) started for {duration} minutes.")
        print(f"Keep pushing! Your session will end at exactly {clock_time}.")

# 1. The Reusable UI Engine
def display_focus_sessions(sessions_list):
    if not sessions_list:
        print("No focus sessions to display.")
        return

    print("\nFocus Sessions History:")
    print("-" * 95)
    # Using fixed widths so the columns align perfectly every time
    print("{:<5} {:<25} {:<15} {:<12} {:<20} {:<10}".format(
        "ID", "Task Name", "Category", "Duration(m)", "Start Time", "Status"
    ))
    print("-" * 95)

    for session in sessions_list:
        # Cleanly converts the True/False boolean into readable text
        status = "Completed" if session["completed"] else "Active"
        
        print("{:<5} {:<25} {:<15} {:<12} {:<20} {:<10}".format(
            session["id"],
            session["task_name"][:23], # Cuts off super long names so they don't break the table
            session["category"],
            session["duration"],
            session["start_time"],
            status
        ))
    print("-" * 95)


# 2. The Logic Manager
def view_focus_sessions():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return
    else:
        # Hand the global list over to the display function
        display_focus_sessions(focus_sessions)

def complete_focus_session():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    try:
        session_id = int(input("Enter the ID of the focus session to mark as completed: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the session ID.")
        return

    for session in focus_sessions:
        if session["id"] == session_id:
            if session["completed"]:
                print(f"Focus session '{session['task_name']}' (ID: {session_id}) is already marked as completed.")
            else:
                session["completed"] = True
                print(f"Focus session '{session['task_name']}' (ID: {session_id}) marked as completed.")
            return

    print(f"No focus session found with ID: {session_id}. Please check the ID and try again.")

def delete_focus_session():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    try:
        session_id = int(input("Enter the ID of the focus session to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the session ID.")
        return

    for session in focus_sessions:
        if session["id"] == session_id:
            focus_sessions.remove(session)
            print(f"Focus session '{session['task_name']}' (ID: {session_id}) has been deleted.")
            return

    print(f"No focus session found with ID: {session_id}. Please check the ID and try again.")

def edit_focus_session():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    try:
        session_id = int(input("Enter the ID of the focus session to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the session ID.")
        return

    for session in focus_sessions:
        if session["id"] == session_id:
            print(f"\nEditing Focus Session with ID {session_id}:")
            new_task_name = input(f"Enter new task name (current: {session['task_name']}): ")
            new_category = input(f"Enter new category (current: {session['category']}): ")
            new_duration = input(f"Enter new duration in minutes (current: {session['duration']}): ")

            if new_task_name:
                session["task_name"] = new_task_name
            if new_category:
                session["category"] = new_category
            if new_duration:
                try:
                    parsed_duration = int(new_duration)
                    if parsed_duration <= 0:
                        print("Duration must be greater than 0. Keeping the current value.")
                    else:
                        session["duration"] = parsed_duration
                        # Update end time based on the new duration
                        start_time_obj = datetime.datetime.strptime(session["start_time"], "%Y-%m-%d %H:%M:%S")
                        end_time_obj = start_time_obj + datetime.timedelta(minutes=parsed_duration)
                        session["end_time"] = end_time_obj.strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print("Invalid duration. Keeping the current value.")

            print(f"Focus session with ID {session_id} has been updated.")
            return

    print(f"No focus session found with ID: {session_id}. Please check the ID and try again.")

def search_focus_sessions():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    search_term = input("Enter a task name or category to search for: ").strip().lower()
    matching_sessions = [
        session for session in focus_sessions
        if search_term in session["task_name"].lower() or search_term in session["category"].lower()
    ]

    if matching_sessions:
        display_focus_sessions(matching_sessions)
    else:
        print(f"No focus sessions found matching '{search_term}'.")

def focus_session_statistics():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    total_sessions = len(focus_sessions)
    completed_sessions = sum(1 for session in focus_sessions if session["completed"])
    active_sessions = total_sessions - completed_sessions
    total_time_spent = sum(session["duration"] for session in focus_sessions)

    print("\nFocus Session Statistics:")
    print("-" * 30)
    print(f"Total Sessions: {total_sessions}")
    print(f"Completed Sessions: {completed_sessions}")
    print(f"Active Sessions: {active_sessions}")
    print(f"Total Time Spent: {total_time_spent} minutes")
    print("-" * 30)

def filter_focus_sessions():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    print("Filter by:")
    print("1. Category")
    print("2. Completion Status")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        category = input("Enter the category to filter by: ").strip().lower()
        filtered_sessions = [session for session in focus_sessions if session["category"].lower() == category]
    elif choice == "2":
        status = input("Enter 'completed' or 'active' to filter by: ").strip().lower()
        if status == "completed":
            filtered_sessions = [session for session in focus_sessions if session["completed"]]
        elif status == "active":
            filtered_sessions = [session for session in focus_sessions if not session["completed"]]
        else:
            print("Invalid status. Please enter 'completed' or 'active'.")
            return
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
        return

    if filtered_sessions:
        display_focus_sessions(filtered_sessions)
    else:
        print(f"No focus sessions found matching the filter criteria.")

def sort_focus_sessions():
    if not focus_sessions:
        print("No focus sessions found.")
        return

    print("\nSort Focus Sessions By:")
    print("1. Task Name")
    print("2. Category")
    print("3. Duration")
    print("4. Start Time")
    print("5. Longest Duration")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        sorted_sessions = sorted(
            focus_sessions,
            key=lambda session: session["task_name"].lower()
        )

    elif choice == "2":
        sorted_sessions = sorted(
            focus_sessions,
            key=lambda session: session["category"].lower()
        )

    elif choice == "3":
        sorted_sessions = sorted(
            focus_sessions,
            key=lambda session: session["duration"]
        )

    elif choice == "4":
        sorted_sessions = sorted(
            focus_sessions,
            key=lambda session: session["start_time"]
        )

    elif choice == "5":
        sorted_sessions = sorted(
            focus_sessions,
            key=lambda session: session["duration"],
            reverse=True
        )

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return

    display_focus_sessions(sorted_sessions)

def focus_timer():
    if not focus_sessions:
        print("No focus sessions found. Start a session to see it here!")
        return

    display_focus_sessions(focus_sessions)

    try:
        session_id = int(
            input("\nEnter the ID of the focus session to start the timer for: ")
        )
    except ValueError:
        print("Invalid input. Please enter a valid number for the session ID.")
        return

    session = next(
        (session for session in focus_sessions if session["id"] == session_id),
        None
    )

    if not session:
        print(f"No focus session found with ID: {session_id}.")
        return

    if session["completed"]:
        print(
            f"Focus session '{session['task_name']}' "
            f"(ID: {session_id}) is already completed."
        )
        return

    total_seconds = session["duration"] * 60

    print(
        f"\nStarting focus timer for "
        f"'{session['task_name']}'..."
    )
    print("Stay focused. You've got this! 🔥")
    print("Press Ctrl+C to stop the timer.\n")

    try:
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)

            print(
                f"\rTime Remaining: {minutes:02d}:{seconds:02d}",
                end="",
                flush=True
            )

            time.sleep(1)
            total_seconds -= 1

        print("\n\n🎉 Focus session completed!")

        session["completed"] = True

        print(
            f"'{session['task_name']}' "
            f"has been marked as completed."
        )

    except KeyboardInterrupt:
        print("\n\n⏸️ Focus timer stopped.")
        print("The session remains active.")