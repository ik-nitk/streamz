import requests
import json
import datetime
from datetime import date

def new_user(firstname,lastname,phone,email,username,password):
    params = {'firstname': firstname,'lastname':lastname,'phone':phone,'email':email,'username':username,'password':password} 
    p=requests.post('http://0.0.0.0:9090/register', data=json.dumps(params))
    return p.json()

def check_user(username,password):
    params = {'username': username,'password':password} 
    p=requests.post('http://0.0.0.0:9090/login', data=json.dumps(params))
    return p.json()

def get_profile(username):
    params = {'username':username} 
    p=requests.post('http://0.0.0.0:9090/profile', data=json.dumps(params))
    return p.json()

def get_dob(username):
    params = {'username':username} 
    p=requests.post('http://0.0.0.0:9090/getdob', data=json.dumps(params))
    return p.json()

def get_country(username):
    params = {'username':username} 
    p=requests.post('http://0.0.0.0:9090/getcountry', data=json.dumps(params))
    return p.json()

     
def update_profile(firstname,lastname,username,phone,email,category,country,dob):
    params = {'firstname':firstname,'lastname':lastname,'username':username,'phone':phone,'email':email,'category':category,'country':country,'dob':dob} 
    p=requests.post('http://0.0.0.0:9090/updateprofile', data=json.dumps(params))
    return p
    #return json.dumps(params)

"""--------------------------------------Search---------------------------------"""

def send_search(search_text,age,country):
    params = {'keyword': search_text,'user_age':age,'user_country':country} 
    p=requests.post('http://0.0.0.0:7070/search', data=json.dumps(params))
    return p.json()
    #return json.dumps(params)

def search_upload_video(path):
    params = {'name':name,'description':description,'tags':tags} 
    #requests.post(url1, data=json.dumps(params))
    return json.dumps(params)
"""--------------------------------------Comments---------------------------------"""

def send_comment(search_text):
    params = {'comment_text':search_text} 
    #requests.post(url1, data=json.dumps(params))
    return json.dumps(params)

"""--------------------------------------Video Upload-----------------------------------------"""

def get_videodesc(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getvideodesc', data=json.dumps(params))
    return p.json()
    #return json.dumps(params)


def upload_video(x,uploader):
    file1 = {'file': x.myfile.file.read(),'name':x.myfile.filename,'uploader':uploader}
    p = requests.post("http://0.0.0.0:5050/upload", files=file1)
    return p.json()


def upload_video_info(id,name,description,tags,countries,category,uploader,age,th):

    params = {'id':id,'video_name':name,'description':description,'tags':tags,'category':category,'countries':json.dumps(countries),'uploader':uploader,'age':age} 
    p=requests.post('http://0.0.0.0:7070/details', data=json.dumps(params))

    paramsth = {'thumbnail_file': th.mythumbnail.file.read(),'thumbnail_name':th.mythumbnail.filename,'id':id,'video_name':name,'description':description,'category':category,'countries':json.dumps(countries),'age':age}
    q = requests.post('http://0.0.0.0:5050/updatevideo', files=paramsth)
    #return p.json()    

def get_video(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getvideo', data=json.dumps(params))
    return p
    #return json.dumps(params)

def get_thumbnail(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getthumbnail', data=json.dumps(params))
    return p

def get_videoname(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getvideoname', data=json.dumps(params))
    return p.json()

def get_description(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getdescription', data=json.dumps(params))
    return p.json()

def get_uploader(id):
    params = {'vid': id} 
    p=requests.post('http://0.0.0.0:5050/getuploader', data=json.dumps(params))
    return p.json()

def calculate_Age(db):
    db=datetime.datetime.strptime(db, '%Y-%m-%d').date()
    today = date.today()
    age=today.year - db.year - ((today.month, today.day) < (db.month, db.day))
    return age