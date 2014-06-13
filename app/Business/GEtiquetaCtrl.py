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
import DAEtiqueta
import CEtiqueta

#Gestion Dueño Control
class GEtiquetaCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreEtiqueta = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccEtiqueta:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaEtiqueta:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGMOperacionUpdateEtiqueta:
			self.Update()

	def Insert(self):
		self.mReturnValue = "0"
		detiqueta = DAEtiqueta.DAEtiqueta()
		detiqueta.mNombreEtiqueta = self.mRequest.get('GENOM')
		detiqueta.mNombreEtiqueta = detiqueta.mNombreEtiqueta.upper()
		bandera = "0"
		qry = DAEtiqueta.DAEtiqueta.query()
		# Ejecutar el query
		if detiqueta.mNombreEtiqueta != "":
			for recEtiqueta in qry:
				if str(recEtiqueta.mNombreEtiqueta) == detiqueta.mNombreEtiqueta:					
					bandera = "1"
		
		if bandera == "0":
			detiqueta.put()
			self.mReturnValue = "1"
			
		

	def Select(self):
		lstEtiqueta = []
		keyValue = str(self.mRequest.get('GEKEY'))
		qry = DAEtiqueta.DAEtiqueta.query()
		for recEtiqueta in qry:
			if keyValue != "":
				if str(recEtiqueta.key.id()) == keyValue:
					lstEtiqueta.append(CEtiqueta.CEtiqueta(str(recEtiqueta.mNombreEtiqueta),str(recEtiqueta.key.id())).jsonSerialize())
			else :
				lstEtiqueta.append(CEtiqueta.CEtiqueta(str(recEtiqueta.mNombreEtiqueta),str(recEtiqueta.key.id())).jsonSerialize())
		self.mReturnValue = lstEtiqueta

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GENOM'))
		keyValue = str(self.mRequest.get('GEKEY'))
		qry = DAEtiqueta.DAEtiqueta.query()
		# Ejecutar el query
		if keyValue != "":
			for recEtiqueta in qry:
				if str(recEtiqueta.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recEtiqueta.mNombreEtiqueta = nombrereturnValue
					recEtiqueta.put()
					self.mReturnValue = "1"

	def GetValue(self):
		return self.mReturnValue
