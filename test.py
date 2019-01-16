#Allen Fleming

#import statements
import unittest
from flask import Flask ,request
from elasticsearch import Elasticsearch
from database import database
from api import putContact,searchContact,getContact,postContact,deleteContact


db=database(None)


#testing methods from the database class
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        db.add('allen','703-774-6588','aflemi10@gmu.edu','42 P Sherman Wallaby way')
        db.add('kevin','703-580-9817','kev@gmu.edu','9 fox lane')


    #checks that get method returns -1 if unavailable index is requested
    def test_get_invalid_index(self):
        correct=-1
        response=db.get('bob')
        self.assertEqual(correct,response)

    #checks that correct index is retrieved even if multiple indexes exist
    def test_get_valid_index(self):
        correct="<p>Name: kevin<p> Phone: 703-580-9817<p> Email: kev@gmu.edu<p> Address: 9 fox lane"
        response=db.get('kevin')
        self.assertEqual(correct,response)

    #checks that the add methods returns -1 if multiples are added
    def test_add_multiple(self):
        db.add('allen','703-774-6588','aflemi10@gmu.edu','42 P Sherman Wallaby way')
        response=(db.add('allen','703-580-9817','kev@gmu.edu','9 fox lane'))
        correct=-1
        self.assertEqual(correct,response)
        db.delete('allen')
        db.add('allen','703-774-6588','aflemi10@gmu.edu','42 P Sherman Wallaby way')

    #tests that the delete method works correctly if given index is valid
    def test_delete_valid(self):
        correct=0
        response=(db.delete('allen'))
        response2=(db.get('allen'))
        self.assertEqual(correct,response)
        self.assertEqual(response2,-1)

    #tests that the delete method returns an error if the given index is invalid
    def test_delete_invalid(self):
        self.assertEqual(-1,db.delete('jack'))

    #tests the query method
    def test_query(self):
        db.add('a1-name','a1-phone','a1-email','a1-address')
        db.add('a2-name','a2-phone','a2-email','a2-address')
        db.add('a3-name','a3-phone','a3-email','a3-address')
        db.add('a4-name','a4-phone','a4-email','a4-address')
        db.add('a5-name','a5-phone','a5-email','a5-address')
        db.add('a6-name','a6-phone','a6-email','a6-address')
        db.add('a7-name','a7-phone','a7-email','a7-address')
        db.add('a8-name','a8-phone','a8-email','a8-address')
        pageNumber=3
        pageSize=2
        response=db.query(pageNumber,pageSize,'name')
        correct='<p>Name: a5-name<p> Phone: a5-phone<p> Email: a5-email<p> Address: a5-address<p><br><p>Name: a6-name<p> Phone: a6-phone<p> Email: a6-email<p> Address: a6-address<p><br>'
        self.assertEqual(correct,response)


class TestAPIFunctions(unittest.TestCase):
    putContact,searchContact,getContact,postContact,deleteContact

    #tests that posting contacts work
    def test_postContact(self):
        ret=deleteContact('allen')
        ret=postContact('allen','703-774-6588','all3nf15','4400 rivanna river way')
        self.assertEqual('Contact added',ret)

    #tests error is returned if duplicate entry is posted
    def test_postContact_duplicate(self):
        postContact('allen','703-774-6588','all3nf15','4400 rivanna river way')
        ret=postContact('allen','703-774-6588','all3nf15','4400 rivanna river way')
        self.assertEqual('Error adding contact',ret)

    #tests the deleteContact method for names in the database
    def test_deleteContact(self):
        postContact('allen','703-774-6588','all3nf15','4400 rivanna river way')
        ret=deleteContact('allen')
        self.assertEqual('Contact deleted succesfully',ret)

    #tests the deleteContact method for names not in the database
    def test_deleteContact_invalid(self):
        deleteContact('allen')
        ret=deleteContact('allen')
        self.assertEqual('Contact not found',ret)

    #tests the getContact method for valid retrievals
    def test_getContact_valid(self):
        postContact('joe','732-643-6123','joe@gmu.edu','4400 rivanna river way')
        ret=getContact('joe')
        correct='<p>Name: joe<p> Phone: 732-643-6123<p> Email: joe@gmu.edu<p> Address: 4400 rivanna river way'
        self.assertEqual(ret,correct)

    #tests the get contact method for invalid retrievals
    def test_getContact_invalid(self):
        ret=getContact('mike')
        correct='Contact not found'
        self.assertEqual(ret,correct)


if __name__ == '__main__':
    unittest.main()
