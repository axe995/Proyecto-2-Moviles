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
import DATipoContacto
import CTipoContacto

#Gestion Dueño Control
class GTipoContactoCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreTipoC = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccTipoContacto:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaTipoContacto:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateTipoContacto:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarTipoContacto:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		dtienda = DATipoContacto.DATipoContacto()
		dtienda.mNombreTipoC = self.mRequest.get('GTCTIP')
		dtienda.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstTipoContacto = []
		keyValue = str(self.mRequest.get('GTCKEY'))
		qry = DATipoContacto.DATipoContacto.query()
		for recTipoContacto in qry:
			if keyValue != "":
				if str(recTipoContacto.key.id()) == keyValue:
					lstTipoContacto.append(CTipoContacto.CTipoContacto(str(recTipoContacto.mNombreTipoC),str(recTipoContacto.key.id())).jsonSerialize())
			else :
				lstTipoContacto.append(CTipoContacto.CTipoContacto(str(recTipoContacto.mNombreTipoC),str(recTipoContacto.key.id())).jsonSerialize())
		self.mReturnValue = lstTipoContacto

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GTCTIP'))
		keyValue = str(self.mRequest.get('GTCKEY'))
		qry = DATipoContacto.DATipoContacto.query()
		# Ejecutar el query
		if keyValue != "":
			for recTipoContacto in qry:
				if str(recTipoContacto.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recTipoContacto.mNombreTipoC = nombrereturnValue
					recTipoContacto.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GTCKEY'))
		qry = DATipoContacto.DATipoContacto.query()
		if keyValue != "":
			for recTipoContacto in qry:
				if str(recTipoContacto.key.id()) == keyValue:
					self.mReturnValue = "1"
					recTipoContacto.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
