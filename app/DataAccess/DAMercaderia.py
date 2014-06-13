# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAMercaderia(ndb.Model):
    mNombreMerc = ndb.StringProperty(indexed=True)
    mDescripcionMerc = ndb.StringProperty(indexed=True)
    mURLFotoMerc = ndb.StringProperty(indexed=True)
    mTipoMerc = ndb.StringProperty(indexed=True)
    mKeyTienda = ndb.StringProperty(indexed=True)
    mKeyContrato = ndb.StringProperty(indexed=True)
    mKeyDisponibilidad = ndb.StringProperty(indexed=True)
