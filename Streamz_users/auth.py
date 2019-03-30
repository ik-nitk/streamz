import web
import model
import json
import requests
import hashlib

urls = ('/login', 'Login',
        '/logout', 'Logout',
        '/register', 'Register',
	'/profile', 'Profile',
	'/updateprofile', 'UpdateProfile',
        '/getdob', 'GetDob',
        '/getcountry', 'GetCountry',
        )


class Register:
   
        def POST(self):
                data = web.data()
                fn=json.loads(data)['firstname']
                ln=json.loads(data)['lastname']
                ph=json.loads(data)['phone']
                eml=json.loads(data)['email']
                un=json.loads(data)['username']
                pwd=json.loads(data)['password']
                pwd1= hashlib.md5(pwd).hexdigest()
                p=model.new_user(fn,ln,ph,eml,un,pwd1,0,0,0)
                return p
        

class Login:
    
        def POST(self):
                data=web.data()
                un=json.loads(data)['username']
                pwd=json.loads(data)['password']
                passhash = hashlib.md5(pwd).hexdigest()
                id=model.check_user(un,passhash)
                return id
	

class Profile:
    
        def POST(self):
                data=web.data()
                user=json.loads(data)['username']
                s=model.get_user(user)
                return s


class UpdateProfile:

        def GET(self):
                fn="aulick3"
                ln="sah3"
                ph="1234567890"
                eml="asdfghjkl@gsdd.com"
                un="lakshmi"
                dob="2017-07-07"
                country="India1"
                category="Preeti"
                p=model.update_user_details(fn,ln,eml,un)
                return p
    
        def POST(self):
                data=web.data()
                fn=json.loads(data)['firstname']
                ln=json.loads(data)['lastname']
                ph=json.loads(data)['phone']
                eml=json.loads(data)['email']
                un=json.loads(data)['username']
		dob=json.loads(data)['dob']
		country=json.loads(data)['country']
		category=json.loads(data)['category']
                p=model.update_user_details(fn,ln,ph,eml,un,dob,country,category)
                return p

class GetDob:
    
        def POST(self):
                data=web.data()
                un=json.loads(data)['username']
                s=model.get_dob(un)
                return s

class GetCountry:
    
        def POST(self):
                data=web.data()
                un=json.loads(data)['username']
                s=model.get_country(un)
                return s

app = web.application(urls, globals())

if __name__ == '__main__':
        app.run()
