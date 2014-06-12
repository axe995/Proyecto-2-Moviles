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
    mNombreMerc = ndb.StringProperty(indexed=True)
	mDescripcionMerc = ndb.StringProperty(indexed=True)
	mURLFotoMerc = ndb.StringProperty(indexed=True)
	mTipoMerc = ndb.StringProperty(indexed=True)
	mKeyTienda = ndb.StringProperty(indexed=True)
	mKeyContrato = ndb.StringProperty(indexed=True)
	mKeyDisponibilidad = ndb.StringProperty(indexed=True)
	
	def setNombreMerc(self, pNombreMerc=""):
     if type(pNombreMerc) is str:
     self.mNombreMerc = pNombreMerc
	 
	def getNombreMerc(self):
     return self.mNombreMerc
	 
	def setDescripcionMerc(self, pDescripcionMerc=""):
     if type(pDescripcionMerc) is str:
     self.mDescripcionMerc = pDescripcionMerc
	 
	def getDescripcionMerc(self):
     return self.mDescripcionMerc
	 
	def setURLFotoMerc(self, pURLFotoMerc=""):
     if type(pURLFotoMerc) is str:
     self.mURLFotoMerc = pURLFotoMerc
	 
	def getURLFotoMerc(self):
     return self.mURLFotoMerc
	 
	def setTipoMerc(self, pTipoMerc=""):
     if type(pTipoMerc) is str:
     self.mTipoMerc = pTipoMerc
	 
	def getTipoMerc(self):
     return self.mTipoMerc
