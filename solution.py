# Solution
employees = {}

def get_name(employee):
    return employee[1]["name"].lower()

def get_age(employee):
    return employee[1]["age"]

def get_department(employee):
    return employee[1]["department"].lower()

def get_emp_id(employee):
    return employee[0]

def add_employee():
    emp_id = input("Enter Employee ID (e.g., E101): ")
   
    if not emp_id[1:].isdigit():
        print("Error: Employee ID must start with an alphabet followed by numbers (e.g., E101).")
        return
    if emp_id in employees:
        print("Error: Employee ID must be unique.")
        return
   
    name = input("Enter Name: ")
    if not name.replace(" ", ""):
        print("Error: Name should contain only alphabets.")
        return
   
    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Error: Age must be a positive integer.")
            return
    except ValueError:
        print("Error: Age must be a number.")
        return
   
    department = input("Enter Department: ")
   
    employees[emp_id] = {"name": name, "age": age, "department": department}
    print(f"Employee {emp_id} added successfully!")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ").strip().upper()
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee {emp_id} removed successfully!")
    else:
        print("Error: Employee ID not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Error: Employee ID not found.")
        return
   
    print("Leave blank if you don't want to update a field.")
    new_name = input("Enter new Name: ")
    new_age = input("Enter new Age: ")
    new_department = input("Enter new Department: ")

    if new_name:
        if new_name.replace(" ", "").isalpha():
            employees[emp_id]["name"] = new_name
        else:
            print("Error: Name should contain only alphabets.")
   
    if new_age:
        try:
            age = int(new_age)
            if age > 0:
                employees[emp_id]["age"] = age
            else:
                print("Error: Age must be positive.")
        except ValueError:
            print("Error: Invalid age input.")
   
    if new_department:
        employees[emp_id]["department"] = new_department.capitalize()

    print(f"Employee {emp_id} updated successfully!")

def search_employee():
    search_term = input("Search by (1) Employee ID or (2) Name: ")
   
    if search_term == "1":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print(f"Employee Found: {employees[emp_id]}")
        else:
            print("Error: Employee ID not found.")
   
    elif search_term == "2":
        name = input("Enter Name to Search: ").strip().lower()
        found = [f"{emp_id}: {data}" for emp_id, data in employees.items() if data["name"].lower() == name]
       
        if found:
            print("\n".join(found))
        else:
            print("No employees found with that name.")
    else:
        print("Invalid option. Please enter 1 or 2.")

def sort_employees():
    criteria = input("Sort by (1) Name, (2) Age, (3) Department, (4) Employee ID: ")
   
    if criteria == "1":
        sorted_employees = sorted(employees.items(), key=get_name)
    elif criteria == "2":
        sorted_employees = sorted(employees.items(), key=get_age)
    elif criteria == "3":
        sorted_employees = sorted(employees.items(), key=get_department)
    elif criteria == "4":
        sorted_employees = sorted(employees.items(), key=get_emp_id)
    else:
        print("Invalid option.")
        return
   
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
       
        choice = input("Enter your choice: ")
       
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")


