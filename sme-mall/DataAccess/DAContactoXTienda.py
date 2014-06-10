# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

from google.appengine.ext import ndb

class DAContactoXTienda(ndb.Model):
	_KeyTipoC = ndb.StringProperty(indexed=True)
	_KeyTienda = ndb.StringProperty(indexed=True)
	_ValorC = ndb.StringProperty(indexed=False)
	
	def setValorC(self, pValorC=""):
     if type(pValorC) is str:
     self._ValorC = pValorC
	 
	def getValorC(self):
     return self._ValorC