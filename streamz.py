""" Basic todo list using webpy 0.3 """
import web
import json
from web import form

### Url mappings

urls = (
	'/', 'Index',
	'/video','Video',
	'/home', 'Homepage',
	'/register', 'Register',
 
)


### Templates
render = web.template.render('templates', base='base')


class Index:

	login = form.Form(
	form.Textbox('email'),
	form.Password('password'),
	form.Button('Login'),
	)

	def GET(self):
		""" Show page """
		
		login = self.login()
		return render.index(login)



	def POST(self):
		login = self.login()
		if not login.validates():
			return "Unsuccesful Login"
		else:
			return login.d.email,login.d.password

		""" Add new entry 
		form = self.form()
		if not form.validates():
		    todos = model.get_todos()
		    return render.index(todos, form)
		model.new_todo(form.d.title)
		raise web.seeother('/')
"""
		

class Homepage:

	def GET(self):
		""" Show page """
		
		return render.homepage()

class Video:

	def GET(self):
		""" Show page """
		
		return render.video()

class Register:
	register = form.Form(
	form.Textbox('firstname'),
	form.Textbox('lastname'),
	form.Textbox('phone'),
	form.Textbox('email'),
	form.Password('password'),
	form.Button('Register'),
	)

	def GET(self):
		""" Show page """
		register = self.register()
		return render.register(register)

	def POST(self):
		register = self.register()
		if not register.validates():
			return "Unsuccesful Registration"
		else:
			return register.d.firstname,register.d.lastname,register.d.phone,register.d.email,register.d.password

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
