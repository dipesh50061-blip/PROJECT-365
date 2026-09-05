import datetime

study_sessions = []

def add_study_session():
    while True:
        subject = input ("Enter the subject: ")
        if subject:
            break
        else:
            print("Subject cannot be empty. Please enter a valid subject.")

    while True:
        topic = input("Enter the topic: ")
        if topic:
            break
        else:
            print("Topic cannot be empty. Please enter a valid topic.")

    while True:
        duration = input("Enter the duration (in minutes): ")
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

    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        if date_str:
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        else:
            print("Date cannot be empty. Please enter a valid date.")

    if not study_sessions:
        new_id = 1
    else:
        new_id = max(session["id"] for session in study_sessions) + 1

    study_session = {
        "id": new_id,
        "subject": subject,
        "topic": topic,
        "duration": duration,
        "date": date.strftime("%Y-%m-%d") # Saved strictly as a string for JSON persistence!
    }

    study_sessions.append(study_session)
    print("Study session added successfully!")


def display_study_sessions(sessions_list):
    print("\nStudy Sessions:")
    print("{:<5} {:<20} {:<30} {:<10} {:<15}".format("ID", "Subject", "Topic", "Duration", "Date"))
    print("-" * 80)

    for session in sessions_list:
        print("{:<5} {:<20} {:<30} {:<10} {:<15}".format(
            session["id"],
            session["subject"],
            session["topic"],
            session["duration"],
            session["date"] # Removed .strftime() since it is now saved as a string
        ))


def view_study_sessions():
    if not study_sessions:
        print("No study sessions found.")
        return
    else:
        display_study_sessions(study_sessions)


def search_study_sessions():
    if not study_sessions:
        print("No study sessions found.")
        return

    search_term = input("Enter the subject or topic to search: ").lower()
    filtered_sessions = [session for session in study_sessions if search_term in session["subject"].lower() or search_term in session["topic"].lower()]

    if not filtered_sessions:
        print("No matching study sessions found.")
    else:
        display_study_sessions(filtered_sessions)


def study_statistics(): # Typo fixed!
    if not study_sessions:
        print("No study sessions found.")
        return

    total_duration = sum(session["duration"] for session in study_sessions)
    average_duration = total_duration / len(study_sessions)

    print("\nStudy Statistics:")
    print(f"Total Study Sessions: {len(study_sessions)}")
    print(f"Total Duration: {total_duration} minutes")
    print(f"Average Duration: {average_duration:.2f} minutes per session")

    # --- New Subject-wise Statistics ---
    print("\nSubject-wise Duration:")
    subject_totals = {}
    
    for session in study_sessions:
        # .title() ensures "sql", "SQL", and "Sql" group together safely
        subj = session["subject"].title() 
        subject_totals[subj] = subject_totals.get(subj, 0) + session["duration"]

    for subj, duration in subject_totals.items():
        print(f"{subj:<11} → {duration} minutes")


def delete_study_session():
    if not study_sessions:
        print("No study sessions found.")
        return

    try:
        session_id = int(input("Enter the ID of the study session to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the ID.")
        return

    for session in study_sessions:
        if session["id"] == session_id:
            study_sessions.remove(session)
            print(f"Study session with ID {session_id} deleted successfully!")
            return

    print(f"No study session found with ID {session_id}.")


def edit_study_session():
    if not study_sessions:
        print("No study sessions found.")
        return

    try:
        session_id = int(input("Enter the ID of the study session to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the ID.")
        return

    for session in study_sessions:
        if session["id"] == session_id:
            print(f"\nEditing Study Session with ID {session_id}:")
            new_subject = input(f"Enter new subject (current: {session['subject']}): ")
            new_topic = input(f"Enter new topic (current: {session['topic']}): ")
            new_duration = input(f"Enter new duration in minutes (current: {session['duration']}): ")
            
            # Removed the .strftime() here since it's already a string!
            new_date_str = input(f"Enter new date (YYYY-MM-DD) (current: {session['date']}): ")

            if new_subject:
                session["subject"] = new_subject
            if new_topic:
                session["topic"] = new_topic
                
            if new_duration:
                try:
                    parsed_duration = int(new_duration)
                    if parsed_duration <= 0:
                        print("Duration must be greater than 0. Keeping the current value.")
                    else:
                        session["duration"] = parsed_duration
                except ValueError:
                    print("Invalid duration. Keeping the current value.")
                    
            if new_date_str:
                try:
                    # Validate it's a real date first, then save it as a string
                    parsed_date = datetime.datetime.strptime(new_date_str, "%Y-%m-%d")
                    session["date"] = parsed_date.strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Keeping the current value.")

            print(f"Study session with ID {session_id} updated successfully!")
            return

    print(f"No study session found with ID {session_id}.")