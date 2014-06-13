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
import DAContrato
import CContrato

#Gestion Dueño Control
class GContratoCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mTipoContrato = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccContrato:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaContrato:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateContrato:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarContrato:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		dtienda = DAContrato.DAContrato()
		dtienda.mTipoContrato = self.mRequest.get('GCTTIP')
		dtienda.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstContrato = []
		keyValue = str(self.mRequest.get('GCTKEY'))
		qry = DAContrato.DAContrato.query()
		for recContrato in qry:
			if keyValue != "":
				if str(recContrato.key.id()) == keyValue:
					lstContrato.append(CContrato.CContrato(str(recContrato.mTipoContrato),str(recContrato.key.id())).jsonSerialize())
			else :
				lstContrato.append(CContrato.CContrato(str(recContrato.mTipoContrato),str(recContrato.key.id())).jsonSerialize())
		self.mReturnValue = lstContrato

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GCTTIP'))
		keyValue = str(self.mRequest.get('GCTKEY'))
		qry = DAContrato.DAContrato.query()
		# Ejecutar el query
		if keyValue != "":
			for recContrato in qry:
				if str(recContrato.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recContrato.mTipoContrato = nombrereturnValue
					recContrato.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GCTKEY'))
		qry = DAContrato.DAContrato.query()
		if keyValue != "":
			for recContrato in qry:
				if str(recContrato.key.id()) == keyValue:
					self.mReturnValue = "1"
					recContrato.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
