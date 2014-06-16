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
import DADueno
import CDueno
import DATienda
import CTienda

#Gestion Dueño Control
class GDuenoCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreDueno = ""
		self.mCorreoDueno = ""
		self.mResidenciaDueno = ""
		self.mDescripcionDueno = ""
		self.mkeyAlbumProductos = ""
		self.mkeyAlbumServicios = ""
		self.mkeyValue = ""
		self.mReturnValue = []

	def Execute(self):
		self.mOperation = str(self.mRequest.get("EXECOP"))
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccDueno:
			self.Select()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccDueno2:
			self.Select2()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaDueno:
			self.Insert()
		if self.mOperation == Constantes.Constantes().mGPOperacionUpdateDueno:
			self.Update()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarDueno:
			self.Delete()


	def Insert(self):
		self.mReturnValue = "0"
		ddueno = DADueno.DADueno()
		ddueno.mNombreDueno = self.mRequest.get('GDNOM')
		ddueno.mCorreoDueno = self.mRequest.get('GDCOR')
		ddueno.mResidenciaDueno = self.mRequest.get('GDRES')
		ddueno.mDescripcionDueno = self.mRequest.get('GDDES')
		ddueno.mkeyAlbumProductos = self.mRequest.get('GDALP')
		ddueno.mkeyAlbumServicios = self.mRequest.get('GDALS')
		bandera = "0"
		qry = DADueno.DADueno.query()
		# Ejecutar el query
		if ddueno.mCorreoDueno != "":
			for recDueno in qry:
				if str(recDueno.mCorreoDueno) == ddueno.mCorreoDueno:					
					bandera = "1"
		
		if bandera == "0":
			llave = ddueno.put()
			dtienda = DATienda.DATienda()
			dtienda.mKeyDuenoTienda = str(llave.id())
			dtienda.put()
			self.mReturnValue = "1"
		
		

	def Select(self):
		lstDueno = []
		keyValue = str(self.mRequest.get('GDKEY'))
		qry = DADueno.DADueno.query()
		for recDueno in qry:
			if keyValue != "":
				if str(recDueno.mCorreoDueno) == keyValue:
					lstDueno.append(CDueno.CDueno(str(recDueno.mNombreDueno),str(recDueno.mCorreoDueno),str(recDueno.mResidenciaDueno),str(recDueno.mDescripcionDueno),str(recDueno.mKeyAlbumProductos),str(recDueno.mKeyAlbumServicios),str(recDueno.key.id())).jsonSerialize())
			else :
				lstDueno.append(CDueno.CDueno(str(recDueno.mNombreDueno),str(recDueno.mCorreoDueno),str(recDueno.mResidenciaDueno),str(recDueno.mDescripcionDueno),str(recDueno.mKeyAlbumProductos),str(recDueno.mKeyAlbumServicios),str(recDueno.key.id())).jsonSerialize())
		self.mReturnValue = lstDueno

	def Select2(self):
		lstDueno = []
		keyValue = str(self.mRequest.get('GDKEY'))
		qry = DADueno.DADueno.query()
		for recDueno in qry:
			if keyValue != "":
				if str(recDueno.key.id()) == keyValue:
					lstDueno.append(CDueno.CDueno(str(recDueno.mNombreDueno),str(recDueno.mCorreoDueno),str(recDueno.mResidenciaDueno),str(recDueno.mDescripcionDueno),str(recDueno.mKeyAlbumProductos),str(recDueno.mKeyAlbumServicios),str(recDueno.key.id())).jsonSerialize())
			else :
				lstDueno.append(CDueno.CDueno(str(recDueno.mNombreDueno),str(recDueno.mCorreoDueno),str(recDueno.mResidenciaDueno),str(recDueno.mDescripcionDueno),str(recDueno.mKeyAlbumProductos),str(recDueno.mKeyAlbumServicios),str(recDueno.key.id())).jsonSerialize())
		self.mReturnValue = lstDueno

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombrereturnValue = str(self.mRequest.get('GDNOM'))
		correoreturnValue = str(self.mRequest.get('GDCOR'))
		residenciareturnValue = str(self.mRequest.get('GDRES'))
		descripcionreturnValue = str(self.mRequest.get('GDDES'))
		keyAlbumProductoValue = str(self.mRequest.get('GDALP'))
		keyAlbumServicioValue = str(self.mRequest.get('GDALS'))
		keyValue = str(self.mRequest.get('GDKEY'))
		qry = DADueno.DADueno.query()
		# Ejecutar el query
		if keyValue != "":
			for recDueno in qry:
				if str(recDueno.mCorreoDueno) == keyValue:					
					if nombrereturnValue != "":
						recDueno.mNombreDueno = nombrereturnValue
					if correoreturnValue != "":
						recDueno.mCorreoDueno = correoreturnValue
					if residenciareturnValue != "":
						recDueno.mResidenciaDueno = residenciareturnValue
					if descripcionreturnValue != "":
						recDueno.mDescripcionDueno = descripcionreturnValue
					if keyAlbumProductoValue != "":
						recDueno.mkeyAlbumProductos = keyAlbumProductoValue
					if keyAlbumServicioValue != "":
						recDueno.mkeyAlbumServicios = keyAlbumServicioValue
					recDueno.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GDKEY'))
		qry = DADueno.DADueno.query()
		if keyValue != "":
			for recDueno in qry:
				if str(recDueno.key.id()) == keyValue:
					self.mReturnValue = "1"
					recDueno.key.delete()
		

	def GetValue(self):
		return self.mReturnValue
