# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DATienda(ndb.Model):
    mNombreTienda = ndb.StringProperty(indexed=True)
	mDescripcionTienda = ndb.StringProperty(indexed=True)
	mURLFotoTienda = ndb.StringProperty(indexed=True)
	mUbicacionTienda = ndb.StringProperty(indexed=True)
	mDuenoTienda = ndb.StringProperty(indexed=True)
	mHorarioTienda = ndb.StringProperty(indexed=True)
	
	def setNombreTienda(self, pNombreTienda=""):
     if type(pNombreTienda) is str:
     self.mNombreTienda = pNombreTienda
	 
	def getNombreTienda(self):
     return self.mNombreTienda
	 
	def setDescripcionTienda(self, pDescripcionTienda=""):
     if type(pDescripcionTienda) is str:
     self.mDescripcionTienda = pDescripcionTienda
	 
	def getDescripcionTienda(self):
     return self.mDescripcionTienda
	 
	def setURLFotoTienda(self, pURLFotoTienda=""):
     if type(pURLFotoTienda) is str:
     self.mURLFotoTienda = pURLFotoTienda
	 
	def getURLFotoTienda(self):
     return self.mURLFotoTienda
	 
	def setUbicacionTienda(self, pUbicacionTienda=""):
     if type(pUbicacionTienda) is str:
     self.mUbicacionTienda = pUbicacionTienda
	 
	def getUbicacionTienda(self):
     return self.mUbicacionTienda
	 
	def setDuenoTienda(self, pDuenoTienda=""):
     if type(pDuenoTienda) is str:
     self.mDuenoTienda = pDuenoTienda
	 
	def getDuenoTienda(self):
     return self.mDuenoTienda
	 
	def setHorarioTienda(self, pHorarioTienda=""):
     if type(pHorarioTienda) is str:
     self.mHorarioTienda = pHorarioTienda
	 
	def getHorarioTienda(self):
     return self.mHorarioTienda
