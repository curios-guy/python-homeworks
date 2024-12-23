# main menu
def main_handler():
    while True:
        print(f"\nPlease choose one from following:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = int(input("Choose: "))
        
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            break
        else: print("Please input options 1-6")

# adds employees
def add_employee():
    with open("employees.txt", "a") as file:
        empId = (input("Input employee ID: "))
        name = input("Input name: ")
        position = input("Input position: ")
        salary = int(input("Input salary: "))
        file.write(f"{{{empId}, {name}, {position}, {salary}}}\n")
        file.close()
        print(f"\nEmployee added successfully")

# view employees
def view_employee():
    with open("employees.txt", "r") as file:
        records = file.readlines()
        # records = records.strip()
        print(records)

        if records != []:
            print(f"\nEmployee records")
            for record in records:
                print(f"\n{record.strip()}")
                # for r in record:
                #     print(r)
        else: print(f"\nRecords are not found!")

# searchs for employees
def search_employee():
    empId = (input("Input employee ID: "))
    with open("employees.txt" , "r") as file: 
        for record in file:
            print(record)
            print("(" + f"'{empId}'" + ",")
            if record.startswith(f"{empId}"):
                print(f"\nEmployee found: {record.strip()}")
                return
        print(f"\nEmployee not found")

# updates employees
def update_employee():
    empId = input("INput employee ID: ")
    with open("employees.txt", "r") as file:
        # print(file)
        for record in file:
            print(record)
            if record.startswith(f"{empId},"):
                print("Found")

# deletes employees
def delete_employee():
    empId = input("Input employee ID: ")
    with open("employees.txt", "r") as file:
        info = file
        for record in info:
            if record.startswith(f"{empId}"):
                return record.strip()

# CALL-TO-ACTION handler
main_handler()