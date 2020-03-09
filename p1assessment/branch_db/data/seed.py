import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR,"branches.db")

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        branches = [
            ["Flushing", "NY", "11368"],
            ["Houston", "TX", "77002"]
        ]

        SQL = """INSERT INTO branch (city, state, zip) VALUES
            (?, ?, ?)"""

        for item in branches:
            cur.execute(SQL, (item[0], item[1], item[2]))

        employees = [
            [1, "Walker","Lockett","S0001",45000],
            [1, "Casey", "Coleman", "S0002", 70000],
            [1, "Franklyn", "Kilome", "S0003", 67000],
            [1, "Hecton", "Santiago", "S0004", 100000],
            [2, "Framber", "Valdez", "S0005", 39000],
            [2, "Brad", "Peacock", "S0006", 51000],
            [2, "Reymin", "Guduan", "S0007", 67000],
            [2, "Gerrit", "Cole", "S0008", 55000]
        ]

        SQL2 = """INSERT INTO employee (branch_id, first, last, id, salary) VALUES
             (?, ?, ?, ?, ?)"""

        for item in employees:
            cur.execute(SQL2, (item[0], item[1], item[2], item[3], item[4]))

# if __name__ == "__main__":
#     seed()