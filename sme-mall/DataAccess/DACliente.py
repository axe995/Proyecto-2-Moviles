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
    mNombreCliente = ndb.StringProperty(indexed=True)
    mCorreoCliente = ndb.StringProperty(indexed=True)
    mUltimaFechaActividad = ndb.StringProperty(indexed=True)


    def setNombreCliente(self, pNombreCliente=""):
     if type(pNombreCliente) is str:
     self.mNombreCliente = pNombreCliente

    def setCorreoCliente(self, pCorreoCliente=""):
     if type(pCorreoCliente) is str:
     self.mCorreoCliente = pCorreoCliente

    def setUltimaFechaActividad(self, pUltimaFechaActividad=""):
     if type(pUltimaFechaActividad) is str:
     self.mUltimaFechaActividad = UltimaFechaActividad

    def getNombreCliente(self):
     return self.mNombreCliente
	
    def getCorreoCliente(self):
     return self.mCorreoCliente

    def getUltimaFechaActividadCliente(self):
     return self.mUltimaFechaActividad

    def saveDS(self):
     self.put()
