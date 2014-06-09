# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAContrato(ndb.Model):
	_TipoContrato = ndb.StringProperty(indexed=False)
	 
	def setTipoContrato(self, pTipoContrato=""):
		if type(pTipoContrato) is str:
			self._TipoContrato = pTipoContrato
	 
	def getTipoContrato(self):
		return self._TipoContrato
