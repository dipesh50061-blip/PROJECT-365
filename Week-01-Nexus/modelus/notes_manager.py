import datetime

notes = []

def add_note():
    while True:
        title = input("Enter note title: ")
        if title:
            break
        else:
            print("Title cannot be empty. Please try again.")

    while True:
        content = input("Enter note content: ")
        if content:
            break
        else:
            print("Content cannot be empty. Please try again.")

    while True:
        category = input("Enter note category: ")
        if category:
            break
        else:
            print("Category cannot be empty. Please try again.")

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

    while True:
        tags_input = input("Enter tags (comma-separated): ")
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            break
        else:
            print("Tags cannot be empty. Please enter at least one tag.")

    if not notes:
        new_id = 1
    else:
        new_id = max(note["id"] for note in notes) + 1

    note = {
        "id": new_id,
        "title": title,
        "content": content,
        "category": category,
        "date": date.strftime("%Y-%m-%d"),  # Saved strictly as a string for JSON persistence!
        "tags": tags
    }
    notes.append(note)
    print("Note added successfully!")

def display_notes(notes_list):
    if not notes_list:
        print("No notes found.")
        return

    print("\n" + "=" * 60)
    print("                    NOTES")
    print("=" * 60)

    for note in notes_list:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Category: {note['category']}")
        print(f"Date: {note['date']}")
        print(f"Tags: {', '.join(note['tags'])}")
        print(f"Content: {note['content']}")
        print("-" * 60)


def view_notes():
    if not notes:
        print("No notes found.")
        return

    display_notes(notes)

def view_notes_by_id():
    if not notes:
        print("No notes found.")
        return

    while True:
        try:
            note_id = int(input("Enter the ID of the note you want to view: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the note ID.")

    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        display_notes([note])
    else:
        print(f"No note found with ID {note_id}.")

def edit_note():
    if not notes:
        print("No notes found.")
        return

    while True:
        try:
            note_id = int(input("Enter the ID of the note you want to edit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the note ID.")

    note = next((note for note in notes if note["id"] == note_id), None)
    if not note:
        print(f"No note found with ID {note_id}.")
        return

    print("Leave a field empty to keep it unchanged.")

    new_title = input(f"Enter new title (current: {note['title']}): ")
    if new_title:
        note['title'] = new_title

    new_content = input(f"Enter new content (current: {note['content']}): ")
    if new_content:
        note['content'] = new_content

    new_category = input(f"Enter new category (current: {note['category']}): ")
    if new_category:
        note['category'] = new_category

    while True:
        new_date_str = input(f"Enter new date (YYYY-MM-DD) (current: {note['date']}): ")
        if not new_date_str:
            break
        try:
            new_date = datetime.datetime.strptime(new_date_str, "%Y-%m-%d")
            note['date'] = new_date.strftime("%Y-%m-%d")  # Saved strictly as a string for JSON persistence!
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    while True:
        new_tags_input = input(f"Enter new tags (comma-separated) (current: {', '.join(note['tags'])}): ")
        if not new_tags_input:
            break
        tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()]
        if tags:
            note['tags'] = tags
            break
        else:
            print("Tags cannot be empty. Please enter at least one tag.")

    print("Note updated successfully!")

def delete_note():
    if not notes:
        print("No notes found.")
        return

    while True:
        try:
            note_id = int(input("Enter the ID of the note you want to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the note ID.")

    note = next((note for note in notes if note["id"] == note_id), None)
    if not note:
        print(f"No note found with ID {note_id}.")
        return

    notes.remove(note)
    print(f"Note with ID {note_id} deleted successfully!")

def search_notes():
    if not notes:
        print("No notes found.")
        return

    search_term = input("Enter a keyword to search in titles and content: ").lower()
    matching_notes = [note for note in notes if search_term in note["title"].lower() or search_term in note["content"].lower()]

    if matching_notes:
        display_notes(matching_notes)
    else:
        print(f"No notes found containing the keyword '{search_term}'.")

def filter_notes():
    if not notes:
        print("No notes found.")
        return

    print("Filter by:")
    print("1. Category")
    print("2. Date")
    print("3. Tags")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        category = input("Enter the category to filter by: ").lower()
        filtered_notes = [note for note in notes if note["category"].lower() == category]
    elif choice == "2":
        date_str = input("Enter the date (YYYY-MM-DD) to filter by: ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            filtered_notes = [note for note in notes if note["date"] == date]
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return
    elif choice == "3":
        tag = input("Enter the tag to filter by: ").lower()
        filtered_notes = [note for note in notes if tag in [t.lower() for t in note["tags"]]]
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    if filtered_notes:
        display_notes(filtered_notes)
    else:
        print("No notes found matching the filter criteria.")

def sort_notes():
    if not notes:
        print("No notes found.")
        return

    print("Sort by:")
    print("1. Title")
    print("2. Date")
    print("3. Category")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        sorted_notes = sorted(notes, key=lambda x: x["title"].lower())
    elif choice == "2":
        sorted_notes = sorted(notes, key=lambda x: x["date"])
    elif choice == "3":
        sorted_notes = sorted(notes, key=lambda x: x["category"].lower())
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    display_notes(sorted_notes)

def note_statistics():
    if not notes:
        print("No notes found.")
        return

    total_notes = len(notes)
    categories = {}
    for note in notes:
        category = note["category"]
        categories[category] = categories.get(category, 0) + 1

    print("\nNote Statistics:")
    print(f"Total Notes: {total_notes}")
    print("Notes by Category:")
    for category, count in categories.items():
        print(f"{category}: {count}")