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
    _NombreEtiqueta = ndb.StringProperty(indexed=False)
	
	def setNombreEtiqueta(self, pNombreEtiqueta=""):
     if type(pNombreEtiqueta) is str:
     self._NombreEtiqueta = pNombreEtiqueta
	 
	def getNombreEtiqueta(self):
     return self._NombreEtiqueta