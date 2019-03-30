import requests
import json
import web
import sqlite3
import hashlib

db = web.database(dbn='sqlite', db='streamz.db')



def new_user(firstname,lastname,phone,email,username,pwd,subscribers,likes,dislikes):
	id=db.insert('user', firstname=firstname, lastname=lastname,email=email,username=username,pwd=pwd,phone=phone,
subscribers=subscribers,likes=likes,dislikes=dislikes)
	params={'status':'Registered','username':username,'firstname':firstname,'lastname':lastname,'email':email,'phone':phone}
	return json.dumps(params)
	
def check_user(username,password):
    authdb = sqlite3.connect('streamz.db')
    #passhash = hashlib.md5(password).hexdigest()
    c= authdb.execute('select * from user where username=? and pwd=?',(username,password))
    row = c.fetchone()
    if row == None:
		logged={"loggedin":"false"}
		return json.dumps(loggedin) 
    else: 
			params={'status':'LoggedIn','username':username}
			return json.dumps(params)
	#error={"loggedin":"true","username":username} 

def get_user(username):
	authdb = sqlite3.connect('streamz.db')
	c= authdb.execute('select * from user where username=?',[username])
	row = c.fetchone()
	fn=row[1]
	ln=row[2]
	eml=row[3]
	un=row[4]
	ph=row[6]
	dob=row[7]
	coun=row[8]
	cat=row[9]
	subs=row[10]
	lik=row[11]
	dlik=row[12]
	param={'firstname':fn, 'lastname':ln,'email':eml,'username':un,'phone':ph,'dob':dob,'country':coun,
'category':cat,'subscribers':subs,'likes':lik,'dislikes':dlik}	
	return json.dumps(param)

def update_user_details(firstname,lastname,phone,email,username,dob,country,category):

	s=db.update('user', where='username= $username',vars=locals(), firstname=firstname, lastname=lastname,phone=phone,email=email, dob=dob,country=country,category=category)
	return "success"

	
def get_dob(username):

	authdb = sqlite3.connect('streamz.db')
	c= authdb.execute('select * from user where username=?',[username])
	row = c.fetchone()
	dob=row[7]
	param={'dob':dob}
	print param
	return json.dumps(param)

def get_country(username):

	authdb = sqlite3.connect('streamz.db')
	c= authdb.execute('select * from user where username=?',[username])
	row = c.fetchone()
	coun=row[8]
	param={'country':coun}
	print param
	return json.dumps(param)