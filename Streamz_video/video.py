import web
import model
import json
import requests

urls = ('/getvideodesc', 'GetVideoDesc',
        '/upload', 'UploadVideo',
	'/updatevideo', 'UpdateVideo',
        '/getvideo', 'GetVideo',
        '/getthumbnail', 'GetThumbnail',
        '/getvideoname', 'GetVideoName',
        '/getuploader', 'GetUploader',
        '/getdescription', 'GetDescription',
	'/updatevideoinfo', 'UpdateVideoInfo',
        '/getuploads','GetUploads',
        '/deletevideo','DeleteVideo',
        '/updatelikestatus','UpdateLikeStatus',
        '/getchannellikescount','GetChannelLikesCount',
)
class GetChannelLikesCount:
        def POST(self):
                data=web.data()
                upl=json.loads(data)['uploader']
                s=model.get_channel_likes_count(upl)
                return s

class UpdateLikeStatus:
        def POST(self):
                data=web.data()
                vid=json.loads(data)['videoid']
                lks=json.loads(data)['likes']
                dlks=json.loads(data)['dislikes']
                s=model.update_likestatus(vid,lks,dlks)
                return s

class DeleteVideo:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['id']
                s=model.delete_video(id)
                return s

class GetVideo:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_video(id)
                return s

class GetThumbnail:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_thumbnail(id)
                return s

class GetVideoName:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_videoname(id)
                return s

class GetDescription:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_description(id)
                return s

class GetUploader:
    
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_uploader(id)
                return s

class GetVideoDesc:
        def POST(self):
                data=web.data()
                id=json.loads(data)['vid']
                s=model.get_videodesc(id)
                return s

class UploadVideo:
        def POST(self):
                web.header('Access-Control-Allow-Origin','*')
                web.header('Access-Control-Allow-Credentials', 'true')
                data = web.input()
                filename=data['name']
                uploader=data['uploader']
                fout = open('static/videos' +'/'+ filename,'w')
                fout.write(data['file']) 
                fout.close() 
                res = model.upload_video(filename,'static/videos/' + filename, uploader)
                return res

class UpdateVideo:
        def POST(self):
                web.header('Access-Control-Allow-Origin','*')
                web.header('Access-Control-Allow-Credentials', 'true')
                data = web.input()
                filename=data['thumbnail_name']
                videoname=data['video_name']
                description=data['description']
                category=data['category']
                country=data['countries']
                age=data['age']
                tags=data['tags']
                id=data['id']
                if filename!="":
                        fout = open('static/thumbnails' +'/'+ filename,'w')
                        fout.write(data['thumbnail_file']) 
                        fout.close() 
                        s=model.update_video_desc(id,'static/thumbnails/' + filename,videoname,description,category,country,age,tags)
                else:
                        s=model.update_video_desc(id,'',videoname,description,category,country,age,tags)
                return s

class GetUploads:
        def POST(self):
                data=web.data()
                un=json.loads(data)['username']
                s=model.get_uploads(un)
                return s

app = web.application(urls, globals())

if __name__ == '__main__':
        app.run()
