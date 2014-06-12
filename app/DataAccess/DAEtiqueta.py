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
    mNombreEtiqueta = ndb.StringProperty(indexed=True)
