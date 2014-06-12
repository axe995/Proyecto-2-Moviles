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
	mTipoContrato = ndb.StringProperty(indexed=True)
	 
	def setTipoContrato(self, pTipoContrato=""):
		if type(pTipoContrato) is str:
			self.mTipoContrato = pTipoContrato
	 
	def getTipoContrato(self):
		return self.mTipoContrato
