from elasticsearch import Elasticsearch
client = Elasticsearch('localhost')

#database event for POST
def add(name,phone,email,address):
    doc = {
        'phone': phone,
        'email': email,
        'address': address,
        }
    res = client.index(index=name, doc_type='document', id=1, body=doc)
    print(res['result'])

    res = client.get(index=name, doc_type='document', id=1)
    print(res['_source'])

#database event for DELETE unique name
#error if not found
def delete(name):
    if client.indices.exists(index=name):
        client.indices.delete(index=name)
        return 0
    else:
        return -1


#database event for GET query search
def query(pageSize,page,query):
    return 0

#database event for PUT update unique name
#error if not found
def update(name):
    if client.indices.exists(index=name):
        client.indices.refresh(index=name)
        return 0
    else:
        return -1

#database event for GET unique name
#error if not found
def get(name):
    try:
        if client.indices.exists(index=name):
            res=client.get_source(index=name,doc_type='document',id=1)
            print(res)
            output=name+" "+res.get('phone')+" "+res.get('email')+" "+res.get('address')
            return output
        else:
            return -1
    except :
        return -1


'''
add('allen','703-774-6588','big','addres here')
add('kevin','123-456-7891','bigk','address here')
add('new','123-456-7891','bigk','address here')
add('allen','703-774-6588','all3nf13','addres here')

add('kev','123-456-7891','bigk','address here')

get('allen')
get('dad')
'''
