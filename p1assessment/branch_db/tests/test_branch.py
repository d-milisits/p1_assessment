import sqlite3 
import os
from unittest import TestCase
from data import schema, seed
from app import Branch
#python3 -m unittest discover tests 

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR,DBFILENAME)

Branch.dbpath=DBPATH

class TestBranch(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)
    
    def tearDown(self):
        os.remove(DBPATH)
    
    def test_select_by_pk(self):
        item = Branch.one_from_pk(2)
        self.assertEqual(item.city, "Houston")
    
    def test_insert(self):
        item = Branch(city="Yonkers",state="NY",zip="10710")
        item.save()
        branch_list = Branch.all()
        self.assertEqual(len(branch_list),3)
    
    def test_delete(self):
        test_branch = Branch.one_from_pk(1)
        test_branch.delete()
        branch_list = Branch.all()
        self.assertEqual(len(branch_list),1)
    
    def test_update(self):
        test_branch = Branch.one_from_pk(1)
        test_branch.city = "Test"
        test_branch.save()
        test_branch = Branch.one_from_pk(1)
        self.assertEqual(test_branch.city, "Test")