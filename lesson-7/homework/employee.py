import json

class Employee():
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary


class EmployeeManager():
    def __init__(self):
        pass
    
    def add_employee(self, employee_id, name, position, salary):
        file_path = "employees.txt"
        employee = Employee(employee_id, name, position, salary)

        
        try:
            with open(file_path, "r") as file:
                employees = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            employees = {}
        
        
        employees[employee.employee_id] = {
            "name" : employee.name,
            "position" : employee.position,
            "salary" : employee.salary 
        }
        
        with open(file_path, "w") as file:
            json.dump(employees, file, indent=4)

        print(f"Employee {employee_id} added successfully.")


    def view_employees(self):
        with open("employees.txt", "r") as file:
            employees = json.load(file)
        
        for keys, values in employees.items():
            print(f"\nEmployee id: {keys}\n\tName: {values["name"]}\n\tPosition: {values["position"]}\n\tSalary: {values["salary"]}")

    def search_employee(self, given_employee_id):
        with open("employees.txt", "r") as file:
            employees = json.load(file)

        for keys, values in employees.items():
            if keys == str(given_employee_id):
                print(f"\nEmployee id: {keys}\n\tName: {values['name']}\n\tPosition: {values['position']}\n\tSalary: {values['salary']}")            
                return
            
        else: print("\nEmployee not found")

    def update_employee(self, given_employee_id, updated_salary, updated_position):
        with open("employees.txt", "r") as file:
            employees = json.load(file)

        for keys, values in employees.items():
            if keys == str(given_employee_id):
                # print(f"\nEmployee id: {keys}\n\tName: {values['name']}\n\tPosition: {values['position']}\n\tSalary: {values['salary']}")
                
                employees[keys] = {
                    "name": values['name'],
                    "position": updated_position,
                    "salary": updated_salary
                }
                
                with open("employees.txt", "w") as file:
                    json.dump(employees, file, indent=4)

                print(f"\nEmployee {keys} has been updated")
                return    
        else: print("\nEmployee not found")

    def delete_employee(self, given_employee_id):
        with open("employees.txt", "r") as file:
            employees = json.load(file)

        for keys, values in employees.items():
            if keys == str(given_employee_id):
                # print(f"\nEmployee id: {keys}\n\tName: {values['name']}\n\tPosition: {values['position']}\n\tSalary: {values['salary']}")
                
                del employees[keys]
                
                with open("employees.txt", "w") as file:
                        json.dump(employees, file, indent=4)

                print(f"\nEmployee {keys} has been deleted")    
                return 
            
        else: print("\nEmployee not found")   

    
manager = EmployeeManager()
# manager.add_employee(213, "Alish", "CTO", 12000)
# manager.add_employee(457, "Alish", "CTO", 12000)
# manager.add_employee(856, "Gosha", "Product Designer", 8000)
# manager.delete_employee(457)

while True:
    ask = int(input( f"\nWelcome to the Employee Records Manager!\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\nYou can select one. Choose wisely: "))
    
    if ask in [1,2,3,4,5,6]:

        # adding new employee
        if ask == 1:
            # gets the initial values for the new employee
            employee_id = int(input("Please provide id: "))
            name = input("Name: ")
            position = input("Position: ")
            salary = int(input("Salary: "))

            try:
                with open("employees.txt", "r") as file:
                    employees = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                employees = {} 

            # checks if given id is unique or not
            if str(employee_id) in employees:
                print("\nEmployee with this ID already exists!")

            else: manager.add_employee(employee_id, name, position, salary)

        # viewing employees
        elif ask == 2:
            manager.view_employees()

        # searching employees
        elif ask == 3:
            employee_id = int(input("Provide employee id: "))
            manager.search_employee(employee_id)

        # update employee
        elif ask == 4:
            employee_id = int(input("Please input employee id: "))
            updated_salary = int(input("Salary: "))
            updated_position = input("Position: ")
            manager.update_employee(employee_id, updated_salary, updated_position)

        # delete employee record
        elif ask == 5:
            employee_id = int(input("Please input employee id: "))
            manager.delete_employee(employee_id)
        # quit
        elif ask == 6:
            print("\nThank you!!!")
            break
    else: print("\nLol not working")


# improve searching employees and other functionalities