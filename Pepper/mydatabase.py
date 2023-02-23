import sqlite3

def add_to_database(mypredicates,mypredicates_tocheck,mypredicates_stable):

    # Connection to database
    conn = sqlite3.connect("world.db")

    # Cursor of the database
    cursor = conn.cursor()

    # Creation of table in database
    cursor.execute("CREATE TABLE IF NOT EXISTS mypredicates (predicates TEXT)")
    
    cursor.execute("DELETE FROM mypredicates")

    for data in mypredicates:
        # add data in the table
        cursor.execute("""INSERT INTO mypredicates (predicates)
                            VALUES (?)""",(data,))
    
    cursor.execute("CREATE TABLE IF NOT EXISTS mypredicates_tocheck (predicates TEXT)")
    
    cursor.execute("DELETE FROM mypredicates_tocheck")

    for data in mypredicates_tocheck:
        # add data in the table
        cursor.execute("""INSERT INTO mypredicates_tocheck (predicates)
                            VALUES (?)""", (data,))
        
    cursor.execute("CREATE TABLE IF NOT EXISTS mypredicates_stable (predicates TEXT)")
    
    cursor.execute("DELETE FROM mypredicates_stable")

    for data in mypredicates_stable:
        # add data in the table
        cursor.execute("""INSERT INTO mypredicates_stable (predicates)
                            VALUES (?)""", (data,))

    # Commit delle modifiche al database
    conn.commit()

    # Chiusura della connessione
    conn.close()


def read_from_database():
    # Connection to database
    conn = sqlite3.connect("world.db")

    # Cursor of the database
    cursor = conn.cursor()

    # Select data from database
    cursor.execute("SELECT * FROM mypredicates")

    # Fetching data from cursor and storing in a list
    data = cursor.fetchall()
    mypredicates = [row[0] for row in data]

    # Cursor of the database
    cursor = conn.cursor()

    # Select data from database
    cursor.execute("SELECT * FROM mypredicates_tocheck")

    # Fetching data from cursor and storing in a list
    data = cursor.fetchall()
    mypredicates_tocheck = [row[0] for row in data]

    # Cursor of the database
    cursor = conn.cursor()

    # Select data from database
    cursor.execute("SELECT * FROM mypredicates_stable")

    # Fetching data from cursor and storing in a list
    data = cursor.fetchall()
    mypredicates_stable = [row[0] for row in data]

    # Commit delle modifiche al database
    conn.commit()

    # Chiusura della connessione
    conn.close()

    return mypredicates, mypredicates_tocheck, mypredicates_stable


