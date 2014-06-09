# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

from google.appengine.ext import ndb

class DAEtiquetaXMercaderia(ndb.Model):
	mKeyEtiqueta = ndb.StringProperty(indexed=True)
	mKeyMercaderia = ndb.StringProperty(indexed=True)