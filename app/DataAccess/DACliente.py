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
