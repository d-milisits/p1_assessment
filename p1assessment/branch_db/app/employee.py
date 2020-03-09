import sqlite3 

class Employee:
    
    dbpath=""
    tablename="employee"

    def __init__(self,**kwargs):
        self.pk = kwargs.get("pk")
        self.branch_id = kwargs.get("branch_id")
        self.first = kwargs.get("first")
        self.last = kwargs.get("last")
        self.id = kwargs.get("id")
        self.salary = kwargs.get("salary")
    
    def save(self):
        if self.pk is None:
            self.insert()
        else:
            self.update()
    
    def branch(self):
        sql = f"""SELECT * FROM branch JOIN employee
                ON branch.pk=employee.branch_id WHERE employee.pk=?"""

        with sqlite3.connect(self.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sql,(self.pk,))
            row=cursor.fetchone()
            return row
    
    def insert(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()

            sql = f"""INSERT INTO {self.tablename}
                    (branch_id, first, last, id, salary)
                    VALUES(?, ?, ?, ?, ?);"""
            values = (self.branch_id, self.first, self.last, self.id, self.salary)
            sql = cursor.execute(sql, values)
    
    def update(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()

            sql = f"""UPDATE {self.tablename} SET
                    branch_id=?, first=?, last=?, id=?, salary=?
                    WHERE pk=?;"""
            
            values = (self.branch_id, self.first, self.last, self.id, self.salary, self.pk)
            sql = cursor.execute(sql, values)
    
    def delete(self):
        if not self.pk:
            raise KeyError("Not a row in " + self.tablename)
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            sql = f"""DELETE FROM {self.tablename} WHERE pk=?"""
            cursor.execute(sql, (self.pk,))

    @classmethod
    def one_from_pk(cls,pk):
        sql = f"SELECT * FROM {cls.tablename} WHERE pk = ?"

        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sql,(pk,))
            row=cursor.fetchone()
            return cls(**row)

    @classmethod
    def all(cls):
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql = f"SELECT * FROM {cls.tablename};"
            cursor.execute(sql)
            rows=cursor.fetchall()
            return [cls(**row) for row in rows]
        