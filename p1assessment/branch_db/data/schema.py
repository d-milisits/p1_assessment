import sqlite3 
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR,"branches.db")

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS branch;")

        sql = """CREATE TABLE branch (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(25),
            state VARCHAR(25),
            zip VARCHAR(10)
        );"""

        cursor.execute(sql)

        cursor.execute("DROP TABLE IF EXISTS employee;")

        sql = """CREATE TABLE employee (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            branch_id INTEGER,
            first VARCHAR(20),
            last VARCHAR(25),
            id VARCHAR(10),
            salary INTEGER,
            FOREIGN KEY(branch_id) REFERENCES branch(pk)
        );"""

        cursor.execute(sql)

if __name__ == "__main__":
    schema()
