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
import DAServicio
import CServicio

#Gestion Dueño Control
class GServicioCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mKeyMerc = ""
		self.mPrecioContrato = ""
		self.mFechaInicioContrato = ""
		self.mFechaLiberacionContrato = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccServicio:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaServicio:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateServicio:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarServicio:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		ddueno = DAServicio.DAServicio()
		ddueno.mKeyMerc = self.mRequest.get('GSRKMR')
		ddueno.mPrecioContrato = self.mRequest.get('GSRPPC')
		ddueno.mFechaInicioContrato = self.mRequest.get('GSRFIC')
		ddueno.mFechaLiberacionContrato = self.mRequest.get('GSRFLC')
		ddueno.put()
		self.mReturnValue = "1" 
		
		

	def Select(self):
		lstServicio = []
		keyValue = str(self.mRequest.get('GSRKEY'))
		qry = DAServicio.DAServicio.query()
		for recServicio in qry:
			if keyValue != "":
				if str(recServicio.key.id()) == keyValue:
					lstServicio.append(CServicio.CServicio(str(recServicio.mKeyMerc),str(recServicio.mPrecioContrato),str(recServicio.mFechaInicioContrato),str(recServicio.mFechaLiberacionContrato),str(recServicio.key.id())).jsonSerialize())
			else :
				lstServicio.append(CServicio.CServicio(str(recServicio.mKeyMerc),str(recServicio.mPrecioContrato),str(recServicio.mFechaInicioContrato),str(recServicio.mFechaLiberacionContrato),str(recServicio.key.id())).jsonSerialize())
		self.mReturnValue = lstServicio

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		llavemercaderiareturnValue = str(self.mRequest.get('GSRKMR'))
		precioporcontratoreturnValue = str(self.mRequest.get('GSRPPC'))
		fechainiciocontreturnValue = str(self.mRequest.get('GSRFIC'))
		fechafinalcontreturnValue = str(self.mRequest.get('GSRFLC'))
		keyValue = str(self.mRequest.get('GSRKEY'))
		qry = DAServicio.DAServicio.query()
		# Ejecutar el query
		if keyValue != "":
			for recServicio in qry:
				if str(recServicio.key.id()) == keyValue:					
					if llavemercaderiareturnValue != "":
						recServicio.mKeyMerc = llavemercaderiareturnValue
					if precioporcontratoreturnValue != "":
						recServicio.mPrecioContrato = precioporcontratoreturnValue
					if fechainiciocontreturnValue != "":
						recServicio.mFechaInicioContrato = fechainiciocontreturnValue
					if fechafinalcontreturnValue != "":
						recServicio.mFechaLiberacionContrato = fechafinalcontreturnValue
					recServicio.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GSRKEY'))
		qry = DAServicio.DAServicio.query()
		if keyValue != "":
			for recServicio in qry:
				if str(recServicio.key.id()) == keyValue:
					self.mReturnValue = "1"
					recServicio.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
