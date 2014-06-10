# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAServicio(ndb.Model):
	_KeyMerc = ndb.StringProperty(indexed=True)
	_PrecioContrato = ndb.IntegerProperty(indexed=False)
	_FechaInicioContrato = ndb.StringProperty(indexed=False)
	_FechaLiberacionContrato = ndb.StringProperty(indexed=False)
	 
	def setPrecioContrato(self, pPrecioContrato):
     if type(pPrecioContrato) is int:
     self._PrecioContrato = pPrecioContrato
	 
	def getPrecioContrato(self):
     return self._PrecioContrato
	 
	def setFechaInicioContrato(self, pFechaInicioContrato=""):
     if type(pFechaInicioContrato) is str:
     self._FechaInicioContrato = pFechaInicioContrato
	 
	def getFechaInicioContrato(self):
     return self._FechaInicioContrato
	 
	def setFechaLiberacionContrato(self, pFechaLiberacionContrato=""):
     if type(pFechaLiberacionContrato) is str:
     self._FechaLiberacionContrato = pFechaLiberacionContrato
	 
	def getFechaLiberacionContrato(self):
     return self._FechaLiberacionContrato