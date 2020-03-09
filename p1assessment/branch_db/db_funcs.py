import sqlite3

def execute_sql(sql_string, values=tuple(), dbpath="branches.db"):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_string, values)

#This function updates Reymin's salary to 7300:
sql = """UPDATE employee SET salary=? WHERE pk=?;"""
values = (73000, 7)
execute_sql(sql, values=values)

#This function selects all employees in New York that make > 70,000.
sql = """SELECT * FROM employee JOIN branch ON 
        employee.branch_id=branch.pk WHERE branch.state=? and salary>?;"""
values = ("NY", 70000)
execute_sql(sql, values=values)

# Write a SQL UPDATE statement to change Reymin Guduan's salary to 73000
# Write a SQL SELECT statement to select all employees in New York that make over 70000 a year.
# Your queries may be submitted as either SQL statements or Python code