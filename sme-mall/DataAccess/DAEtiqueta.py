# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAEtiqueta(ndb.Model):
    mNombreEtiqueta = ndb.StringProperty(indexed=True)
	
	def setNombreEtiqueta(self, pNombreEtiqueta=""):
     if type(pNombreEtiqueta) is str:
     self.mNombreEtiqueta = pNombreEtiqueta
	 
	def getNombreEtiqueta(self):
     return self.mNombreEtiqueta