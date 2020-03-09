import sqlite3 
import os
from unittest import TestCase
from data import schema, seed
from app import Employee
#python3 -m unittest discover tests 

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR,DBFILENAME)

Employee.dbpath=DBPATH

class TestBranch(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)
    
    def tearDown(self):
        os.remove(DBPATH)
    
    def test_select_by_pk(self):
        item = Employee.one_from_pk(2)
        self.assertEqual(item.first, "Casey")
    
    def test_insert(self):
        item = Employee(branch_id=1,first="Dan",last="Milisits",id="S0009",salary=100000)
        item.save()
        employee_list = Employee.all()
        self.assertEqual(len(employee_list),9)
    
    def test_delete(self):
        test_employee = Employee.one_from_pk(1)
        test_employee.delete()
        employee_list = Employee.all()
        self.assertEqual(len(employee_list),7)
    
    def test_update(self):
        test_employee = Employee.one_from_pk(1)
        test_employee.first = "Test"
        test_employee.save()
        test_employee = Employee.one_from_pk(1)
        self.assertEqual(test_employee.first, "Test")