
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

def admin_menu():
    employees = load_employee_data()
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
    male_count = sum(1 for emp in employees.values() if emp["gender"] == "male")
    female_count = len(employees) - male_count
    print(f"Number of male employees: {male_count}")
    print(f"Number of female employees: {female_count}")
#https://stackoverflow.com/questions/71030855/print-details-of-an-employee-by-entering-the-name-of-employee-in-python
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
    emp_id = input("Enter the Employee ID of the employee you want to remove: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")

def Raise_Salary(employees):
    emp_id = input("Enter the Employee ID of the employee whose salary you want to raise: ")
    raise_percentage = float(input("Enter the raise percentage (e.g., 1.05 for 5% raise): "))

    if emp_id in employees:
        employees[emp_id]["salary"] *= raise_percentage
        print("Salary raised successfully.")
    else:
        print("Employee not found.")

def save_employee_data(employees):
    try:
        with open("employees.txt", "w") as file:
            for emp_id, emp_info in employees.items():
                line = f"{emp_info['emp_id']}, {emp_id}, {emp_info['timestamp']}, {emp_info['gender']}, {emp_info['salary']}\n"
                file.write(line)
        print("Employee data saved successfully.")
    except Exception as e:
        print("Error saving employee data:", e)

def load_employee_data():
    employees = {}
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, username, timestamp, gender, salary = line.strip().split(", ")
                employees[emp_id] = {
                    "username": username,
                    "emp_id": emp_id,
                    "timestamp": timestamp,
                    "gender": gender,
                    "salary": int(salary)
                }
        print("Employee data loaded successfully.")
    except FileNotFoundError:
        print("No employee data found.")
    except Exception as e:
        print("Error loading employee data:", e)
    return employees

def user_menu(username, employee_data):
    employee_info = employee_data.get(username)
    if employee_info:
        print(f"Hi Mr. {employee_info['emp_id']}" if employee_info['gender'] == 'male' else f"Hi Ms. {employee_info['emp_id']}")
        while True:
            print("User Menu")
            print("1. Check my Salary")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your salary is: {employee_info['salary']}")
            elif choice == "2":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select again.")
    else:
        print("Employee data not found.")
login()