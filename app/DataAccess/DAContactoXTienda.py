# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

from google.appengine.ext import ndb

class DAContactoXTienda(ndb.Model):
	mKeyTipoC = ndb.StringProperty(indexed=True)
	mKeyTienda = ndb.StringProperty(indexed=True)
	mValorC = ndb.StringProperty(indexed=True)
