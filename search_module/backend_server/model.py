#import libraries
import web
import json
import requests

# Import Elasticsearch package 
from elasticsearch import Elasticsearch 


# function to upload details to server
#details consists of id,channel,uploader,category,title,description and tags
def send_details(details):
  ids=json.loads(details)['id']
  # Connect to the elastic cluster
  es=Elasticsearch([{'host':'localhost','port':9200}])
  res = es.index(index='streams1',doc_type='video',body=details,id=ids)  #index_name=streams1, doc_type=videos
  return res


# function to search by keywords
#search based on category,channel,uploader,title,tags
def send_search(txt):
  txt=str(txt)
  #print(txt)
  videos=[]
  es=Elasticsearch([{'host':'localhost','port':9200}])
  res= es.search(index='streams1',body={"query" : {
                "bool" : {
                    "should" : [
                    { "match" : {"channel" : txt}},
                    { "match" : {"category" : txt} },
                    {"match":{ "uploader" : txt }},
                    {"match": {"tags": txt}},
                    {"match": {"title":{"query":txt,"analyzer": "english"}}},
                    
                     ]
                    }
                    }
                    })
  for hit in res['hits']['hits']:
    videos.append(hit['_source']['id'])
  ids = {'id': videos}
  return ids

  
 # function to delete from server 
def delete(index):
  #print index
  es=Elasticsearch([{'host':'localhost','port':9200}])
  res = es.delete(index='streams1', doc_type='video', id=index)
  return res	
    
