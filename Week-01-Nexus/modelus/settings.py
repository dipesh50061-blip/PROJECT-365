settings = {
    "username": "User",
    "date_format": "YYYY-MM-DD",
    "default_study_duration": 60,
    "default_focus_duration": 25
}


def view_settings():
    print("\n" + "=" * 45)
    print("                 SETTINGS")
    print("=" * 45)

    print(f"Username                : {settings['username']}")
    print(f"Date Format             : {settings['date_format']}")
    print(
        f"Default Study Duration  : "
        f"{settings['default_study_duration']} minutes"
    )
    print(
        f"Default Focus Duration  : "
        f"{settings['default_focus_duration']} minutes"
    )


def change_username():
    while True:
        username = input("Enter your new username: ").strip()

        if username:
            settings["username"] = username
            print("Username updated successfully!")
            return

        print("Username cannot be empty. Please try again.")


def change_date_format():
    print("\nAvailable Date Formats:")
    print("1. YYYY-MM-DD")
    print("2. DD-MM-YYYY")
    print("3. MM-DD-YYYY")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        settings["date_format"] = "YYYY-MM-DD"

    elif choice == "2":
        settings["date_format"] = "DD-MM-YYYY"

    elif choice == "3":
        settings["date_format"] = "MM-DD-YYYY"

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    print("Date format updated successfully!")


def set_default_study_duration():
    while True:
        duration = input(
            "Enter default study duration in minutes: "
        ).strip()

        try:
            duration = int(duration)

            if duration <= 0:
                print("Duration must be greater than 0.")
                continue

            settings["default_study_duration"] = duration
            print("Default study duration updated successfully!")
            return

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def set_default_focus_duration():
    while True:
        duration = input(
            "Enter default focus duration in minutes: "
        ).strip()

        try:
            duration = int(duration)

            if duration <= 0:
                print("Duration must be greater than 0.")
                continue

            settings["default_focus_duration"] = duration
            print("Default focus duration updated successfully!")
            return

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def reset_settings():
    print("\nReset Settings?")
    print("This will restore all settings to their default values.")

    confirmation = input(
        "Type 'yes' to confirm: "
    ).strip().lower()

    if confirmation == "yes":
        settings["username"] = "User"
        settings["date_format"] = "YYYY-MM-DD"
        settings["default_study_duration"] = 60
        settings["default_focus_duration"] = 25

        print("Settings reset successfully!")

    else:
        print("Reset cancelled.")


def settings_menu():
    while True:
        print("\n" + "=" * 45)
        print("                 SETTINGS")
        print("=" * 45)

        print("1. View Settings")
        print("2. Change Username")
        print("3. Change Date Format")
        print("4. Set Default Study Duration")
        print("5. Set Default Focus Duration")
        print("6. Reset Settings")
        print("7. Back to NEXUS")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_settings()

        elif choice == "2":
            change_username()

        elif choice == "3":
            change_date_format()

        elif choice == "4":
            set_default_study_duration()

        elif choice == "5":
            set_default_focus_duration()

        elif choice == "6":
            reset_settings()

        elif choice == "7":
            print("Returning to NEXUS...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")