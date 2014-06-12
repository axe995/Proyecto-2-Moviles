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
	mKeyMerc = ndb.StringProperty(indexed=True)
    mCantidadDisponibleProd = ndb.IntegerProperty(indexed=True)
	mPrecioUnitarioProd = ndb.IntegerProperty(indexed=True)
	mFechaDevolucionProd = ndb.StringProperty(indexed=True)
	
	def setCantidadDisponibleProd(self, pCantidadDisponibleProd):
     if type(pCantidadDisponibleProd) is int:
     self.mCantidadDisponibleProd = pCantidadDisponibleProd
	 
	def getCantidadDisponibleProd(self):
     return self.mCantidadDisponibleProd
	 
	def setPrecioUnitarioProd(self, pPrecioUnitarioProd):
     if type(pPrecioUnitarioProd) is int:
     self.mPrecioUnitarioProd = pPrecioUnitarioProd
	 
	def getPrecioUnitarioProd(self):
     return self.mPrecioUnitarioProd
	 
	def setFechaDevolucionProd(self, pFechaDevolucionProd=""):
     if type(pFechaDevolucionProd) is str:
     self.mFechaDevolucionProd = pFechaDevolucionProd
	 
	def getFechaDevolucionProd(self):
     return self.mFechaDevolucionProd
