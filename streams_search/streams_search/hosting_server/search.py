import web
import model
from web import form

### Url mappings

urls = (
	'/', 'Index',
	
)


### Templates
render = web.template.render('templates', base='base')

class Index:

	searchform = form.Form(
	form.Textbox('searchtext'),
	form.Button('Search'),
	)

	def GET(self):
		""" Show page """
		searchform = self.searchform()
		return render.index(searchform)

	def POST(self):
		searchform = self.searchform()
		if not searchform.validates():            
			return "Unsuccessful"
		txt=searchform.d.searchtext
		model.send_search(txt)
        
		


app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()