import json
import os

from study_manager import (
    add_study_session,
    view_study_sessions,
    search_study_sessions,
    study_statistics,
    delete_study_session,
    edit_study_session,
    set_study_sessions
)


FILE_NAME = "study_sessions.json"


# ==============================
# LOAD STUDY SESSIONS
# ==============================

def load_sessions():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, IOError):
        print("Could not load saved sessions.")
        return []


# ==============================
# SAVE STUDY SESSIONS
# ==============================

def save_sessions(sessions):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(sessions, file, indent=4)

    except IOError:
        print("Error saving study sessions.")


# ==============================
# MAIN MENU
# ==============================

def main():

    sessions = load_sessions()

    # Send loaded sessions to study_manager.py
    set_study_sessions(sessions)

    while True:

        print("\n")
        print("=" * 40)
        print("          STUDY TRACKER")
        print("=" * 40)

        print("1. Add Study Session")
        print("2. View Study Sessions")
        print("3. Search Study Sessions")
        print("4. Study Statistics")
        print("5. Delete Study Session")
        print("6. Edit Study Session")
        print("7. Exit")

        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_study_session()
            save_sessions(sessions)

        elif choice == "2":

            view_study_sessions()

        elif choice == "3":

            search_study_sessions()

        elif choice == "4":

            study_statistics()

        elif choice == "5":

            delete_study_session()
            save_sessions(sessions)

        elif choice == "6":

            edit_study_session()
            save_sessions(sessions)

        elif choice == "7":

            save_sessions(sessions)

            print("Study Tracker closed. Goodbye! 👋")
            break

        else:

            print(
                "Invalid choice. "
                "Please select a number from 1-7."
            )


if __name__ == "__main__":
    main()