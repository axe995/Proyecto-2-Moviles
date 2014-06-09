# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DACliente(ndb.Model):
    _NombreCliente = ndb.StringProperty(indexed=False)
    _CorreoCliente = ndb.StringProperty(indexed=False)
    _UltimaFechaActividad = ndb.StringProperty(indexed=False)


    def setNombreCliente(self, pNombreCliente=""):
     if type(pNombreCliente) is str:
     self._NombreCliente = pNombreCliente

    def setCorreoCliente(self, pCorreoCliente=""):
     if type(pCorreoCliente) is str:
     self._CorreoCliente = pCorreoCliente

    def setUltimaFechaActividad(self, pUltimaFechaActividad=""):
     if type(pUltimaFechaActividad) is str:
     self._UltimaFechaActividad = UltimaFechaActividad

    def getNombreCliente(self):
     return self._NombreCliente
	
    def getCorreoCliente(self):
     return self._CorreoCliente

    def getUltimaFechaActividadCliente(self):
     return self._UltimaFechaActividad

    def saveDS(self):
     self.put()
