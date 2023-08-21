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
login()