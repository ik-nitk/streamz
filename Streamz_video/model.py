import web
import json 
import sqlite3

db = web.database(dbn='sqlite', db='videos.db')

def get_videodesc(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	nm=row[1]
	upl=row[4]
	des=row[5]
	cat=row[6]
	count=row[7]
	age=row[8]
	params={'id':id, 'name':nm, 'uploader':upl, 'description':des, 'category':cat, 'countries':count, 'age':age}
	return json.dumps(params)

def get_video(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	url=row[2]
	return open(url,"rb").read()

def get_thumbnail(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	url=row[3]
	return open(url,"rb").read()

def get_videoname(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	nm=row[1]
	params={'name':nm}
	return json.dumps(params)

def get_description(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	desc=row[5]
	params={'description':desc}
	return json.dumps(params)

def get_uploader(id):
	data = db.select('video', order='id')
	authdb = sqlite3.connect('videos.db')
	c= authdb.execute('select * from video where id=?',[id])
	row = c.fetchone()
	ul=row[4]
	params={'uploader':ul}
	return json.dumps(params)

def upload_video(name,videopath, uploader):
	id=db.insert('video', name=name, urlpath=videopath, uploader=uploader)
	params={'id':id}
	return json.dumps(params)

def upload_thumbnail(name,thumbnailpath):
	id=db.insert('video', thumbnail=thumbnailpath)
	params={'id':id}
	return json.dumps(params)
		

def update_video_desc(id,thumbnail,name,description,category,country,age):
	if thumbnail=='':
		db.update('video', where='id= $id',vars=locals(), name=name,description=description,category=category,country=country,age=age)
	else:
		db.update('video', where='id= $id',vars=locals(), name=name, thumbnail=thumbnail,description=description,category=category,country=country,age=age)
	return "success"

def del_video(id):
    db.delete('videos', where="id=$id", vars=locals())
