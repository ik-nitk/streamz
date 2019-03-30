#import elasticsearch
from elasticsearch import Elasticsearch 

# Connect to the elastic cluster
es=Elasticsearch([{'host':'localhost','port':9200}])
print es

#dummy data
#12 entries made
e1={    "id": "1", 
        "channel":"mostlysane",
        "uploader": "prajakta kohli",
        "category": "vlogger",
        "title": "books you should read",
        "description": "knowledge",
        "tags": ["books","read"],
        }

e2={
	    "id": "2",
        "channel":"tedtalks",
        "uploader": "tedtalks",
        "category": "motivation",
        "title": "how to stay motivated",
        "description": "motivation",
        "tags": ["inspiration","motivation","motivated"],
}  

e3={
	   "id": "3",
        "channel":"Pogotv",
        "uploader": "pogo",
        "category": "cartoon",
        "title": "chota bheem series",
        "description": "chota bheem",
        "tags": ["chota bheem","kids show"],
} 

e4={    "id": "4",
        "channel":"Pogotv",
        "uploader": "pogo",
        "category": "art",
        "title": "madart",
        "description": "fun art for kids",
        "tags": ["fun art","art","kids show","pogo"], 
        }   


e5={
	    "id": "5",
        "channel":"CNN",
        "uploader": "CNN",
        "category": "news",
        "title": "breaking news",
        "description": "breaking news around the world",
        "tags": ["breaking news","news","world news"],
}   

e6={
	    "id": "6",
        "channel":"Eros Now",
        "uploader": "eros",
        "category": "music",
        "title": "bollywood songs of all time",
        "description": "bollywood songs of all time",
        "tags": ["bollywood songs","hindi songs"],
}      

e7={
	    "id": "7",
        "channel":"health time",
        "uploader": "DR Bhatra",
        "category": "health",
        "title": "top 5 health tips",
        "description": "healthy tips",
        "tags": ["health","healthy tips","medicines"],
}

e8={
	   "id": "8",
        "channel":"yourhealth",
        "uploader": "sadguru",
        "category": "health",
        "title": "diet for diabetes patient",
        "description": "diet",
        "tags": ["diet for diabetes","food for diabetes","health"],
}

e9={
	   "id": "9",
        "channel":"wifistudy",
        "uploader": "aman dattarwal",
        "category": "education",
        "title": "tips to solve math problems",
        "description": "solve mathematics",
        "tags": ["solve math","mathematics"],
}

e10={
	   "id": "10",
        "channel":"TVF",
        "uploader": "TVF",
        "category": "entertainment",
        "title": "Pitchers",
        "description": "web series on startup",
        "tags": ["web series","serials","startup serials"],
}

e11={   "id": "11",
        "channel":"byjus",
        "uploader": "byjus",
        "category": "education",
        "title": "how to prepare for exams",
        "description": "education",
        "tags": ["prepare for exams","exam preparation"],
        }

e12={
	    
	    "id": "12",
        "channel":"BCC",
        "uploader": "BCC",
        "category": "news",
        "title": "breaking news",
        "description": "breaking news around the world",
        "tags": ["breaking news","news","world news"],
}   

# create index called streams1
# added analysers for stemming and tokenizing
# remove stop words
res = es.indices.create(index ='streams2', body = {
   "settings": {
    "analysis": {
      "filter": {
        "english_stop": {
          "type":       "stop",
          "stopwords":  "_english_"
        },
        "light_english_stemmer": {
          "type":       "stemmer",
          "language":   "light_english" 
        },
        "english_possessive_stemmer": {
          "type":       "stemmer",
          "language":   "possessive_english"
        }
      },
      "analyzer": {
        "english": {
          "tokenizer":  "standard",
          "filter": [
            "english_possessive_stemmer",
            "lowercase",
            "english_stop",
            "light_english_stemmer", 
            "asciifolding" ,
          ]
        }
      }
    }
  }
})

res = es.index(index='streams2',doc_type='video',body=e1,id=1)
res = es.index(index='streams2',doc_type='video',body=e2,id=2)
res = es.index(index='streams2',doc_type='video',body=e3,id=3)
res = es.index(index='streams2',doc_type='video',body=e4,id=4)
res = es.index(index='streams2',doc_type='video',body=e5,id=5)
res = es.index(index='streams2',doc_type='video',body=e6,id=6)
res = es.index(index='streams2',doc_type='video',body=e7,id=7)
res = es.index(index='streams2',doc_type='video',body=e8,id=8)
res = es.index(index='streams2',doc_type='video',body=e9,id=9)
res = es.index(index='streams2',doc_type='video',body=e10,id=10)
res = es.index(index='streams2',doc_type='video',body=e11,id=11)
res = es.index(index='streams2',doc_type='video',body=e12,id=12)

