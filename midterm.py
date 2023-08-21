#https://stackoverflow.com/questions/47202331/python-username-and-password-with-3-attempts
from datetime import datetime
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

def Display_Statistics(employees):

#https://stackoverflow.com/questions/71030855/print-details-of-an-employee-by-entering-the-name-of-employee-in-python
def Add_Employee(employees):
    def Add_Employee(employees):
        username = input("Enter new employee's username: ")
        gender = input("Enter employee's gender (male/female): ")
        salary = int(input("Enter employee's salary: "))
        emp_id = f"emp{len(employees) + 1:03}"
        timestamp = datetime.today().strftime("%Y%m%d")
        employees[emp_id] = {
            "username": username,
            "emp_id": emp_id,
            "timestamp": timestamp,
            "gender": gender,
            "salary": salary
        }
        print("Employee added successfully.")


def display_all_employees(employees):
# https://crtr4u.com/index.php/2023/06/28/python-example-to-sort-employee-by-multiple-properties/
    sorted_employees = sorted(employees.values(), key=lambda emp: emp["timestamp"], reverse=True)
    for emp in sorted_employees:
        print(f"Employee ID: {emp['emp_id']}")
        print(f"Username: {emp['username']}")
        print(f"Joining Date: {emp['timestamp']}")
        print(f"Gender: {emp['gender']}")
        print(f"Salary: {emp['salary']}")
        print()


def Change_Salary(employees):
    emp_id = input("Enter the Employee ID whose salary you want to change: ")
    new_salary = int(input("Enter the new salary: "))

    if emp_id in employees:
        employees[emp_id]["salary"] = new_salary
        print("Salary changed successfully.")
    else:
        print("Employee not found.")


def Remove_Employee(employees):
def Raise_Salary(employees):
def save_employee_data(employees):
def load_employee_data():


login()