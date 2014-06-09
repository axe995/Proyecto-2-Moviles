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
    _NombreTienda = ndb.StringProperty(indexed=False)
	_DescripcionTienda = ndb.StringProperty(indexed=False)
	_URLFotoTienda = ndb.StringProperty(indexed=False)
	_UbicacionTienda = ndb.StringProperty(indexed=False)
	_DuenoTienda = ndb.StringProperty(indexed=False)
	_HorarioTienda = ndb.StringProperty(indexed=False)
	
	def setNombreTienda(self, pNombreTienda=""):
     if type(pNombreTienda) is str:
     self._NombreTienda = pNombreTienda
	 
	def getNombreTienda(self):
     return self._NombreTienda
	 
	def setDescripcionTienda(self, pDescripcionTienda=""):
     if type(pDescripcionTienda) is str:
     self._DescripcionTienda = pDescripcionTienda
	 
	def getDescripcionTienda(self):
     return self._DescripcionTienda
	 
	def setURLFotoTienda(self, pURLFotoTienda=""):
     if type(pURLFotoTienda) is str:
     self._URLFotoTienda = pURLFotoTienda
	 
	def getURLFotoTienda(self):
     return self._URLFotoTienda
	 
	def setUbicacionTienda(self, pUbicacionTienda=""):
     if type(pUbicacionTienda) is str:
     self._UbicacionTienda = pUbicacionTienda
	 
	def getUbicacionTienda(self):
     return self._UbicacionTienda
	 
	def setDuenoTienda(self, pDuenoTienda=""):
     if type(pDuenoTienda) is str:
     self._DuenoTienda = pDuenoTienda
	 
	def getDuenoTienda(self):
     return self._DuenoTienda
	 
	def setHorarioTienda(self, pHorarioTienda=""):
     if type(pHorarioTienda) is str:
     self._HorarioTienda = pHorarioTienda
	 
	def getHorarioTienda(self):
     return self._HorarioTienda
