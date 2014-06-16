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
import DADueno
import DAMercaderia
import DATienda

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
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccServicio2:
			self.Select2()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaServicio:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateServicio:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarServicio:
			self.Delete()
	

	def Insert(self):
		self.mReturnValue = "0"
		keyTiendaValue = self.mRequest.get('GMKTI') #Correo del dueño
		keyDueno = ""
		qryDueno = DADueno.DADueno.query()
		for recDueno in qryDueno:
			if keyTiendaValue != "":
				if recDueno.mCorreoDueno == keyTiendaValue:
					keyDueno = str(recDueno.key.id())
		keyTienda = ""
		qry = DATienda.DATienda.query()
		for recTienda in qry:
			if keyDueno != "":
				if str(recTienda.mKeyDuenoTienda) == keyDueno:
					keyTienda = recTienda.key.id()
		dmerc = DAMercaderia.DAMercaderia()
		dmerc.mNombreMerc = self.mRequest.get('GMNOM')
		dmerc.mDescripcionMerc = self.mRequest.get('GMDES')
		dmerc.mTipoMerc = "2"
		dmerc.llaveTienda = str(keyTienda)
		dmerc.llaveContrato = self.mRequest.get('GMKCO')
		dmerc.llaveDisponib = self.mRequest.get('GMKDI')
		keyMercaderia = dmerc.put()
		ddueno = DAServicio.DAServicio()
		ddueno.mKeyMerc = str(keyMercaderia.id())
		ddueno.mPrecioContrato = self.mRequest.get('GSRPPC')
		ddueno.mFechaInicioContrato = self.mRequest.get('GSRFIC')
		ddueno.mFechaLiberacionContrato = self.mRequest.get('GSRFLC')
		ddueno.put()
		self.mReturnValue = "1"	
	
	def Select(self):
		lstServicio = []
		keyDueno = str(self.mRequest.get('GSRKEY')) #Correo del dueno
		qryDueno = DADueno.DADueno.query()
		for recDueno in qryDueno:
			if keyDueno != "":
				if recDueno.mCorreoDueno == keyDueno:
					keyDueno = str(recDueno.key.id())
		keyTienda = ""
		qry = DATienda.DATienda.query()
		for recTienda in qry:
			if keyDueno != "":
				if str(recTienda.mKeyDuenoTienda) == keyDueno:
					keyTienda = str(recTienda.key.id())
		keyMercaderia = ""
		qry = DAMercaderia.DAMercaderia.query()
		for recMerc in qry:
			if keyTienda != "":
				if str(recMerc.mKeyTienda) == keyTienda:
					keyMercaderia = str(recMerc.key.id())
		qry = DAServicio.DAServicio.query()
		for recServicio in qry:
			if keyMercaderia != "":
				if str(recServicio.mKeyMerc) == keyMercaderia:
					lstServicio.append(CServicio.CServicio(str(recServicio.mKeyMerc),str(recServicio.mPrecioContrato),str(recServicio.mFechaInicioContrato),str(recServicio.mFechaLiberacionContrato),str(recServicio.key.id())).jsonSerialize())
			else :
				lstServicio.append(CServicio.CServicio(str(recServicio.mKeyMerc),str(recServicio.mPrecioContrato),str(recServicio.mFechaInicioContrato),str(recServicio.mFechaLiberacionContrato),str(recServicio.key.id())).jsonSerialize())
		self.mReturnValue = lstServicio

	def Select2(self):
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
