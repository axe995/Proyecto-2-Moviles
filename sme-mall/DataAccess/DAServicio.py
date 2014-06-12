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
	mKeyMerc = ndb.StringProperty(indexed=True)
	mPrecioContrato = ndb.IntegerProperty(indexed=True)
	mFechaInicioContrato = ndb.StringProperty(indexed=True)
	mFechaLiberacionContrato = ndb.StringProperty(indexed=True)
	 
	def setPrecioContrato(self, pPrecioContrato):
     if type(pPrecioContrato) is int:
     self.mPrecioContrato = pPrecioContrato
	 
	def getPrecioContrato(self):
     return self.mPrecioContrato
	 
	def setFechaInicioContrato(self, pFechaInicioContrato=""):
     if type(pFechaInicioContrato) is str:
     self.mFechaInicioContrato = pFechaInicioContrato
	 
	def getFechaInicioContrato(self):
     return self.mFechaInicioContrato
	 
	def setFechaLiberacionContrato(self, pFechaLiberacionContrato=""):
     if type(pFechaLiberacionContrato) is str:
     self.mFechaLiberacionContrato = pFechaLiberacionContrato
	 
	def getFechaLiberacionContrato(self):
     return self.mFechaLiberacionContrato