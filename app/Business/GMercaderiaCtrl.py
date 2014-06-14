# coding: utf-8

#Proyecto 2
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
import DAMercaderia
import CMercaderia
import DAEtiquetaXMercaderia
import DAEtiqueta
import CEtiqueta

#Gestion Mercaderia Control
class GMercaderiaCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreMerc = ""
		self.mDescripcionMerc = ""
		self.mURLFotoMerc = ""
		self.mTipoMerc = ""
		self.mKeyTienda = ""
		self.mKeyContrato = ""
		self.mKeyDisponibilidad = ""
		self.mKeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccMerc:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaMerc:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGMOperacionUpdateMerc:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarMerc:
			self.Delete()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaEtiquetaxMerc:
			self.AgregarEtiquetaXMercaderia()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarEtiquetaxMerc:
			self.DeleteEtiquetaXMercaderia()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccEtiquetaxMerc:
			self.SeleccionarEtiquetas()

	def Insert(self):
		self.mReturnValue = "0"
		dmerc = DAMercaderia.DAMercaderia()
		dmerc.mNombreMerc = self.mRequest.get('GMNOM')
		dmerc.mDescripcionMerc = self.mRequest.get('GMDES')
		dmerc.mURLFotoMerc = self.mRequest.get('GMURL')
		dmerc.mTipoMerc = self.mRequest.get('GMTIP')
		dmerc.mkeyTienda = self.mRequest.get('GMKTI')
		dmerc.mkeyContrato = self.mRequest.get('GMKCO')
		dmerc.mkeyDisponibilidad = self.mRequest.get('GMKDI')
		dmerc.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstMerc = []
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DAMercaderia.DAMercaderia.query()
		for recMerc in qry:
			if keyValue != "":
				if str(recMerc.key.id()) == keyValue:
					lstMerc.append(CMercaderia.CMercaderia(str(recMerc.mNombreMerc),str(recMerc.mDescripcionMerc),str(recMerc.mURLFotoMerc),str(recMerc.mTipoMerc),str(recMerc.mKeyTienda),str(recMerc.mKeyContrato),str(recMerc.mKeyDisponibilidad),str(recMerc.key.id())).jsonSerialize())
			else :
				lstMerc.append(CMercaderia.CMercaderia(str(recMerc.mNombreMerc),str(recMerc.mDescripcionMerc),str(recMerc.mURLFotoMerc),str(recMerc.mTipoMerc),str(recMerc.mKeyTienda),str(recMerc.mKeyContrato),str(recMerc.mKeyDisponibilidad),str(recMerc.key.id())).jsonSerialize())
		self.mReturnValue = lstMerc

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GMNOM'))
		descripcionreturnValue = str(self.mRequest.get('GMDES'))
		urlfotoreturnValue = str(self.mRequest.get('GMURL'))
		tiporeturnValue = str(self.mRequest.get('GMTIP'))
		keytiendaValue = str(self.mRequest.get('GMKTI'))
		keycontratoValue = str(self.mRequest.get('GMKCO'))
		keydisponibilidadValue = str(self.mRequest.get('GMKDI'))
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DAMercaderia.DAMercaderia.query()
		# Ejecutar el query
		if keyValue != "":
			for recMercaderia in qry:
				if str(recMercaderia.key.id()) == keyValue:					
					if nombrereturnValue != "":
						recMercaderia.mNombreMercaderia = nombrereturnValue
					if descripcionreturnValue != "":
						recMercaderia.mDescripcionMerc = descripcionreturnValue
					if urlfotoreturnValue != "":
						recMercaderia.mURLFotoMerc = urlfotoreturnValue
					if tiporeturnValue != "":
						recMercaderia.mTipoMerc = tiporeturnValue
					if keytiendaValue != "":
						recMercaderia.mkeyTienda = keytiendaValue
					if keycontratoValue != "":
						recMercaderia.mkeyContrato = keycontratoValue
					if keydisponibilidadValue != "":
						recMercaderia.mkeyDisponibilidad = keydisponibilidadValue
					recMercaderia.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GDKEY'))
		qry = DAMercaderia.DAMercaderia.query()
		if keyValue != "":
			for recMercaderia in qry:
				if str(recMercaderia.key.id()) == keyValue:
					self.mReturnValue = "1"
					recMercaderia.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
	
	#EtiquetaXMercaderia
	def AgregarEtiquetaXMercaderia(self):
		self.mReturnValue = "0"
		keyValueMercaderia = str(self.mRequest.get('GMKEY'))
		KeyetiquetasreturnValue = str(self.mRequest.get('GMKET'))
		daEtiquetaXMercaderia = DAEtiquetaXMercaderia.DAEtiquetaXMercaderia()
		daEtiquetaXMercaderia.mKeyEtiqueta = KeyetiquetasreturnValue
		daEtiquetaXMercaderia.mKeyMercaderia = keyValueMercaderia
		bandera = "0"
		qry = DAEtiquetaXMercaderia.DAEtiquetaXMercaderia.query()
		# Ejecutar el query
		if keyValueMercaderia != "" and KeyetiquetasreturnValue != "":
			for recEtiquetaXMercaderia in qry:
				if str(recEtiquetaXMercaderia.mKeyEtiqueta) == daEtiquetaXMercaderia.mKeyEtiqueta and str(recEtiquetaXMercaderia.mKeyMercaderia) == daEtiquetaXMercaderia.mKeyMercaderia:					
					bandera = "1"
		
		if bandera == "0":
			daEtiquetaXMercaderia.put()
			self.mReturnValue = "1"
			
		
	
	def DeleteEtiquetaXMercaderia(self):
		self.mReturnValue = "0"
		keyValueMercaderia = str(self.mRequest.get('GMKEY'))
		KeyetiquetasreturnValue = str(self.mRequest.get('GMKET'))
		qry = DAEtiquetaXMercaderia.DAEtiquetaXMercaderia.query()
		if keyValueMercaderia != "" and KeyetiquetasreturnValue != "":
			for recEtiquetaXMercaderia in qry:
				if str(recEtiquetaXMercaderia.mKeyEtiqueta) == KeyetiquetasreturnValue and str(recEtiquetaXMercaderia.mKeyMercaderia) == keyValueMercaderia:
					self.mReturnValue = "1"
					recEtiquetaXMercaderia.key.delete()
	
	def SeleccionarEtiquetas(self):
		self.mReturnValue = "0"
		lstEtiqueta = []
		keyValueMercaderia = str(self.mRequest.get('GMKEY'))
		qryEtiquetaXMercaderia= DAEtiquetaXMercaderia.DAEtiquetaXMercaderia.query()
		qryEtiqueta= DAEtiqueta.DAEtiqueta.query()
		if keyValueMercaderia != "":
			for recEtiquetaXMercaderia in qryEtiquetaXMercaderia:
				if str(recEtiquetaXMercaderia.mKeyMercaderia) == keyValueMercaderia:					
					for recEtiqueta in qryEtiqueta:
							if str(recEtiqueta.key.id()) == str(recEtiquetaXMercaderia.mKeyEtiqueta):
								lstEtiqueta.append(CEtiqueta.CEtiqueta(str(recEtiqueta.mNombreEtiqueta),str(recEtiqueta.key.id())).jsonSerialize())
			self.mReturnValue = lstEtiqueta