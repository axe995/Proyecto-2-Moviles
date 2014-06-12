# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DATienda(ndb.Model):
    mNombreTienda = ndb.StringProperty(indexed=True)
    mDescripcionTienda = ndb.StringProperty(indexed=True)
    mURLFotoTienda = ndb.StringProperty(indexed=True)
    mLongitud = ndb.StringProperty(indexed=True)
    mLatitud = ndb.StringProperty(indexed=True)
    mKeyDuenoTienda = ndb.StringProperty(indexed=True)
    mHorarioTienda = ndb.StringProperty(indexed=True)

