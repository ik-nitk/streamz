import web
import json
import requests
# Import Elasticsearch package 

from elasticsearch import Elasticsearch 
# Connect to the elastic cluster
url='http://0.0.0.0:8080'
def send_search(txt):
  txt=str(txt)
  print(txt)
  videos=[]
  es=Elasticsearch([{'host':'localhost','port':9200}])
  res= es.search(index='streams11',body={"query" : {
                "bool" : {
                    "should" : [
                    { "match" : {"data.channel" : txt}},
                    { "match" : {"data.category" : txt} },
                    {"match":{ "data.uploader" : txt }},
                    {"match": {"data.tags": txt}},
                    {"match": {"data.title":{"query":"txt","analyzer": "english"}}},
                    { "range": { "data.restrictions.age": {"gte": 0,"lt": 1}}},
                     ]
                    }
                    },
                    "sort" : [{"data.duration" : {"order" : "asc", "mode" : "avg"}},

                    ]
                    })
  for hit in res['hits']['hits']:
    videos.append(hit['_source']['data']['id'])
  return videos
   
	
    
