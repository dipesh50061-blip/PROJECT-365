import datetime

goals = []

def add_goal():
    while True:
        title = input("Enter the goal title: ")
        if title:
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")

    while True:
        description = input("Enter the goal description: ")
        if description:
            break
        else:
            print("Description cannot be empty. Please enter a valid description.")

    while True:
        category = input("Enter the goal category: ")
        if category:
            break
        else:
            print("Category cannot be empty. Please enter a valid category.")

    while True:
        target_date_str = input("Enter the target date (YYYY-MM-DD): ")
        if target_date_str:
            try:
                target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        else:
            print("Target date cannot be empty. Please enter a valid date.")

    while True:
        priority = input("Enter the goal priority (High, Medium, Low): ")
        if priority.lower() in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority. Please enter High, Medium, or Low.")

    if not goals:
        new_id = 1
    else:
        new_id = max(goal["id"] for goal in goals) + 1

    # FIXED: Added missing comma, priority, and completed status!
    goal = {
        "id": new_id,
        "title": title,
        "description": description,
        "category": category,
        "target_date": target_date.strftime("%Y-%m-%d"), 
        "priority": priority.title(),
        "completed": False
    }

    goals.append(goal)
    print("Goal added successfully!")

def display_goals(goals_list): 
    if not goals_list:
        print("No goals found.")
        return

    print("\n" + "=" * 45)
    print("            GOAL MANAGER")
    print("=" * 45)

    for goal in goals_list:
        # Added Priority and Status to the display so you can actually see them!
        status = "Completed" if goal["completed"] else "Pending"
        
        print(f"ID: {goal['id']}")
        print(f"Title: {goal['title']}")
        print(f"Description: {goal['description']}")
        print(f"Category: {goal['category']}")
        print(f"Priority: {goal['priority']}")
        print(f"Target Date: {goal['target_date']}")
        print(f"Status: {status}")
        print("-" * 45)

def view_goals():
    if not goals:
        print("No goals found.")
        return
    else:
        display_goals(goals)

def edit_goal():
    if not goals:
        print("No goals found.")
        return

    try:
        goal_id = int(input("Enter the ID of the goal you want to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
        return

    goal_to_edit = next((goal for goal in goals if goal["id"] == goal_id), None)

    if not goal_to_edit:
        print(f"No goal found with ID {goal_id}.")
        return

    print("\nLeave a field empty to keep the current value.")

    new_title = input(f"Enter new title (current: {goal_to_edit['title']}): ")
    if new_title:
        goal_to_edit["title"] = new_title

    new_description = input(f"Enter new description (current: {goal_to_edit['description']}): ")
    if new_description:
        goal_to_edit["description"] = new_description

    new_category = input(f"Enter new category (current: {goal_to_edit['category']}): ")
    if new_category:
        goal_to_edit["category"] = new_category

    # FIXED: Added the priority editor block
    while True:
        new_priority = input(f"Enter new priority (High, Medium, Low) (current: {goal_to_edit['priority']}): ")
        
        if not new_priority: # If they just press Enter, break and keep the old one
            break
            
        if new_priority.lower() in ["high", "medium", "low"]:
            goal_to_edit["priority"] = new_priority.title()
            break
        else:
            print("Invalid priority. Please enter High, Medium, or Low.")

    while True:
        new_target_date_str = input(f"Enter new target date (YYYY-MM-DD) (current: {goal_to_edit['target_date']}): ")
        if not new_target_date_str:
            break
        try:
            new_target_date = datetime.datetime.strptime(new_target_date_str, "%Y-%m-%d")
            goal_to_edit["target_date"] = new_target_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    print("Goal updated successfully!") 

def delete_goal():
    if not goals:
        print("No goals found.")
        return

    try:
        goal_id = int(input("Enter the ID of the goal you want to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
        return

    goal_to_delete = next((goal for goal in goals if goal["id"] == goal_id), None)

    if not goal_to_delete:
        print(f"No goal found with ID {goal_id}.")
        return

    goals.remove(goal_to_delete)
    print(f"Goal with ID {goal_id} deleted successfully!")

def complete_goal():
    if not goals:
        print("No goals found.")
        return

    try:
        goal_id = int(input("Enter the ID of the goal you want to mark as completed: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
        return

    goal_to_complete = next((goal for goal in goals if goal["id"] == goal_id), None)

    if not goal_to_complete:
        print(f"No goal found with ID {goal_id}.")
        return

    goal_to_complete["completed"] = True
    print(f"Goal with ID {goal_id} marked as completed!")

def search_goals():
    if not goals:
        print("No goals found.")
        return

    search_term = input("Enter a keyword to search for in goal titles and descriptions: ").lower()
    matching_goals = [goal for goal in goals if search_term in goal["title"].lower() or search_term in goal["description"].lower()]

    if not matching_goals:
        print(f"No goals found matching the keyword '{search_term}'.")
    else:
        display_goals(matching_goals)

def filter_goals():
    if not goals:
        print("No goals found.")
        return

    print("Filter by:")
    print("1. Category")
    print("2. Target Date")
    print("3. Completion Status")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        category = input("Enter the category to filter by: ").lower()
        filtered_goals = [goal for goal in goals if goal["category"].lower() == category]
    elif choice == "2":
        target_date_str = input("Enter the target date to filter by (YYYY-MM-DD): ")
        try:
            target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            filtered_goals = [goal for goal in goals if goal["target_date"] == target_date]
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return
    elif choice == "3":
        status = input("Enter 'completed' or 'not completed' to filter by: ").lower()
        if status == "completed":
            filtered_goals = [goal for goal in goals if goal["completed"]]
        elif status == "not completed":
            filtered_goals = [goal for goal in goals if not goal["completed"]]
        else:
            print("Invalid status. Please enter 'completed' or 'not completed'.")
            return
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    if not filtered_goals:
        print(f"No goals found matching the filter criteria.")
    else:
        display_goals(filtered_goals)

def sort_goals():
    if not goals:
        print("No goals found.")
        return

    print("Sort by:")
    print("1. Title")
    print("2. Target Date")
    print("3. Priority")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        sorted_goals = sorted(goals, key=lambda x: x["title"].lower())
    elif choice == "2":
        sorted_goals = sorted(goals, key=lambda x: x["target_date"]) # Already formatted as YYYY-MM-DD, sorts perfectly as string!
    elif choice == "3":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        # Safely looks up the priority. If it's somehow missing, it defaults to 4 (bottom of list)
        sorted_goals = sorted(goals, key=lambda x: priority_order.get(x["priority"], 4))
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    display_goals(sorted_goals)

def goal_statistics():
    if not goals:
        print("No goals found.")
        return

    total_goals = len(goals)
    completed_goals = len([goal for goal in goals if goal["completed"]])
    pending_goals = total_goals - completed_goals

    # FIXED: Added the completion rate calculation!
    completion_rate = (completed_goals / total_goals) * 100

    print("\nGoal Statistics:")
    print(f"Total Goals: {total_goals}")
    print(f"Completed Goals: {completed_goals}")
    print(f"Pending Goals: {pending_goals}")
    print(f"Completion Rate: {completion_rate:.2f}%")

def validation():
    if not goals:
        print("No goals found.")
        return

    print("\nGoal Validation:")
    for goal in goals:
        if goal["completed"]:
            print(f"Goal ID {goal['id']} - '{goal['title']}' is completed.")
        else:
            print(f"Goal ID {goal['id']} - '{goal['title']}' is pending.")