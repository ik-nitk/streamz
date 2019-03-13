#import packages
import web
import model
import json

### Url mappings
#insertion,search,deletion

urls = (
	'/details','Details',
    '/search', 'Search',
    '/delete','Delete',
    '/sort','Sort',
    '/filter','Filter',
    
)
# sorting and filtering to be added
# This is the backend server.
#
#



# search by keyword
class Search:
    def GET(self):
        """no function"""

    def POST(self):
        
        keywords= web.data()
        ids = model.send_search(json.loads(keywords)['keyword'])
        #print ids
        return ids


# delete by id
class Delete:

    def GET(self):
        """no function"""

    def POST(self):
        
        index= web.data()
        res = model.delete(json.loads(index)['id'])
        #print res
        return res  

#insert video details
class Details:
    def POST(self):
        
        data= web.data()
        ids=json.loads(data)['id']
        channel=json.loads(data)['channel']
        uploader=json.loads(data)['uploader']
        category=json.loads(data)['category']
        title=json.loads(data)['title']
        description=json.loads(data)['desc']
        tags=json.loads(data)['tags']
        details=json.dumps({'id':ids,'channel':channel,'uploader':uploader,'category':category,'title':title,'description':description,'tags':tags})
        #print details
        res = model.send_details(details)
        return res
        

       
        
		
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
