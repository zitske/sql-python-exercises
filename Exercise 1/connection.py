## Conectando com o database
import sqlite3

def db():
    try:
        db = sqlite3.connect('Northwind.db')
        print('connection succesful')
        return db
    except:
        print('connection error')
        return None