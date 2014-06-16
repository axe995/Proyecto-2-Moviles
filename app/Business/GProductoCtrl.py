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
import DAProducto
import DAMercaderia
import DAContrato
import DADueno
import DATienda
import DADisponibilidad
import CProducto

#Gestion Dueño Control
class GProductoCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mKeyMerc = ""
		self.mCantidadDisponibleProd = ""
		self.mPrecioUnitarioProd = ""
		self.mFechaDevolucionProd = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccProducto:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaProducto:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateProducto:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarProducto:
			self.Delete()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccProducto2:
			self.Select2()


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
					keyTienda = recTienda.key
		keyContrato = ""
		qryContrato = DAContrato.DAContrato.query()
		for recContrato in qryContrato:
			if recContrato.mTipoContrato == "venta":
				keyContrato = recContrato.key
		keyDisponibilidad = ""
		qryDisponibilidad = DADisponibilidad.DADisponibilidad.query()
		for recDisponibilidad in qryDisponibilidad:
			if recDisponibilidad.mTipoDisponibilidad == "inmediata":
				keyDisponibilidad = recDisponibilidad.key
		dmerc = DAMercaderia.DAMercaderia()
		dmerc.mNombreMerc = self.mRequest.get('GMNOM')
		dmerc.mDescripcionMerc = self.mRequest.get('GMDES')
		dmerc.mTipoMerc = "1"
		dmerc.llaveTienda = str(keyTienda.id())
		dmerc.llaveContrato = str(keyContrato.id())
		dmerc.llaveDisponib = str(keyDisponibilidad.id())
		keyMercaderia = dmerc.put()
		ddueno = DAProducto.DAProducto()
		ddueno.mKeyMerc = str(keyMercaderia.id())
		ddueno.mCantidadDisponibleProd = self.mRequest.get('GPRCAN')
		ddueno.mPrecioUnitarioProd = self.mRequest.get('GPRPUN')
		ddueno.mFechaDevolucionProd = self.mRequest.get('GPRDEV')
		ddueno.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstProducto = []
		keyDueno = str(self.mRequest.get('GPRKEY'))
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
		qry = DAProducto.DAProducto.query()
		for recProducto in qry:
			if keyMercaderia != "":
				if str(recProducto.mKeyMerc) == keyMercaderia:
					lstProducto.append(CProducto.CProducto(str(recProducto.mKeyMerc),str(recProducto.mCantidadDisponibleProd),str(recProducto.mPrecioUnitarioProd),str(recProducto.mFechaDevolucionProd),str(recProducto.key.id())).jsonSerialize())
			else :
				lstProducto.append(CProducto.CProducto(str(recProducto.mKeyMerc),str(recProducto.mCantidadDisponibleProd),str(recProducto.mPrecioUnitarioProd),str(recProducto.mFechaDevolucionProd),str(recProducto.key.id())).jsonSerialize())
		self.mReturnValue = lstProducto

	def Select2(self):
		lstProducto = []
		keyValue = str(self.mRequest.get('GPRKEY'))
		qry = DAProducto.DAProducto.query()
		for recProducto in qry:
			if keyValue != "":
				if str(recProducto.key.id()) == keyValue:
					lstProducto.append(CProducto.CProducto(str(recProducto.mKeyMerc),str(recProducto.mCantidadDisponibleProd),str(recProducto.mPrecioUnitarioProd),str(recProducto.mFechaDevolucionProd),str(recProducto.key.id())).jsonSerialize())
			else :
				lstProducto.append(CProducto.CProducto(str(recProducto.mKeyMerc),str(recProducto.mCantidadDisponibleProd),str(recProducto.mPrecioUnitarioProd),str(recProducto.mFechaDevolucionProd),str(recProducto.key.id())).jsonSerialize())
		self.mReturnValue = lstProducto

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		llavemercaderiareturnValue = str(self.mRequest.get('GPRKMR'))
		cantidadreturnValue = str(self.mRequest.get('GPRCAN'))
		preciounitarioreturnValue = str(self.mRequest.get('GPRPUN'))
		fechadevolucionreturnValue = str(self.mRequest.get('GPRDEV'))
		keyValue = str(self.mRequest.get('GPRKEY'))
		qry = DAProducto.DAProducto.query()
		# Ejecutar el query
		if keyValue != "":
			for recProducto in qry:
				if str(recProducto.key.id()) == keyValue:					
					if llavemercaderiareturnValue != "":
						recProducto.mKeyMerc = llavemercaderiareturnValue
					if cantidadreturnValue != "":
						recProducto.mCantidadDisponibleProd = cantidadreturnValue
					if preciounitarioreturnValue != "":
						recProducto.mPrecioUnitarioProd = preciounitarioreturnValue
					if fechadevolucionreturnValue != "":
						recProducto.mFechaDevolucionProd = fechadevolucionreturnValue
					recProducto.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GPRKEY'))
		qry = DAProducto.DAProducto.query()
		if keyValue != "":
			for recProducto in qry:
				if str(recProducto.key.id()) == keyValue:
					self.mReturnValue = "1"
					recProducto.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
