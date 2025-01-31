import sqlite3

populate = [
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29)
]

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    cursor.execute("DROP table IF EXISTS Roster")
    cursor.execute("CREATE table IF NOT EXISTS Roster(name text, species text, age int)")
    
    cursor.executemany("INSERT into Roster Values(?,?,?)", populate)
    con.commit()

    cursor.execute("UPDATE Roster SET name = 'Ezri Dax' WHERE name = 'Jadzia Dax'")
    data = cursor.execute("SELECT * from Roster WHERE species = 'Bajoran'")
    cursor.execute("DELETE from Roster where age > 100")

    # checks if column exists or not. will run smoothly even though t exists
    try: 
        cursor.execute("ALTER table Roster ADD column rank text")
    except sqlite3.OperationalError:
        pass

    cursor.execute("UPDATE Roster SET rank = 'Captain' WHERE species  = 'Human'")
    cursor.execute("UPDATE Roster SET rank = 'Major' WHERE name = 'Kira Nerys'")
    data_age = cursor.execute("SELECT * from Roster order by age desc")
    
    print("Created!!!")
    print(data.fetchall())
    print(data_age.fetchall())