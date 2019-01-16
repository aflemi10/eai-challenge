#Allen Fleming

#imports elasticsearch
from elasticsearch import Elasticsearch

#creating a class using elasticsearch
class database:

    #constructor for a given or a default host
    def __init__(self,host):
        if host==None:
            self.client=Elasticsearch('localhost')
        else:
            self.client=Elasticsearch(host)


    #database event for POST  to add a unique name
    #adds index to the database
    #error if index already exists
    def add(self,name,phone,email,address):
        if not self.client.indices.exists(index=name):
            doc = {
                'name':name,
                'phone': phone,
                'email': email,
                'address': address,
            }
            res = self.client.index(index=name, doc_type='document', id=1, body=doc)
        else:
            return -1


    #database event for DELETE unique name
    #deletes index of given name
    #error if index doesnt exist
    def delete(self,name):
        if self.client.indices.exists(index=name):
            self.client.indices.delete(index=name)
            return 0
        else:
            return -1


    #database event for PUT update unique name
    #updates index of given name
    #error if index doesnt exist
    def update(name):
        if self.client.indices.exists(index=name):
            self.client.indices.refresh(index=name)
            return 0
        else:
            return -1


    #database event for GET unique name
    #returns a string format of the index given
    #error if index doesnt exist
    def get(self,name):
        try:
            if self.client.indices.exists(index=name):
                res = self.client.search(index=name, doc_type="document", body={"query": {"match_all": {}}})
                for hit in res['hits']['hits']:
                    output="<p>Name: %(name)s<p> Phone: %(phone)s<p> Email: %(email)s<p> Address: %(address)s" % hit["_source"]
                    return output
            else:
                return -1
        except :
            return -1


    #database event for GET query search
    #returns a string format of the query returned formatted
    #to the correct page and page size
    #returns error if no pages found in query
    def query(self,page,pageSize,query):

            res = self.client.search(index="*", doc_type="document", body={"query": {"query_string": {"query": query}}})
            output=list()
            pageSize=int(pageSize)
            page=int(page)
            lowBound=((page-1)*pageSize)
            highBound=((page)*pageSize)
            for hit in res['hits']['hits']:
                item="<p>Name: %(name)s<p> Phone: %(phone)s<p> Email: %(email)s<p> Address: %(address)s<p><br>" % hit["_source"]
                output.append(item)
            outputstr=""
            ctr=lowBound
            while ctr< highBound:
                outputstr+=output[ctr]
                ctr+=1
            return outputstr
