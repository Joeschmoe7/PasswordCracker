import os
import sqlite3

fileList = []     # Initialize list for files in breach
database = r"c:\test\account_database.db"     # Database location
breachLocation = r"C:\Users\Lou\Downloads\CompilationOfManyBreaches\data\1\\"    # Location of breach file
r = []


def create_database():  # Creates database with Username and Password tables
    import sqlite3
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS Accounts
              (Username text, Password text)
              ''')
    conn.commit()


def list_files(dir):      # Creates a list of files in the breach folder
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

list_files(breachLocation)

username = []     # Initialize list for usernames
password = []     # Initialize list for passwords


def create_lists():     # Populate lists from text files
    conn = sqlite3.connect(database)
    c = conn.cursor()
    print(r)
    for files in r:
        with open(files, encoding = "UTF-8") as x:
            for lines in x:
                left, right = lines.rsplit(":", 1)
                c.execute("INSERT INTO Accounts (Username, Password) VALUES(?,?)", (left, right))
                conn.commit()

    conn.close()

create_database()
list_files(breachLocation)
create_lists()
