import requests
import json
import web
import sqlite3
import hashlib

db = web.database(dbn='sqlite', db='streamz.db')

def new_user(firstname,lastname,phone,email,username,pwd):
    #userdb=sqlite3.connect('streamz.db')
    #id=userdb.insert('insert values into user)
    id=db.insert('user', firstname=firstname, lastname=lastname,email=email,username=username,pwd=pwd,phone=phone)
    dict={"username":username,"id":id}
    return json.dumps(dict)


def check_user(username,password):
    authdb = sqlite3.connect('streamz.db')
    #passhash = hashlib.md5(password).hexdigest()
    c= authdb.execute('select * from user where username=? and pwd=?',(username,password))
    row = c.fetchone()
    if row == None:
    #if pass2==password: 
        logged={"loggedin":"false"}
 	#raise web.seeother('/results')
	return json.dumps({"loggedin":"false"})   
    else: 
	error={"loggedin":"true","username":username} 
	return json.dumps(error)

