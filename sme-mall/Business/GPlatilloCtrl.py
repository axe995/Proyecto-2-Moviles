# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Dataaccess'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CommonEntities'))
from google.appengine.ext import ndb
import Constantes
import DPlatillo
import DIngXPlat
import DIngrediente
import CPlatillo
import CIngrediente

#Gestion Platillo Control
class GPlatilloCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombrePlatillo = ""
		self.mPrecio = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mOperacionSelect:
			self.Select()
		if self.mOperation == Constantes.Constantes().mOperacionInsert:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mOperacionUpdate:
			self.Update()
		if self.mOperation == Constantes.Constantes().mOperacionDelete:
			self.Delete()
		if self.mOperation == Constantes.Constantes().mGPOperacionAgregaIng:
			self.AgregarIngrediente()
		if self.mOperation == Constantes.Constantes().mGPOperacionBorrarIng:
			self.BorrarIngrediente()
		if self.mOperation == Constantes.Constantes().mGPOperacionSeleccIng:
			self.SeleccionarIngredientes()


	def Insert(self):
		self.mReturnValue = "0"
		dplatillo = DPlatillo.DPlatillo()
		dplatillo.mNombrePlatillo = self.mRequest.get('GPNOM')
		dplatillo.mPrecio = self.mRequest.get('GPPRE')
		dplatillo.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstPlatillos = []
		keyValue = str(self.mRequest.get('GPKEY'))
		qry = DPlatillo.DPlatillo.query()
		for recPlatillo in qry:
			if keyValue != "":
				if str(recPlatillo.key.id()) == keyValue:
					lstPlatillos.append(CPlatillo.CPlatillo(str(recPlatillo.mNombrePlatillo),str(recPlatillo.mPrecio),str(recPlatillo.key.id())).jsonSerialize())
			else :
				lstPlatillos.append(CPlatillo.CPlatillo(str(recPlatillo.mNombrePlatillo),str(recPlatillo.mPrecio),str(recPlatillo.key.id())).jsonSerialize())
		self.mReturnValue = lstPlatillos

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombreValue = str(self.mRequest.get('GPNOM'))
		precioValue = str(self.mRequest.get('GPPRE'))
		keyValue = str(self.mRequest.get('GPKEY'))
		qry = DPlatillo.DPlatillo.query()
		# Ejecutar el query
		if keyValue != "":
			for recPlatillo in qry:
				if str(recPlatillo.key.id()) == keyValue:					
					if nombreValue != "":
						recPlatillo.mNombrePlatillo = nombreValue
					if precioValue != "":
						recPlatillo.mPrecio = precioValue
					recPlatillo.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GPKEY'))
		qry = DPlatillo.DPlatillo.query()
		if keyValue != "":
			for recPlatillo in qry:
				if str(recPlatillo.key.id()) == keyValue:
					self.mReturnValue = "1"
					recPlatillo.key.delete()
	
	def AgregarIngrediente(self):
		self.mReturnValue = "0"
		keyPlatilloValue = str(self.mRequest.get('GPKEY'))
		keyIngredienteValue = str(self.mRequest.get('GIKEY'))
		dingxplat = DIngXPlat.DIngXPlat()
		dingxplat.mKeyPlatillo = keyPlatilloValue
		dingxplat.mKeyIngrediente = keyIngredienteValue
		dingxplat.put()
		self.mReturnValue = "1"

	def BorrarIngrediente(self):
		self.mReturnValue = "0"
		keyPlatilloValue = str(self.mRequest.get('GPKEY'))
		keyIngredienteValue = str(self.mRequest.get('GIKEY'))
		qry = DIngXPlat.DIngXPlat.query()
		if keyPlatilloValue != "" and keyIngredienteValue != "":
			for recPlatillo in qry:
				if str(recPlatillo.mKeyPlatillo) == keyPlatilloValue and str(recPlatillo.mKeyIngrediente) == keyIngredienteValue:
					self.mReturnValue = "1"
					recPlatillo.key.delete()

	def SeleccionarIngredientes(self):
		self.mReturnValue = "0"
		lstIngredientes = []
		keyPlatilloValue = str(self.mRequest.get('GPKEY'))
		qryPlatillo = DIngXPlat.DIngXPlat.query()
		qryIngrediente = DIngrediente.DIngrediente.query()
		for recPlatillo in qryPlatillo:
			if str(recPlatillo.mKeyPlatillo) == keyPlatilloValue:					
				for recIngrediente in qryIngrediente:
					if str(recIngrediente.key.id()) == str(recPlatillo.mKeyIngrediente):
						lstIngredientes.append(CIngrediente.CIngrediente(str(recIngrediente.mNombreIngrediente),str(recIngrediente.mCalorias),str(recIngrediente.key.id())).jsonSerialize())
		self.mReturnValue = lstIngredientes

	def GetValue(self):
		return self.mReturnValue