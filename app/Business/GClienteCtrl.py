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
import datetime
from google.appengine.ext import ndb
import Constantes
import DACliente
import CCliente

#Gestion Ingrediente Control
class GClienteCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreCliente = ""
		self.mCorreoCliente = ""
		self.mUltimaFechaActividad = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGPOperacionSeleccCliente:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGPOperacionAgregaCliente:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateCliente:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGPOperacionBorrarCliente:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		dcliente = DACliente.DACliente()
		dcliente.mNombreCliente = self.mRequest.get('GCNOM')
		dcliente.mCorreoCliente = self.mRequest.get('GCCOR')
		localtime = datetime.datetime.utcnow()
		localtime = localtime - datetime.timedelta(hours=6)
		dcliente.mUltimaFechaActividad = localtime.strftime("%Y%m%d") + " " +localtime.time().strftime("%H%M%S")
		bandera = "0"
		qry = DACliente.DACliente.query()
		# Ejecutar el query
		if dcliente.mCorreoCliente != "":
			for recCliente in qry:
				if str(recCliente.mCorreoCliente) == dcliente.mCorreoCliente:					
					bandera = "1"
		
		if bandera == "0":
			dcliente.put()
			self.mReturnValue = "1"
		
		

	def Select(self):
		lstClientes = []
		keyValue = str(self.mRequest.get('GCKEY'))
		qry = DACliente.DACliente.query()
		for recClientes in qry:
			if keyValue != "":
				if str(recClientes.key.id()) == keyValue:
					lstClientes.append(CCliente.CCliente(str(recClientes.mNombreCliente),str(recClientes.mCorreoCliente),str(recClientes.mUltimaFechaActividad),str(recClientes.key.id())).jsonSerialize())
			else :
				lstClientes.append(CCliente.CCliente(str(recClientes.mNombreCliente),str(recClientes.mCorreoCliente),str(recClientes.mUltimaFechaActividad),str(recClientes.key.id())).jsonSerialize())
		self.mReturnValue = lstClientes

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GCNOM'))
		correoreturnValue = str(self.mRequest.get('GCCOR'))
		localtime = datetime.datetime.utcnow()
		localtime = localtime - datetime.timedelta(hours=6)
		fechareturnValue = localtime.strftime("%Y%m%d") + " " +localtime.time().strftime("%H%M%S")
		keyValue = str(self.mRequest.get('GCKEY'))
		qry = DACliente.DACliente.query()
		# Ejecutar el query
		if keyValue != "":
			for recClientes in qry:
				if str(recClientes.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recClientes.mNombreCliente = nombrereturnValue
					if correoreturnValue != "":
						recClientes.mCorreoCliente = correoreturnValue
					if fechareturnValue != "":
						recClientes.mUltimaFechaActividad = fechareturnValue
					recClientes.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GCKEY'))
		qry = DACliente.DACliente.query()
		if keyValue != "":
			for recClientes in qry:
				if str(recClientes.key.id()) == keyValue:
					self.mReturnValue = "1"
					recClientes.key.delete()
		

	def GetValue(self):
		return self.mReturnValue