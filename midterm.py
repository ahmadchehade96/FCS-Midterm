#https://stackoverflow.com/questions/47202331/python-username-and-password-with-3-attempts
def login():
    attempts = 0
    while attempts < 5:
        username = input("Enter username: ")
        password = input("Enter password (leave empty if none): ")
        if username == "admin" and password == "admin123123":
            admin_menu()
            break
        else:
            print("Incorrect username and/or password.")
            attempts += 1
    else:
        print("Too many failed attempts. Try again later.")
#https://stackoverflow.com/questions/60610009/multiple-choice-menu-python#:~:text=choice%20%3D%20input%20%28%22%22%22%201.%20M
def admin_menu():

    while True:
        print("Admin Menu")
        print("1. Display Statistics")
        print("2. Add an Employee")
        print("3. Display all Employees")
        print("4. Change Employee’s Salary")
        print("5. Remove Employee")
        print("6. Raise Employee’s Salary")
        print("7. Exit")

        choose = input("Enter your choice: ")
        if choose == "1":
            Display_Statistics(employees)
        elif choose == "2":
            Add_Employee(employees)
        elif choose == "3":
            display_all_employees(employees)
        elif choose == "4":
            Change_Salary(employees)
        elif choose == "5":
            Remove_Employee(employees)
        elif choose == "6":
            Raise_Salary(employees)
        elif choose == "7":
            save_employee_data(employees)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")
login()