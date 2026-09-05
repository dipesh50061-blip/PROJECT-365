import datetime

habits = []

def add_habit():
    while True:
        name = input("Enter the habit name: ").strip()
        if name:
            break
        print("Habit name cannot be empty. Please enter a valid name.")

    while True:
        description = input("Enter the habit description: ").strip()
        if description:
            break
        print("Description cannot be empty. Please enter a valid description.")

    while True:
        frequency = input("Enter the habit frequency (Daily, Weekly, Monthly): ").strip()
        if frequency.lower() in ["daily", "weekly", "monthly"]:
            break
        print("Invalid frequency. Please enter Daily, Weekly, or Monthly.")

    while True:
        start_date_str = input("Enter the start date (YYYY-MM-DD): ").strip()
        if start_date_str:
            try:
                start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        else:
            print("Start date cannot be empty. Please enter a valid date.")

    if not habits:
        new_id = 1
    else:
        new_id = max(habit["id"] for habit in habits) + 1

    # ARCHITECTURAL UPGRADE: Using completed_dates list instead of a boolean
    habit = {
        "id": new_id,
        "name": name,
        "description": description,
        "frequency": frequency.title(),
        "start_date": start_date.strftime("%Y-%m-%d"),
        "completed_dates": []
    }

    habits.append(habit)
    print(f"\nHabit '{name}' (ID: {new_id}) added successfully!")


def calculate_streak(completed_dates):
    """Calculates the current streak of consecutive days completed."""
    if not completed_dates:
        return 0

    today = datetime.date.today()
    streak = 0
    check_date = today

    # If not completed today, check if streak is alive from yesterday
    today_str = today.strftime("%Y-%m-%d")
    yesterday_str = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    if today_str not in completed_dates and yesterday_str not in completed_dates:
        return 0

    if today_str not in completed_dates:
        check_date = today - datetime.timedelta(days=1)

    while check_date.strftime("%Y-%m-%d") in completed_dates:
        streak += 1
        check_date -= datetime.timedelta(days=1)

    return streak


def display_habits(habits_list):
    if not habits_list:
        print("No habits found.")
        return

    today_str = datetime.date.today().strftime("%Y-%m-%d")

    print("\nYour Habits:")
    print("-" * 105)
    print(f"{'ID':<4} {'Name':<20} {'Frequency':<10} {'Today':<8} {'Streak':<10} {'Total Done':<12} {'Start Date':<12}")
    print("-" * 105)

    for habit in habits_list:
        completed_today = "Yes" if today_str in habit["completed_dates"] else "No"
        streak = calculate_streak(habit["completed_dates"])
        total_completions = len(habit["completed_dates"])

        print(f"{habit['id']:<4} {habit['name']:<20} {habit['frequency']:<10} {completed_today:<8} {f'{streak} days':<10} {total_completions:<12} {habit['start_date']:<12}")
    print("-" * 105)


def view_habits():
    if not habits:
        print("No habits found.")
        return
    display_habits(habits)


def complete_habit():
    if not habits:
        print("No habits found.")
        return

    display_habits(habits)

    while True:
        try:
            habit_id = int(input("\nEnter the ID of the habit to mark complete for today: "))
            habit = next((h for h in habits if h["id"] == habit_id), None)
            if habit:
                break
            print("Habit not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    today_str = datetime.date.today().strftime("%Y-%m-%d")

    # Prevent duplicate logging for the same day
    if today_str in habit["completed_dates"]:
        print(f"\nHabit '{habit['name']}' has already been marked complete for today ({today_str})!")
    else:
        habit["completed_dates"].append(today_str)
        streak = calculate_streak(habit["completed_dates"])
        print(f"\nSuccess! Marked '{habit['name']}' complete for today ({today_str}).")
        print(f"Current Streak: {streak} day(s)!")


def edit_habit():
    if not habits:
        print("No habits found.")
        return

    display_habits(habits)

    while True:
        try:
            habit_id = int(input("\nEnter the ID of the habit you want to edit: "))
            habit = next((h for h in habits if h["id"] == habit_id), None)
            if habit:
                break
            print("Habit not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nLeave a field empty to keep the current value.")
    new_name = input(f"Enter new name (current: {habit['name']}): ").strip() or habit['name']
    new_description = input(f"Enter new description (current: {habit['description']}): ").strip() or habit['description']
    
    new_freq_input = input(f"Enter new frequency (Daily, Weekly, Monthly) (current: {habit['frequency']}): ").strip()
    if new_freq_input.lower() in ["daily", "weekly", "monthly"]:
        new_frequency = new_freq_input.title()
    else:
        new_frequency = habit['frequency']

    while True:
        new_start_date_str = input(f"Enter new start date (YYYY-MM-DD) (current: {habit['start_date']}): ").strip()
        if not new_start_date_str:
            new_start_date = habit['start_date']
            break
        try:
            datetime.datetime.strptime(new_start_date_str, "%Y-%m-%d")
            new_start_date = new_start_date_str
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")

    habit["name"] = new_name
    habit["description"] = new_description
    habit["frequency"] = new_frequency
    habit["start_date"] = new_start_date

    print("\nHabit updated successfully!")


def delete_habit():
    if not habits:
        print("No habits found.")
        return

    display_habits(habits)

    while True:
        try:
            habit_id = int(input("\nEnter the ID of the habit you want to delete: "))
            habit = next((h for h in habits if h["id"] == habit_id), None)
            if habit:
                break
            print("Habit not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    habits.remove(habit)
    print(f"\nHabit '{habit['name']}' (ID: {habit_id}) deleted successfully!")


def search_habits():
    if not habits:
        print("No habits found.")
        return

    search_term = input("Enter the habit name or description to search for: ").strip().lower()
    matching_habits = [h for h in habits if search_term in h["name"].lower() or search_term in h["description"].lower()]

    if matching_habits:
        display_habits(matching_habits)
    else:
        print(f"No matching habits found for '{search_term}'.")


def filter_habits():
    if not habits:
        print("No habits found.")
        return

    print("\nFilter by:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Completed Today")
    print("5. Pending Today")

    choice = input("Enter your choice (1-5): ").strip()
    today_str = datetime.date.today().strftime("%Y-%m-%d")

    if choice == "1":
        filtered = [h for h in habits if h["frequency"] == "Daily"]
    elif choice == "2":
        filtered = [h for h in habits if h["frequency"] == "Weekly"]
    elif choice == "3":
        filtered = [h for h in habits if h["frequency"] == "Monthly"]
    elif choice == "4":
        filtered = [h for h in habits if today_str in h["completed_dates"]]
    elif choice == "5":
        filtered = [h for h in habits if today_str not in h["completed_dates"]]
    else:
        print("Invalid choice.")
        return

    display_habits(filtered)


def sort_habits():
    if not habits:
        print("No habits found.")
        return

    print("\nSort habits by:")
    print("1. Name (A → Z)")
    print("2. Frequency")
    print("3. Start Date (Earliest First)")
    print("4. Highest Total Completions")
    print("5. Highest Current Streak")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        sorted_habits = sorted(habits, key=lambda x: x["name"].lower())
    elif choice == "2":
        sorted_habits = sorted(habits, key=lambda x: x["frequency"])
    elif choice == "3":
        sorted_habits = sorted(habits, key=lambda x: x["start_date"])
    elif choice == "4":
        sorted_habits = sorted(habits, key=lambda x: len(x["completed_dates"]), reverse=True)
    elif choice == "5":
        sorted_habits = sorted(habits, key=lambda x: calculate_streak(x["completed_dates"]), reverse=True)
    else:
        print("Invalid choice.")
        return

    display_habits(sorted_habits)


def habit_statistics():
    if not habits:
        print("No habits found.")
        return

    today_str = datetime.date.today().strftime("%Y-%m-%d")
    total_habits = len(habits)
    completed_today_count = sum(1 for h in habits if today_str in h["completed_dates"])
    pending_today_count = total_habits - completed_today_count
    daily_rate = (completed_today_count / total_habits) * 100 if total_habits > 0 else 0.0

    print("\n" + "=" * 40)
    print("          HABIT STATISTICS")
    print("=" * 40)
    print(f"Total Tracked Habits  : {total_habits}")
    print(f"Completed Today       : {completed_today_count}")
    print(f"Pending Today         : {pending_today_count}")
    print(f"Today's Completion    : {daily_rate:.1f}%\n")

    print("Individual Breakdown:")
    for h in habits:
        streak = calculate_streak(h["completed_dates"])
        total_done = len(h["completed_dates"])
        print(f" • {h['name']:<18} | Streak: {streak}d | Total Logged: {total_done} times")
    print("=" * 40)


