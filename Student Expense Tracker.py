#Expense Tracker for Students

class Expense:
    def __init__(self,Date,Expense_amt,description):
        self.Date = Date
        self.Expense_amt = Expense_amt
        self.description = description


expenses = []
while True:
    print("1. Add Expense: ")
    print("2. Expense Report: ")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Date = input("Enter date(DD/MM/YYYY): ")
        Expense_amt = float(input("Enter expense amount: "))
        description = input("Enter description: ")
        expense = Expense(Date, Expense_amt, description)
        expenses.append(expense)
    
    elif choice == 2:
        print("========= Expense Report =========")
        for expense in expenses:
            print(expense.Date, expense.Expense_amt, expense.description)

    elif choice == 3:
        total = 0

        for expense in expenses:
            total += expense.Expense_amt
        
        print("Total Expense =", total)
        
    elif choice == 4:
        print("Exiting the program.")
        break


    else:
        print("Invalid choice. Please try again.")
    