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
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateMerc:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarMerc:
			self.Delete()
			

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