import os
import pandas as pd
import sqlite3

r = []     #Initialize list for files in breach
database = r"c:\test\account_database"     #Database location
breachLocation = r"C:\Users\Lou\Downloads\CompilationOfManyBreaches\data\0\""    #Location of breach file

def createDatabase():  #Creates database with Username and Password tables
    import sqlite3
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS Accounts
              (Username TEXT, Password TEXT)
              ''')
    conn.commit()

def list_files(dir):      #Creates a list of files in the breach folder
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

username = []     #Initialize list for usernames
password = []     #Initialize list for passwords

def createLists():     #Populate lists from text files
    for files in r:
        with open (files, encoding = "UTF-8") as x:
             for lines in x:
                 left, right= lines.rsplit(":", 1)
                 username.append(left)
                 password.append(right)

        username.clear()
        password.clear()

createDatabase()
list_files(breachLocation)
createLists()
