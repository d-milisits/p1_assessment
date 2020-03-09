import sqlite3 

class Branch:

    dbpath=""
    tablename="branch"

    def __init__(self,**kwargs):
        self.pk = kwargs.get("pk")
        self.city = kwargs.get("city")
        self.state = kwargs.get("state")
        self.zip = kwargs.get("zip")
    
    def save(self):
        if self.pk is None:
            self.insert()
        else:
            self.update()
    
    def insert(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()

            sql = f"""INSERT INTO {self.tablename}
                    (city, state, zip)
                    VALUES(?, ?, ?);"""
            values = (self.city, self.state, self.zip)
            sql = cursor.execute(sql, values)
    
    def update(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()

            sql = f"""UPDATE {self.tablename} SET
                    city=?, state=?, zip=?
                    WHERE pk=?;"""
            
            values = (self.city, self.state, self.zip, self.pk)
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