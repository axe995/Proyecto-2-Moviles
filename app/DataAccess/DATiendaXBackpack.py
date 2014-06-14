# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

from google.appengine.ext import ndb

class DATiendaXBackpack(ndb.Model):
	mKeyTienda = ndb.StringProperty(indexed=True)
	mKeyBackpack = ndb.StringProperty(indexed=True)
