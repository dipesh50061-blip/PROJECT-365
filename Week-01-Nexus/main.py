from modelus.task_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task,
    edit_task,
    search_tasks,
    filter_tasks,
    sort_tasks,
    task_statistics,
)

from modelus.study_tracker import (
    add_study_session,
    view_study_sessions,
    search_study_sessions,
    study_statistics,
    delete_study_session,
    edit_study_session,
)

from modelus.goal_manager import (
    add_goal,
    view_goals,
    edit_goal,
    delete_goal,
    complete_goal,
    search_goals,
    filter_goals,
    sort_goals,
    goal_statistics,
)

from modelus.habit_tracker import (
    add_habit,
    view_habits,
    complete_habit,
    delete_habit,
    edit_habit,
    search_habits,
    filter_habits,
    sort_habits,
    habit_statistics,
)

from modelus.focus_center import (
    start_focus_session,
    view_focus_sessions,
    complete_focus_session,
    delete_focus_session,
    edit_focus_session,
    search_focus_sessions,
    filter_focus_sessions,
    sort_focus_sessions,
    focus_session_statistics,
    focus_timer,
)

from modelus.notes_manager import (
    add_note,
    view_notes,
    view_notes_by_id,
    edit_note,
    delete_note,
    search_notes,
    filter_notes,
    sort_notes,
    note_statistics,
)

from modelus.dashboard import dashboard
from modelus.settings import settings_menu


def task_manager_menu():
    while True:
        print("\n" + "=" * 45)
        print("             TASK MANAGER")
        print("=" * 45)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Task Statistics")
        print("10. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            filter_tasks()
        elif choice == "8":
            sort_tasks()
        elif choice == "9":
            task_statistics()
        elif choice == "10":
            print("Returning to NEXUS...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def study_tracker_menu():
    while True:
        print("\n" + "=" * 45)
        print("             STUDY TRACKER")
        print("=" * 45)

        print("1. Add Study Session")
        print("2. View Study Sessions")
        print("3. Search Study Sessions")
        print("4. Study Statistics")
        print("5. Delete Study Session")
        print("6. Edit Study Session")
        print("7. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_study_session()
        elif choice == "2":
            view_study_sessions()
        elif choice == "3":
            search_study_sessions()
        elif choice == "4":
            study_statistics()
        elif choice == "5":
            delete_study_session()
        elif choice == "6":
            edit_study_session()
        elif choice == "7":
            print("Returning to NEXUS...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


def goal_manager_menu():
    while True:
        print("\n" + "=" * 45)
        print("              GOAL MANAGER")
        print("=" * 45)

        print("1. Add Goal")
        print("2. View Goals")
        print("3. Edit Goal")
        print("4. Delete Goal")
        print("5. Complete Goal")
        print("6. Search Goals")
        print("7. Filter Goals")
        print("8. Sort Goals")
        print("9. Goal Statistics")
        print("10. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_goal()
        elif choice == "2":
            view_goals()
        elif choice == "3":
            edit_goal()
        elif choice == "4":
            delete_goal()
        elif choice == "5":
            complete_goal()
        elif choice == "6":
            search_goals()
        elif choice == "7":
            filter_goals()
        elif choice == "8":
            sort_goals()
        elif choice == "9":
            goal_statistics()
        elif choice == "10":
            print("Returning to NEXUS...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def habit_tracker_menu():
    while True:
        print("\n" + "=" * 45)
        print("             HABIT TRACKER")
        print("=" * 45)

        print("1. Add Habit")
        print("2. View Habits")
        print("3. Complete Habit")
        print("4. Delete Habit")
        print("5. Edit Habit")
        print("6. Search Habits")
        print("7. Filter Habits")
        print("8. Sort Habits")
        print("9. Habit Statistics")
        print("10. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            complete_habit()
        elif choice == "4":
            delete_habit()
        elif choice == "5":
            edit_habit()
        elif choice == "6":
            search_habits()
        elif choice == "7":
            filter_habits()
        elif choice == "8":
            sort_habits()
        elif choice == "9":
            habit_statistics()
        elif choice == "10":
            print("Returning to NEXUS...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def focus_center_menu():
    while True:
        print("\n" + "=" * 45)
        print("             FOCUS CENTER")
        print("=" * 45)

        print("1. Start Focus Session")
        print("2. View Focus Sessions")
        print("3. Complete Focus Session")
        print("4. Delete Focus Session")
        print("5. Edit Focus Session")
        print("6. Search Focus Sessions")
        print("7. Filter Focus Sessions")
        print("8. Sort Focus Sessions")
        print("9. Focus Statistics")
        print("10. Focus Timer")
        print("11. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            start_focus_session()
        elif choice == "2":
            view_focus_sessions()
        elif choice == "3":
            complete_focus_session()
        elif choice == "4":
            delete_focus_session()
        elif choice == "5":
            edit_focus_session()
        elif choice == "6":
            search_focus_sessions()
        elif choice == "7":
            filter_focus_sessions()
        elif choice == "8":
            sort_focus_sessions()
        elif choice == "9":
            focus_session_statistics()
        elif choice == "10":
            focus_timer()
        elif choice == "11":
            print("Returning to NEXUS...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")


def notes_manager_menu():
    while True:
        print("\n" + "=" * 45)
        print("             NOTES MANAGER")
        print("=" * 45)

        print("1. Add Note")
        print("2. View Notes")
        print("3. View Note by ID")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Search Notes")
        print("7. Filter Notes")
        print("8. Sort Notes")
        print("9. Note Statistics")
        print("10. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            view_notes_by_id()

        elif choice == "4":
            edit_note()

        elif choice == "5":
            delete_note()

        elif choice == "6":
            search_notes()

        elif choice == "7":
            filter_notes()

        elif choice == "8":
            sort_notes()

        elif choice == "9":
            note_statistics()

        elif choice == "10":
            print("Returning to NEXUS...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("                  N E X U S")
        print("          PERSONAL COMMAND CENTER")
        print("=" * 50)

        print("\n1. Task Manager")
        print("2. Study Tracker")
        print("3. Goal Manager")
        print("4. Habit Tracker")
        print("5. Focus Center")
        print("6. Notes Manager")
        print("7. Dashboard")
        print("8. Settings")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            task_manager_menu()

        elif choice == "2":
            study_tracker_menu()

        elif choice == "3":
            goal_manager_menu()

        elif choice == "4":
            habit_tracker_menu()

        elif choice == "5":
            focus_center_menu()

        elif choice == "6":
            notes_manager_menu()

        elif choice == "7":
            dashboard()

        elif choice == "8":
            settings_menu()

        elif choice == "9":
            print("\nShutting down NEXUS. Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main_menu()