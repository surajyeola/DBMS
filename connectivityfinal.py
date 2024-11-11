import mysql.connector
from mysql.connector import Error

def connect_to_db():
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your MySQL username
            password='your_password', # Replace with your MySQL password
            database='your_database'  # Replace with your database name
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def insert_employee(connection):
    """Insert a new employee record into the employee table."""
    empid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    query = "INSERT INTO employee (empid, name, salary) VALUES (%s, %s, %s)"
    data = (empid, name, salary)
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Employee inserted successfully!")
    except Error as e:
        print(f"Failed to insert record: {e}")
    finally:
        cursor.close()


def update_employee(connection):
    """Update an employee's salary by employee ID."""
    empid = int(input("Enter Employee ID to update: "))
    salary = float(input("Enter new Salary: "))

    query = "UPDATE employee SET salary = %s WHERE empid = %s"
    data = (salary, empid)

    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Employee salary updated successfully!")
    except Error as e:
        print(f"Failed to update record: {e}")
    finally:
        cursor.close()


def delete_employee(connection):
    """Delete an employee record by employee ID."""
    empid = int(input("Enter Employee ID to delete: "))

    query = "DELETE FROM employee WHERE empid = %s"
    data = (empid,)

    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Employee deleted successfully!")
    except Error as e:
        print(f"Failed to delete record: {e}")
    finally:
        cursor.close()


def display_all_employees(connection):
    """Display all employee records."""
    query = "SELECT * FROM employee"
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        
        if records:
            for empid, name, salary in records:
                print(f"ID: {empid}, Name: {name}, Salary: {salary}")
        else:
            print("No records found.")
    except Error as e:
        print(f"Failed to fetch records: {e}")
    finally:
        cursor.close()


def display_high_salary_employees(connection):
    """Display employees with salary greater than 50000."""
    query = "SELECT * FROM employee WHERE salary > 50000"
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        
        if records:
            for empid, name, salary in records:
                print(f"ID: {empid}, Name: {name}, Salary: {salary}")
        else:
            print("No employees found with salary > 50000.")
    except Error as e:
        print(f"Failed to fetch records: {e}")
    finally:
        cursor.close()


def display_employee(connection):
    """Display a particular employee's record by employee ID."""
    empid = int(input("Enter Employee ID to display: "))
    query = "SELECT * FROM employee WHERE empid = %s"
    data = (empid,)
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        record = cursor.fetchone()
        if record:
            print(f"ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
        else:
            print("Employee not found.")
    except Error as e:
        print(f"Failed to fetch record: {e}")
    finally:
        cursor.close()


def menu():
    """Main menu to navigate the employee management operations."""
    connection = connect_to_db()
    if connection is None:
        print("Error: Could not connect to the database.")
        return
    
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Insert Employee")
        print("2. Update Employee Salary")
        print("3. Delete Employee")
        print("4. Display All Employees")
        print("5. Display Employees with Salary > 50000")
        print("6. Display Specific Employee")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_employee(connection)
        elif choice == '2':
            update_employee(connection)
        elif choice == '3':
            delete_employee(connection)
        elif choice == '4':
            display_all_employees(connection)
        elif choice == '5':
            display_high_salary_employees(connection)
        elif choice == '6':
            display_employee(connection)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
    
    connection.close()


if _name_ == "_main_":
    menu()
