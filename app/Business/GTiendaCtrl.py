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
import DATienda
import CTienda
import DAContactoXTienda
import DATipoContacto
import CContactoxTienda

#Gestion Dueño Control
class GTiendaCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreTienda = ""
		self.mDescripcionTienda = ""
		self.mURLFotoTienda = ""
		self.mLongitud = ""
		self.mLatitud = ""
		self.mKeyDuenoTienda = ""
		self.mHorarioTienda = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccTie:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaTie:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGMOperacionUpdateTie:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarTie:
			self.Delete()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaContactoxTienda:
			self.AgregarContactoXTienda()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarContactoxTiendae:
			self.DeleteContactoXTienda()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccContactoxTienda:
			self.SeleccionarContactos()


	def Insert(self):
		self.mReturnValue = "0"
		dtienda = DATienda.DATienda()
		dtienda.mNombreTienda = self.mRequest.get('GTNOM')
		dtienda.mDescripcionTienda = self.mRequest.get('GTDES')
		dtienda.mURLFotoTienda = self.mRequest.get('GTFOT')
		dtienda.mLongitud = self.mRequest.get('GTLOT')
		dtienda.mLatitud = self.mRequest.get('GTLAT')
		dtienda.mHorarioTienda = self.mRequest.get('GTTIM')
		dtienda.mKeyDuenoTienda = self.mRequest.get('GTGDK')
		dtienda.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstTienda = []
		keyValue = str(self.mRequest.get('GTKEY'))
		qry = DATienda.DATienda.query()
		for recTienda in qry:
			if keyValue != "":
				if str(recTienda.key.id()) == keyValue:
					lstTienda.append(CTienda.CTienda(str(recTienda.mNombreTienda),str(recTienda.mDescripcionTienda),str(recTienda.mURLFotoTienda),str(recTienda.mLongitud),str(recTienda.mLatitud),str(recTienda.mHorarioTienda),str(recTienda.mKeyDuenoTienda),str(recTienda.key.id())).jsonSerialize())
			else :
				lstTienda.append(CTienda.CTienda(str(recTienda.mNombreTienda),str(recTienda.mDescripcionTienda),str(recTienda.mURLFotoTienda),str(recTienda.mLongitud),str(recTienda.mLatitud),str(recTienda.mHorarioTienda),str(recTienda.mKeyDuenoTienda),str(recTienda.key.id())).jsonSerialize())
		self.mReturnValue = lstTienda

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GTNOM'))
		descripcionreturnValue = str(self.mRequest.get('GTDES'))
		urlfotoreturnValue = str(self.mRequest.get('GTFOT'))
		longitudreturnValue = str(self.mRequest.get('GTLOT'))
		latitudreturnValue = str(self.mRequest.get('GTLAT'))
		horarioreturnValue = str(self.mRequest.get('GTTIM'))
		keyduenoreturnValue = str(self.mRequest.get('GTGDK'))
		keyValue = str(self.mRequest.get('GTKEY'))
		qry = DATienda.DATienda.query()
		# Ejecutar el query
		if keyValue != "":
			for recTienda in qry:
				if str(recTienda.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recTienda.mNombreTienda = nombrereturnValue
					if descripcionreturnValue != "":
						recTienda.mDescripcionTienda = descripcionreturnValue
					if urlfotoreturnValue != "":
						recTienda.mURLFotoTienda = urlfotoreturnValue
					if longitudreturnValue != "":
						recTienda.mLongitud = longitudreturnValue
					if latitudreturnValue != "":
						recTienda.mLatitud = latitudreturnValue
					if horarioreturnValue != "":
						recTienda.mHorarioTienda = horarioreturnValue
					if keyduenoreturnValue != "":
						recTienda.mKeyDuenoTienda = keyduenoreturnValue
					recTienda.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GTKEY'))
		qry = DATienda.DATienda.query()
		if keyValue != "":
			for recTienda in qry:
				if str(recTienda.key.id()) == keyValue:
					self.mReturnValue = "1"
					recTienda.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
		
	#ContactoXTienda
	def AgregarContactoXTienda(self):
		self.mReturnValue = "0"
		keyValueTienda = str(self.mRequest.get('GTKEY'))
		keyValueTipoContacto = str(self.mRequest.get('GTCKEY'))
		ValueContacto = str(self.mRequest.get('GTVACO'))
		daContactoXTienda = DAContactoXTienda.DAContactoXTienda()
		daContactoXTienda.mKeyTipoC = keyValueTipoContacto
		daContactoXTienda.mKeyTienda = keyValueTienda
		daContactoXTienda.mValorC = ValueContacto
		bandera = "0"
		qry = DAContactoXTienda.DAContactoXTienda.query()
		# Ejecutar el query
		if keyValueTienda != "" and keyValueTipoContacto != "":
			for recContactoXTienda in qry:
				if str(recContactoXTienda.mKeyTipoC) == daContactoXTienda.mKeyTipoC and str(recContactoXTienda.mKeyTienda) == daContactoXTienda.mKeyTienda and str(recContactoXTienda.mValorC) == daContactoXTienda.mValorC:					
					bandera = "1"
		
		if bandera == "0":
			daContactoXTienda.put()
			self.mReturnValue = "1"
			
		
	
	def DeleteContactoXTienda(self):
		self.mReturnValue = "0"
		keyValueTienda = str(self.mRequest.get('GTKEY'))
		keyValueTipoContacto = str(self.mRequest.get('GTCKEY'))
		qry = DAContactoXTienda.DAContactoXTienda.query()
		if keyValueTienda != "" and keyValueTipoContacto != "":
			for recTienda in qry:
				if str(recTienda.mKeyTipoC) == keyValueTipoContacto and str(recTienda.mKeyTienda) == keyValueTienda:
					self.mReturnValue = "1"
					recTienda.key.delete()
	
	def SeleccionarContactos(self):
		self.mReturnValue = "0"
		lstContactoporTienda = []
		keyValueTienda = str(self.mRequest.get('GTKEY'))
		qryContactoxTienda= DAContactoXTienda.DAContactoXTienda.query()
		qryTipoContacto= DATipoContacto.DATipoContacto.query()
		if keyValueTienda != "":
			for recContactoXTienda in qryContactoxTienda:
				if str(recContactoXTienda.mKeyTienda) == keyValueTienda:					
					for recTipoContacto in qryTipoContacto:
							if str(recTipoContacto.key.id()) == str(recContactoXTienda.mKeyTipoC):
								lstContactoporTienda.append(CContactoxTienda.CContactoxTienda(str(recContactoXTienda.mValorC),str(recContactoXTienda.mKeyTienda),str(recContactoXTienda.mKeyTipoC),str(recTipoContacto.mNombreTipoC),str(recContactoXTienda.key.id())).jsonSerialize())
			self.mReturnValue = lstContactoporTienda
