# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

from google.appengine.ext import ndb

class DMercaderiaXBackpack(ndb.Model):
	mKeyMerc = ndb.StringProperty(indexed=True)
	mKeyBackpack = ndb.StringProperty(indexed=True)