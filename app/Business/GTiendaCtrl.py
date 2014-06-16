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
import DADueno
import CTienda
import DAEtiqueta
import DAEtiquetaXTienda
import CEtiqueta

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
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccTie2:
			self.Select2()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaTie:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGMOperacionUpdateTie:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarTie:
			self.Delete()
		if self.mOperation == Constantes.Constantes().mGMOperacionInsertaEtiqueta:
			self.AgregarEtiqueta()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccionaEtiqueta:
			self.SeleccionarEtiquetas()


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
		keyDueno = ""
		qryDueno = DADueno.DADueno.query()
		for recDueno in qryDueno:
			if keyValue != "":
				if recDueno.mCorreoDueno == keyValue:
					keyDueno = str(recDueno.key.id())
		qry = DATienda.DATienda.query()
		for recTienda in qry:
			if keyDueno != "":
				if str(recTienda.mKeyDuenoTienda) == keyDueno:
					lstTienda.append(CTienda.CTienda(str(recTienda.mNombreTienda),str(recTienda.mDescripcionTienda),str(recTienda.mURLFotoTienda),str(recTienda.mLongitud),str(recTienda.mLatitud),str(recTienda.mHorarioTienda),str(recTienda.mKeyDuenoTienda),str(recTienda.key.id())).jsonSerialize())
			else :
				lstTienda.append(CTienda.CTienda(str(recTienda.mNombreTienda),str(recTienda.mDescripcionTienda),str(recTienda.mURLFotoTienda),str(recTienda.mLongitud),str(recTienda.mLatitud),str(recTienda.mHorarioTienda),str(recTienda.mKeyDuenoTienda),str(recTienda.key.id())).jsonSerialize())
		self.mReturnValue = lstTienda

	def Select2(self):
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
		keyDueno = ""
		qryDueno = DADueno.DADueno.query()
		for recDueno in qryDueno:
			if keyValue != "":
				if recDueno.mCorreoDueno == keyValue:
					keyDueno = str(recDueno.key.id())
		qry = DATienda.DATienda.query()
		# Ejecutar el query
		if keyValue != "":
			for recTienda in qry:
				if str(recTienda.mKeyDuenoTienda) == keyDueno:					
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
						recTienda.mKeyDuenoTienda = keyDueno
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
		

	def AgregarEtiqueta(self):
		self.mReturnValue = "0"
		keyTiendaValue = str(self.mRequest.get('GTKEY'))
		keyEtiquetaValue = str(self.mRequest.get('GEKEY'))
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
					keyTienda = str(recTienda.key.id())
		keyEtiqueta = ""
		qry = DAEtiqueta.DAEtiqueta.query()
		for recEtiqueta in qry:
			if keyEtiquetaValue != "":
				if str(recEtiqueta.mNombreEtiqueta) == keyEtiquetaValue:
					keyEtiqueta = str(recEtiqueta.key.id())
		if keyEtiqueta == "":
			nuevaEtiqueta = DAEtiqueta.DAEtiqueta()
			nuevaEtiqueta.mNombreEtiqueta = keyEtiquetaValue
			keyNueva = nuevaEtiqueta.put()
			keyEtiqueta = str(keyNueva.id())
		exists = "0"
		qry = DAEtiquetaXTienda.DAEtiquetaXTienda.query()
		for recEtiquetaRel in qry:
			if recEtiquetaRel.mKeyEtiqueta ==  keyEtiqueta and recEtiquetaRel.mKeyTienda == keyTienda:
				exists = "1"
		if exists == "0":
			detiqXtienda = DAEtiquetaXTienda.DAEtiquetaXTienda()
			detiqXtienda.mKeyTienda = keyTienda
			detiqXtienda.mKeyEtiqueta = keyEtiqueta
			detiqXtienda.put()
		self.mReturnValue = "1"

	def SeleccionarEtiquetas(self):
		self.mReturnValue = "0"
		lstEtiquetas = []
		keyTiendaValue = str(self.mRequest.get('GTKEY'))
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
					keyTienda = str(recTienda.key.id())
		qryTienda = DAEtiquetaXTienda.DAEtiquetaXTienda.query()
		qryEtiqueta = DAEtiqueta.DAEtiqueta.query()
		for recTienda in qryTienda:
			if str(recTienda.mKeyTienda) == keyTienda:					
				for recEtiqueta in qryEtiqueta:
					if str(recEtiqueta.key.id()) == str(recTienda.mKeyEtiqueta):
						lstEtiquetas.append(CEtiqueta.CEtiqueta(str(recEtiqueta.mNombreEtiqueta),str(recEtiqueta.key.id())).jsonSerialize())
		self.mReturnValue = lstEtiquetas

	def GetValue(self):
		return self.mReturnValue
