from app import Branch, Employee
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR,"data","branches.db")

# Branch.dbpath=DBPATH

# new_branch = Branch(city="Yonkers",state="NY",zip=10710)
# new_branch.save()
# updated_branch = Branch.one_from_pk(4)
# updated_branch.city="Test2"
# updated_branch.save()

# Employee.dbpath=DBPATH

#To test branch function
# emp = Employee.one_from_pk(2)
# emp_branch = emp.branch()
# print(emp_branch)