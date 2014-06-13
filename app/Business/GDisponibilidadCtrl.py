# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'DataAccess'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CommonEntities'))
from google.appengine.ext import ndb
import Constantes
import DADisponibilidad
import CDisponibilidad

#Gestion Dueño Control
class GDisponibilidadCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mTipoDisponibilidad = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccDis:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaDis:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateDis:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarDis:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		dtienda = DADisponibilidad.DADisponibilidad()
		dtienda.mTipoDisponibilidad = self.mRequest.get('GDSTIP')
		dtienda.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstDisponibilidad = []
		keyValue = str(self.mRequest.get('GDSKEY'))
		qry = DADisponibilidad.DADisponibilidad.query()
		for recDisponibilidad in qry:
			if keyValue != "":
				if str(recDisponibilidad.key.id()) == keyValue:
					lstDisponibilidad.append(CDisponibilidad.CDisponibilidad(str(recDisponibilidad.mTipoDisponibilidad),str(recDisponibilidad.key.id())).jsonSerialize())
			else :
				lstDisponibilidad.append(CDisponibilidad.CDisponibilidad(str(recDisponibilidad.mTipoDisponibilidad),str(recDisponibilidad.key.id())).jsonSerialize())
		self.mReturnValue = lstDisponibilidad

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GDSTIP'))
		keyValue = str(self.mRequest.get('GDSKEY'))
		qry = DADisponibilidad.DADisponibilidad.query()
		# Ejecutar el query
		if keyValue != "":
			for recDisponibilidad in qry:
				if str(recDisponibilidad.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recDisponibilidad.mTipoDisponibilidad = nombrereturnValue
					recDisponibilidad.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GDSKEY'))
		qry = DADisponibilidad.DADisponibilidad.query()
		if keyValue != "":
			for recDisponibilidad in qry:
				if str(recDisponibilidad.key.id()) == keyValue:
					self.mReturnValue = "1"
					recDisponibilidad.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
