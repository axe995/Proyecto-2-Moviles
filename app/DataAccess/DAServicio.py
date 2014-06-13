# coding: utf-8
"""
Proyecto 2
Electiva Desarrollo de Aplicaciones Moviles
Andres Gonzalez
David Montero
Emanuel Avendano
"""
from google.appengine.ext import ndb

class DAServicio(ndb.Model):
	mKeyMerc = ndb.StringProperty(indexed=True)
	mPrecioContrato = ndb.StringProperty(indexed=True)
	mFechaInicioContrato = ndb.StringProperty(indexed=True)
	mFechaLiberacionContrato = ndb.StringProperty(indexed=True)
