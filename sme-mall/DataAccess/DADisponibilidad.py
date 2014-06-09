# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DADisponibilidad(ndb.Model):
	_TipoDisponibilidad = ndb.StringProperty(indexed=False)
	 
	def setTipoDisponibilidad(self, pTipoDisponibilidad=""):
		if type(pTipoDisponibilidad) is str:
			self._TipoDisponibilidad = pTipoDisponibilidad
	 
	def getTipoDisponibilidad(self):
		return self._TipoDisponibilidad