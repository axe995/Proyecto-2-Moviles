# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DATipoContacto(ndb.Model):
	_NombreTipoC = ndb.StringProperty(indexed=False)
	 
	def setNombreTipoC(self, pNombreTipoC=""):
     if type(pNombreTipoC) is str:
     self._NombreTipoC = pNombreTipoC
	 
	def getNombreTipoC(self):
     return self._NombreTipoC
