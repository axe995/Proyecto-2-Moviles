import cgi
import urllib

from google.appengine.ext import ndb
import webapp2
import Bridge
import json

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		b = Bridge.Bridge(self.request)
		b.IniciarEjecucion()
		self.response.write(b.mReturnValue)

	def put(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		self.response.headers.add_header('Access-Control-Allow-Methods','POST, GET, PUT, DELETE')
		self.response.headers.add_header('Content-Type','application/json') 
		self.response.setContentType("text/html; charset=utf-8")
		b = Bridge.Bridge(self.request)
		b.IniciarEjecucion2()
		self.response.write(json.dumps(b.mReturnValue))

	#Metodo que abilita los metodos http
	def options(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		self.response.headers.add_header('Access-Control-Allow-Methods','POST, GET, PUT, DELETE')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)