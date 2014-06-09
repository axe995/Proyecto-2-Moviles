# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAMercaderia(ndb.Model):
    _NombreMerc = ndb.StringProperty(indexed=False)
	_DescripcionMerc = ndb.StringProperty(indexed=False)
	_URLFotoMerc = ndb.StringProperty(indexed=False)
	_TipoMerc = ndb.StringProperty(indexed=False)
	
	def setNombreMerc(self, pNombreMerc=""):
     if type(pNombreMerc) is str:
     self._NombreMerc = pNombreMerc
	 
	def getNombreMerc(self):
     return self._NombreMerc
	 
	def setDescripcionMerc(self, pDescripcionMerc=""):
     if type(pDescripcionMerc) is str:
     self._DescripcionMerc = pDescripcionMerc
	 
	def getDescripcionMerc(self):
     return self._DescripcionMerc
	 
	def setURLFotoMerc(self, pURLFotoMerc=""):
     if type(pURLFotoMerc) is str:
     self._URLFotoMerc = pURLFotoMerc
	 
	def getURLFotoMerc(self):
     return self._URLFotoMerc
	 
	def setTipoMerc(self, pTipoMerc=""):
     if type(pTipoMerc) is str:
     self._TipoMerc = pTipoMerc
	 
	def getTipoMerc(self):
     return self._TipoMerc
