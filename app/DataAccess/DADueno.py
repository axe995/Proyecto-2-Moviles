# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DADueno(ndb.Model):
    mNombreDueno = ndb.StringProperty(indexed=True)
    mCorreoDueno = ndb.StringProperty(indexed=True)
    mResidenciaDueno = ndb.StringProperty(indexed=True)
    mDescripcionDueno = ndb.StringProperty(indexed=True)

   
