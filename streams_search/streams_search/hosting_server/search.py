import web
import model
import json
from web import form

### Url mappings

urls = (
	'/', 'Index',
	'/search/','Search',
	
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
        
class Search:
	def POST(self):
		res=web.input()
		print res
		#return json.dumps({'id':res})
		return render.search(res)

app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()
