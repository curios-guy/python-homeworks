import sqlite3

books = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    # delete data if exists
    cursor.execute("DROP table IF EXISTS Library")

    # create data table
    cursor.execute("CREATE table IF NOT EXISTS Library(title text, author text, year_published int, genre text)")
    
    # new data on database
    cursor.executemany("INSERT into Library Values(?, ?, ?, ?)", books)

    # update data
    cursor.execute("UPDATE Library SET year_published = 1950 WHERE title = '1984'")

    # select and display data
    data = cursor.execute("SELECT * from Library where genre = 'Dystopian'")
    for row in data.fetchall():
        print(row)

    # remove data
    cursor.execute("DELETE from Library where year_published < 1950")

    # adding new column(bonus)
    try: 
        cursor.execute("ALTER table Library ADD column rating text")
    except sqlite3.OperationalError:
        pass

    # update values
    cursor.execute("UPDATE Library SET rating = 4.8 WHERE title = 'To Kill a Mockingbird'")
    cursor.execute("UPDATE Library SET rating = 4.7 WHERE title = '1984'")

    # sort data
    data_year = cursor.execute("SELECT * from Library order by year_published asc")
    for year in data_year.fetchall():
        print(year)