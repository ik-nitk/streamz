import web
import model
import json

### Url mappings

urls = (
    '/', 'Index',
    
)
url='http://0.0.0.0:8080'
#
# This is the backend server.
#
#

class Index:

    def GET(self):
        """no function"""

    def POST(self):
        
        keywords= web.data()
        ids = model.send_search(json.loads(keywords)['keyword'])
        #print json.dumps({'id': ids})


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
