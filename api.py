#Allen Fleming

#import statements
from flask import Flask ,request
from database import database
import sys


#creating app
app = Flask(__name__)


#either accepts a command line argument for a host for Elasticsearch
#or accepts a None value and automatically sets host to local host
if len(sys.argv)==2:
    db=database(sys.argv[1])
else:
    db=database(None)


#app route to use an search the database using a query
#returns a string of the indexes in the given pageSize
#and page number range
@app.route('/contact',methods=['GET'])
def searchContact():
    try:
        pageSize=request.args.get('pageSize')
        page=request.args.get('page')
        query=request.args.get('query')
        ret = db.query(page,pageSize,query)
        if ret==-1:
            return 'No contacts found with this search'
        else:
            return ret
    except:
        return 'No contacts found with this search'


#app route to retrieve a contact given a unique name
#returns error if a contact is not found
@app.route('/contact/<string:name>',methods=['GET'])
def getContact(name):
    ret = db.get(name)
    if(ret==-1):
        return 'Contact not found'
    else:
        return ret


#app route to update contact given a unique name
#returns error if contact does not exist
@app.route('/contact/<string:name>',methods=['PUT'])
def putContact(name):
    ret = db.put(name)
    if(ret==-1):
        return 'Contact not found'


#app route to post a contact using the url
#returns error if attempts to add a contact that already exists
@app.route('/contact/<string:name>&<string:phone>&<string:email>&<string:address>',methods=['POST'])
def postContact(name,phone,email,address):
    ret = db.add(name,phone,email,address)
    if(ret==-1):
        return 'Error adding contact'
    else:
        return "Contact added"


#app route to delete a contact given a name
#returns an error if contact does not exist
@app.route('/contact/<string:name>',methods=['DELETE'])
def deleteContact(name):
    ret = db.delete(name)
    if ret == -1:
        return 'Contact not found'
    else:
        return 'Contact deleted succesfully'


#runs app
if __name__ == '__main__':
    app.run(debug=True)
