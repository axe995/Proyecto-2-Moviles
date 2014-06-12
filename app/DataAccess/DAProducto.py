# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAProducto(ndb.Model):
	mKeyMerc = ndb.StringProperty(indexed=True)
	mKeyDueno = ndb.StringProperty(indexed=True)
        mCantidadDisponibleProd = ndb.IntegerProperty(indexed=True)
	mPrecioUnitarioProd = ndb.IntegerProperty(indexed=True)
	mFechaDevolucionProd = ndb.StringProperty(indexed=True)
	
	
