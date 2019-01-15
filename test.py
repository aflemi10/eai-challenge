import unittest
from flask import Flask ,request
from elasticsearch import Elasticsearch
import database
import hello
client = Elasticsearch('localhost')

#testing methods from
class TestDatabaseFunctions(unittest.TestCase):
    #add
    #delete
    #query
    #update
    #get
    
class TestAPIFunctions(unittest.TestCase):
    #searchContact
    #getContact
    #putContact
    #postContact
    #deleteContact
