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
import DABackpack
import CBackpack
import DATiendaXBackpack
import DATienda
import CTienda
import DAMercaderia
import CMercaderia
import DAMercaderiaXBackpack
import DAEtiqueta
import CEtiqueta
import DAEtiquetaXBackpack

#Gestion Dueño Control
class GBackpackCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mKeyCliente = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccBackpack:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaBackpack:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateBackpack:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarBackpack:
			self.Delete()
		#tienda por backpack
		if self.mOperation == Constantes.Constantes().mGPOperacionAgregarTiendaxBackpack:
			self.AgregarTiendaxBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionBorrarTiendaxBackpack:
			self.DeleteTiendaxBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionSeleccTiendaxBackpack:
			self.SeleccionarTiendas()
		#mercaderia por backpack
		if self.mOperation == Constantes.Constantes().mGPOperacionAgregarMercxBackpack:
			self.AgregarMercaderiaXBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionBorrarMercxBackpack:
			self.DeleteMercaderiaXBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionSeleccMercxBackpack:
			self.SeleccionarMercaderia()
		#etiquetas por backpack
		if self.mOperation == Constantes.Constantes().mGPOperacionAgregarEtiquetaxBackpack:
			self.AgregarEtiquetaXBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionBorrarEtiquetaxBackpack:
			self.DeleteEtiquetaXBackpack()
		if self.mOperation == Constantes.Constantes().mGPOperacionSeleccEtiquetaxBackpack:
			self.SeleccionarEtiquetas()


	def Insert(self):
		self.mReturnValue = "0"
		dbackpack = DABackpack.DABackpack()
		dbackpack.mKeyCliente = self.mRequest.get('GBPKCL')
		dbackpack.put()
		self.mReturnValue = "1" 
		
		

	def Select(self):
		lstBackpack = []
		keyValue = str(self.mRequest.get('GBPKEY'))
		qry = DABackpack.DABackpack.query()
		for recBackpack in qry:
			if keyValue != "":
				if str(recBackpack.key.id()) == keyValue:
					lstBackpack.append(CBackpack.CBackpack(str(recBackpack.mKeyCliente),str(recBackpack.key.id())).jsonSerialize())
			else :
				lstBackpack.append(CBackpack.CBackpack(str(recBackpack.mKeyCliente),str(recBackpack.key.id())).jsonSerialize())
		self.mReturnValue = lstBackpack

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		llaveclientereturnValue = str(self.mRequest.get('GBPKCL'))
		keyValue = str(self.mRequest.get('GBPKEY'))
		qry = DABackpack.DABackpack.query()
		# Ejecutar el query
		if keyValue != "":
			for recBackpack in qry:
				if str(recBackpack.key.id()) == keyValue:					
					if llaveclientereturnValue != "":
						recBackpack.mKeyCliente = llaveclientereturnValue
					recBackpack.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GBPKEY'))
		qry = DABackpack.DABackpack.query()
		if keyValue != "":
			for recBackpack in qry:
				if str(recBackpack.key.id()) == keyValue:
					self.mReturnValue = "1"
					recBackpack.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
	
	#TiendaxBackpack
	def AgregarTiendaxBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeytiendareturnValue = str(self.mRequest.get('GBPKTI'))
		daTiendaxBackpack = DATiendaXBackpack.DATiendaXBackpack()
		daTiendaxBackpack.mKeyTienda = KeytiendareturnValue
		daTiendaxBackpack.mKeyBackpack = keyValuebackpack
		bandera = "0"
		qry = DATiendaXBackpack.DATiendaXBackpack.query()
		# Ejecutar el query
		if keyValuebackpack != "" and KeytiendareturnValue != "":
			for recTiendaXBackpack in qry:
				if str(recTiendaXBackpack.mKeyTienda) == daTiendaxBackpack.mKeyTienda and str(recTiendaXBackpack.mKeyBackpack) == daTiendaxBackpack.mKeyBackpack:					
					bandera = "1"
		
		if bandera == "0":
			daTiendaxBackpack.put()
			self.mReturnValue = "1"
			
		
	
	def DeleteTiendaxBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeytiendareturnValue = str(self.mRequest.get('GBPKTI'))
		qry = DATiendaXBackpack.DATiendaXBackpack.query()
		if keyValuebackpack != "" and KeytiendareturnValue != "":
			for recBackpack in qry:
				if str(recBackpack.mKeyTienda) == KeytiendareturnValue and str(recBackpack.mKeyBackpack) == keyValuebackpack:
					self.mReturnValue = "1"
					recBackpack.key.delete()
	
	def SeleccionarTiendas(self):
		self.mReturnValue = "0"
		lstTiendas = []
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		qryBackpack= DATiendaXBackpack.DATiendaXBackpack.query()
		qryTienda= DATienda.DATienda.query()
		if keyValuebackpack != "":
			for recTiendaXBackpack in qryBackpack:
				if str(recTiendaXBackpack.mKeyBackpack) == keyValuebackpack:					
					for recTienda in qryTienda:
							if str(recTienda.key.id()) == str(recTiendaXBackpack.mKeyTienda):
								lstTiendas.append(CTienda.CTienda(str(recTienda.mNombreTienda),str(recTienda.mDescripcionTienda),str(recTienda.mURLFotoTienda),str(recTienda.mLongitud),str(recTienda.mLatitud),str(recTienda.mHorarioTienda),str(recTienda.mKeyDuenoTienda),str(recTienda.key.id())).jsonSerialize())
			self.mReturnValue = lstTiendas
		
	#MercaderiaXBackpack
	def AgregarMercaderiaXBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeymercaderiareturnValue = str(self.mRequest.get('GBPKMR'))
		daMercaderiaXBackpack = DAMercaderiaXBackpack.DAMercaderiaXBackpack()
		daMercaderiaXBackpack.mKeyMerc = KeymercaderiareturnValue
		daMercaderiaXBackpack.mKeyBackpack = keyValuebackpack
		bandera = "0"
		qry = DAMercaderiaXBackpack.DAMercaderiaXBackpack.query()
		# Ejecutar el query
		if keyValuebackpack != "" and KeymercaderiareturnValue != "":
			for recMercaderiaXBackpack in qry:
				if str(recMercaderiaXBackpack.mKeyMerc) == daMercaderiaXBackpack.mKeyMerc and str(recMercaderiaXBackpack.mKeyBackpack) == daMercaderiaXBackpack.mKeyBackpack:					
					bandera = "1"
		
		if bandera == "0":
			daMercaderiaXBackpack.put()
			self.mReturnValue = "1"
			
		
	
	def DeleteMercaderiaXBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeymercaderiareturnValue = str(self.mRequest.get('GBPKMR'))
		qry = DAMercaderiaXBackpack.DAMercaderiaXBackpack.query()
		if keyValuebackpack != "" and KeymercaderiareturnValue != "":
			for recBackpack in qry:
				if str(recBackpack.mKeyMerc) == KeymercaderiareturnValue and str(recBackpack.mKeyBackpack) == keyValuebackpack:
					self.mReturnValue = "1"
					recBackpack.key.delete()
	
	def SeleccionarMercaderia(self):
		self.mReturnValue = "0"
		lstMercaderia = []
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		qryBackpack= DAMercaderiaXBackpack.DAMercaderiaXBackpack.query()
		qryMercaderia= DAMercaderia.DAMercaderia.query()
		if keyValuebackpack != "":
			for recMercaderiaXBackpack in qryBackpack:
				if str(recMercaderiaXBackpack.mKeyBackpack) == keyValuebackpack:					
					for recMercaderia in qryMercaderia:
							if str(recMercaderia.key.id()) == str(recMercaderiaXBackpack.mKeyMerc):
								lstMercaderia.append(CMercaderia.CMercaderia(str(recMercaderia.mNombreMerc),str(recMercaderia.mDescripcionMerc),str(recMercaderia.mURLFotoMerc),str(recMercaderia.mTipoMerc),str(recMercaderia.mKeyTienda),str(recMercaderia.mKeyContrato),str(recMercaderia.mKeyDisponibilidad),str(recMercaderia.key.id())).jsonSerialize())
			self.mReturnValue = lstMercaderia
			
		#EtiquetaXBackpack
	def AgregarEtiquetaXBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeyetiquetasreturnValue = str(self.mRequest.get('GBPKET'))
		daEtiquetaXBackpack = DAEtiquetaXBackpack.DAEtiquetaXBackpack()
		daEtiquetaXBackpack.mKeyEtiqueta = KeyetiquetasreturnValue
		daEtiquetaXBackpack.mKeyBackpack = keyValuebackpack
		bandera = "0"
		qry = DAEtiquetaXBackpack.DAEtiquetaXBackpack.query()
		# Ejecutar el query
		if keyValuebackpack != "" and KeyetiquetasreturnValue != "":
			for recEtiquetaXBackpack in qry:
				if str(recEtiquetaXBackpack.mKeyEtiqueta) == daEtiquetaXBackpack.mKeyEtiqueta and str(recEtiquetaXBackpack.mKeyBackpack) == daEtiquetaXBackpack.mKeyBackpack:					
					bandera = "1"
		
		if bandera == "0":
			daEtiquetaXBackpack.put()
			self.mReturnValue = "1"
			
		
	
	def DeleteEtiquetaXBackpack(self):
		self.mReturnValue = "0"
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		KeyetiquetasreturnValue = str(self.mRequest.get('GBPKET'))
		qry = DAEtiquetaXBackpack.DAEtiquetaXBackpack.query()
		if keyValuebackpack != "" and KeyetiquetasreturnValue != "":
			for recBackpack in qry:
				if str(recBackpack.mKeyEtiqueta) == KeyetiquetasreturnValue and str(recBackpack.mKeyBackpack) == keyValuebackpack:
					self.mReturnValue = "1"
					recBackpack.key.delete()
	
	def SeleccionarEtiquetas(self):
		self.mReturnValue = "0"
		lstEtiqueta = []
		keyValuebackpack = str(self.mRequest.get('GBPKEY'))
		qryBackpack= DAEtiquetaXBackpack.DAEtiquetaXBackpack.query()
		qryEtiqueta= DAEtiqueta.DAEtiqueta.query()
		if keyValuebackpack != "":
			for recEtiquetaXBackpack in qryBackpack:
				if str(recEtiquetaXBackpack.mKeyBackpack) == keyValuebackpack:					
					for recEtiqueta in qryEtiqueta:
							if str(recEtiqueta.key.id()) == str(recEtiquetaXBackpack.mKeyEtiqueta):
								lstEtiqueta.append(CEtiqueta.CEtiqueta(str(recEtiqueta.mNombreEtiqueta),str(recEtiqueta.key.id())).jsonSerialize())
			self.mReturnValue = lstEtiqueta