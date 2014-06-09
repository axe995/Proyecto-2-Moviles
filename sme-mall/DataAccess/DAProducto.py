# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAProducto(ndb.Model):
    _CantidadDisponibleProd = ndb.IntegerProperty(indexed=False)
	_PrecioUnitarioProd = ndb.IntegerProperty(indexed=False)
	_FechaDevolucionProd = ndb.StringProperty(indexed=False)
	
	def setCantidadDisponibleProd(self, pCantidadDisponibleProd):
     if type(pCantidadDisponibleProd) is int:
     self._CantidadDisponibleProd = pCantidadDisponibleProd
	 
	def getCantidadDisponibleProd(self):
     return self._CantidadDisponibleProd
	 
	def setPrecioUnitarioProd(self, pPrecioUnitarioProd):
     if type(pPrecioUnitarioProd) is int:
     self._PrecioUnitarioProd = pPrecioUnitarioProd
	 
	def getPrecioUnitarioProd(self):
     return self._PrecioUnitarioProd
	 
	def setFechaDevolucionProd(self, pFechaDevolucionProd=""):
     if type(pFechaDevolucionProd) is str:
     self._FechaDevolucionProd = pFechaDevolucionProd
	 
	def getFechaDevolucionProd(self):
     return self._FechaDevolucionProd
