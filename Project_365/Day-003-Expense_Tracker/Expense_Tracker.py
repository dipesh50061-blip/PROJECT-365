from datetime import datetime 

expenses = []

def add_expense():

    while True:
        item = input("Enter the name of item: ").strip()

        if item:
            break
        else:
            print("Items cannot be empty. Please type something.")

    while True:
        try:
            amount = int(input("Enter the amount: "))

            if amount <=0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    while True:
        category = input("Enter the category of item: ").strip()

        if category:
            break
        else:
            print("Category cannot be empty. Please type something.")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            new_date = datetime.strptime(date, "%Y-%m-%d")

            if new_date.date() > datetime.today().date():
                print("Date cannot be in the future. Please enter today or a past date.")
                continue

            break

        except ValueError:
            print("Invalid date. Please use a real date in YYYY-MM-DD format.")

    if not expenses:
        new_id = 1

    else:
        new_id = max(e["id"] for e in expenses) +1 

    
    expense = {
        "id":new_id,
        "item":item,
        "amount":amount,
        "category":category,
        "date":new_date.strftime("%Y-%m-%d")
    }

    expenses.append(expense)

    print("Item saved successfully")


def display_expenses(expense):
    print(f'ID        :  {expense["id"]}')
    print(f'Item      :  {expense["item"]}')
    print(f'Amount    :  {expense["amount"]}')
    print(f'Category  :  {expense["category"]}')
    print(f'Date      :  {expense["date"]}')


def view_expenses():
    if not expenses:
        print("No expenses to show")
        return

    for expense in expenses:
        print(f'\nExpenses {expense["id"]}')
        display_expenses(expense)


def delete_expense():
    if not expenses:
        print("No expense to delete")
        return

    while True:
        user_input = input("Enter the id of the item: ").strip()

        if not user_input:
            print("ID cannot be empty. Please enter a number.")
            continue

        try:
            delete_id = int(user_input)
            break

        except ValueError:
            print("Please enter a valid numeric ID.")

    found = False

    for expense in expenses:
        if delete_id == expense["id"]:
            expenses.remove(expense)

            print("Item has been successfully deleted.")
            found = True
            break

    if not found:
        print("Invalid id. No expense found with that ID.")


def search_expenses():
    