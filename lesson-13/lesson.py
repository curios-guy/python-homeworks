import sqlite3

connection = sqlite3.connect("test.db")

print(type(connection))

con = sqlite3.connect(":memory:")

query = "Select datetime('now', 'location')"

cursor = con.cursor()
time = cursor.execute(query)
print(time.fetchone())

# with sqlite3.connect("students.db") as connection:
#     cursor = connection.cursor()
#     query = "Create table IF NOT EXISTS Students(fname text, lname text, age int);"
#     data = cursor.execute(query)

# with sqlite3.connect("students.db") as connection:
#     cursor = connection.cursor()
#     query = "Insert into Students Values('Hehe', 'Boi', 69, 190);"
#     data = cursor.execute(query)
#     connection.commit()

# create = """
# Create table if not exists Students(fname str, lname str, age int, height_cm int);
# """

# insert = """
# Insert into Students Values
# ('Hehe', 'Boi', 69, 190),
# ('Hehe', 'Boi', 69, 190),
# ('Hehe', 'Boi', 69, 190),
# ('Hehe', 'Boi', 69, 190),
# ('Hehe', 'Boi', 69, 190),
# ('Hehe', 'Boi', 69, 190);
# """

# delete = """
# Drop table Students
# """

# with sqlite3.connect("students.db") as con:
#     cursor = con.cursor()
#     con.execute(create)
#     con.execute(insert)
#     # con.execute(delete)
#     con.commit()

main_query = """
Create table if not exists Teachers(name str, salary int)
"""

with sqlite3.connect("students.db") as con:
    cursor = con.cursor()
    query = "Select * from Students order by age asc"
    data = cursor.execute(query)
    cursor.execute(main_query)

print(data.fetchone())

# fname = input("First Name: ")
# lname = input("Last Name: ")
# age = int(input("Age: "))
# height = int(input("Height: "))

# values = [(fname, lname, age, height)]

# full_name = input("Name: ")
# salary = int(input("salary: "))

# later_query = f"Insert into Teachers Values('{full_name}', '{salary}')"

# with sqlite3.connect("students.db") as con:
#     cursor = con.cursor()
#     cursor.executemany("Insert into Students Values(?,?,?,?)", values)
#     cursor.execute(later_query)

with sqlite3.connect("students.db") as con:
    cursor = con.cursor()
    cursor.execute("Delete from Students where age = 69")
    print(f"Deleted {cursor.rowcount} record(s)")
    try:
        cursor.execute("ALTER TABLE Students ADD COLUMN email TEXT")
    except sqlite3.OperationalError:
        print("Column 'email' already exists.")
    cursor.execute("UPDATE Students SET email = 'somt@qwe.ewq' WHERE email IS NULL")
    

