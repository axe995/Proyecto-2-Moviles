# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

pNombreDueno="", pCorreoDueno="", pEdadDueno="", pResidenciaDueno="", pDescripcionDueno=""

class DACliente(ndb.Model):
    mNombreDueno = ndb.StringProperty(indexed=True)
    mCorreoDueno = ndb.StringProperty(indexed=True)
    mEdadDueno = ndb.StringProperty(indexed=True)
    mResidenciaDueno = ndb.StringProperty(indexed=True)
    mDescripcionDueno = ndb.StringProperty(indexed=True)

    def setNombreDueno(self, pNombreDueno=""):
     if type(pNombreDueno) is str:
     self.mNombreDueno = pNombreDueno

    def setCorreoDueno(self, pCorreoDueno=""):
     if type(pCorreoDueno) is str:
     self.mCorreoDueno = pCorreoDueno

    def setEdadDueno(self, pEdadDueno=""):
     if type(pEdadDueno) is str:
     self.mEdadDueno = pEdadDueno

    def setResidenciaDueno(self, pResidenciaDueno=""):
     if type(pResidenciaDueno) is str:
     self.mResidenciaDueno = pResidenciaDueno

    def setDescripcionDueno(self, pDescripcionDueno=""):
     if type(pDescripcionDueno) is str:
     self.mDescripcionDueno = pDescripcionDueno

    def getNombreDueno(self):
     return self.mNombreDueno
	
    def getCorreoDueno(self):
     return self.mCorreoDueno

    def getEdadDueno(self):
     return self.mEdadDueno

    def getResidenciaDueno(self):
     return self.mResidenciaDueno

    def getDescripcionDueno(self):
     return self.mDescripcionDueno

    def saveDS(self):
     self.put()
