import requests
import json

url = 'http://0.0.0.0:3000/'

def send_search(search_text):
    keywords = {'keyword': search_text} 
    requests.post(url, data=json.dumps(keywords)) 