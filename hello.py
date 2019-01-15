from flask import Flask ,request

from database import get,delete,update,query
app = Flask(__name__)

@app.route('/contact',methods=['GET'])
def searchContact():
    pageSize=request.args.get('pageSize')
    page=request.args.get('page')
    query=request.args.get('query')
    ret = query(pageSize,page,query)
    return ret

@app.route('/contact/<string:name>',methods=['GET'])
def getContact(name):
    ret = get(name)
    if(ret==-1):
        return 'Contact not found'
    else:
        return get(name)

@app.route('/contact/<string:name>',methods=['PUT'])
def putContact(name):
    ret = put(name)
    if(ret==-1):
        return 'Contact not found'

@app.route('/contact/<string:name>',methods=['POST'])
def postContact(name):
    return "post contact"

@app.route('/contact/<string:name>',methods=['DELETE'])
def deleteContact(name):
    ret = delete(name)
    if ret == -1:
        return 'Contact not found'

if __name__ == '__main__':
    app.run(debug=True)
