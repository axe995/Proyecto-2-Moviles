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
from datetime import datetime
from google.appengine.ext import ndb
import Constantes
import DMenu
import DPlatillo
import DPlaXMenu
import CMenu
import CPlatillo

#Gestion Menu Control
class GMenuCtrl:
	def __init__(self,pRequest):
		self.mRequest = pRequest
		self.mOperation = ""
		self.mNombreMenu = ""
		self.mDescripcion = ""
		self.mFechaInicioAplicacion = ""
		self.mFechaFinalAplicacion = ""
		self.mEstadoAplicacion = ""
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
		if self.mOperation == Constantes.Constantes().mGMOperacionAcivar:
			self.Activar()
		if self.mOperation == Constantes.Constantes().mGMOperacionDesact:
			self.Desactivar()
		if self.mOperation == Constantes.Constantes().mGMOperacionAgregaPla:
			self.AgregarPlatillo()
		if self.mOperation == Constantes.Constantes().mGMOperacionBorrarPla:
			self.BorrarPlatillo()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccPla:
			self.SeleccionarPlatillos()
		if self.mOperation == Constantes.Constantes().mGMOperacionSeleccMen:
			self.SeleccionarMenuDelDia()


	def Insert(self):
		self.mReturnValue = "0"
		dmenu = DMenu.DMenu()
		dmenu.mNombreMenu = self.mRequest.get('GMNOM')
		dmenu.mDescripcion = self.mRequest.get('GMDSC')
		dmenu.mFechaInicioAplicacion = self.mRequest.get('GMFIA')
		dmenu.mFechaFinalAplicacion = self.mRequest.get('GMFFA')
		dmenu.mEstadoAplicacion = Constantes.Constantes().mGMEstadoInactivo
		dmenu.put()
		self.mReturnValue = "1"
		
		

	def Select(self):
		lstMenus = []
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DMenu.DMenu.query()
		for recMenu in qry:
			if keyValue != "":
				if str(recMenu.key.id()) == keyValue:
					lstMenus.append(CMenu.CMenu(str(recMenu.mNombreMenu),str(recMenu.mDescripcion),str(recMenu.mFechaInicioAplicacion),str(recMenu.mFechaFinalAplicacion),str(recMenu.mEstadoAplicacion),str(recMenu.key.id())).jsonSerialize())
			else :
				lstMenus.append(CMenu.CMenu(str(recMenu.mNombreMenu),str(recMenu.mDescripcion),str(recMenu.mFechaInicioAplicacion),str(recMenu.mFechaFinalAplicacion),str(recMenu.mEstadoAplicacion),str(recMenu.key.id())).jsonSerialize())
		self.mReturnValue = lstMenus

	def Update(self):
		# Obtener los parametros para poder actualizarlos
		self.mReturnValue = "0"
		nombreValue = str(self.mRequest.get('GMNOM'))
		descripcionValue = str(self.mRequest.get('GMDSC'))
		fechaInicioAplicacionValue = self.mRequest.get('GMFIA')
		fechaFinalAPlicacionValue = self.mRequest.get('GMFFA')
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DMenu.DMenu.query()
		# Ejecutar el query
		if keyValue != "":
			for recMenu in qry:
				if str(recMenu.key.id()) == keyValue:					
					if nombreValue != "":
						recMenu.mNombreMenu = nombreValue
					if descripcionValue != "":
						recMenu.mDescripcion = descripcionValue
					if fechaInicioAplicacionValue != "":
						recMenu.mFechaInicioAplicacion = fechaInicioAplicacionValue
					if fechaFinalAPlicacionValue != "":
						recMenu.mFechaFinalAplicacion = fechaFinalAPlicacionValue
					recMenu.put()
					self.mReturnValue = "1"
		

	def Delete(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DMenu.DMenu.query()
		if keyValue != "":
			for recMenu in qry:
				if str(recMenu.key.id()) == keyValue:
					self.mReturnValue = "1"
					recMenu.key.delete()
	

	def Activar(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DMenu.DMenu.query()
		if keyValue != "":
			for recMenu in qry:
				if str(recMenu.key.id()) == keyValue:
					recMenu.mEstadoAplicacion = Constantes.Constantes().mGMEstadoActivo
					recMenu.put()
					self.mReturnValue = "1"

	def Desactivar(self):
		self.mReturnValue = "0"
		keyValue = str(self.mRequest.get('GMKEY'))
		qry = DMenu.DMenu.query()
		if keyValue != "":
			for recMenu in qry:
				self.mReturnValue = "Entro al loop"
				if str(recMenu.key.id()) == keyValue:
					recMenu.mEstadoAplicacion = Constantes.Constantes().mGMEstadoInactivo
					recMenu.put()
					self.mReturnValue = "1"

	def AgregarPlatillo(self):
		self.mReturnValue = "0"
		keyMenuValue = str(self.mRequest.get('GMKEY'))
		keyPlatilloValue = str(self.mRequest.get('GPKEY'))
		dplaxmenu = DPlaXMenu.DPlaXMenu()
		dplaxmenu.mKeyMenu = keyMenuValue
		dplaxmenu.mKeyPlatillo = keyPlatilloValue
		dplaxmenu.put()
		self.mReturnValue = "1"

	def BorrarPlatillo(self):
		self.mReturnValue = "0"
		keyMenuValue = str(self.mRequest.get('GMKEY'))
		keyPlatilloValue = str(self.mRequest.get('GPKEY'))
		qry = DPlaXMenu.DPlaXMenu.query()
		if keyMenuValue != "" and keyPlatilloValue != "":
			for recMenu in qry:
				if str(recMenu.mKeyMenu) == keyMenuValue and str(recMenu.mKeyPlatillo) == keyPlatilloValue:
					self.mReturnValue = "1"
					recMenu.key.delete()

	def SeleccionarPlatillos(self):
		self.mReturnValue = "0"
		lstPlatillos = []
		keyMenuValue = str(self.mRequest.get('GMKEY'))
		qryMenu = DPlaXMenu.DPlaXMenu.query()
		qryPlatillo = DPlatillo.DPlatillo.query()
		for recMenu in qryMenu:
			if str(recMenu.mKeyMenu) == keyMenuValue:					
				for recPlatillo in qryPlatillo:
					if str(recPlatillo.key.id()) == str(recMenu.mKeyPlatillo):
						lstPlatillos.append(CPlatillo.CPlatillo(str(recPlatillo.mNombrePlatillo),str(recPlatillo.mPrecio),str(recPlatillo.key.id())).jsonSerialize())
		self.mReturnValue = lstPlatillos

	def SeleccionarMenuDelDia(self):
		self.mReturnValue = "0"
		lstMenus = []
		qryMenu = DMenu.DMenu.query()
		for recMenu in qryMenu:
			strActivo = recMenu.mEstadoAplicacion
			dateDMenuFIA = datetime.strptime(recMenu.mFechaInicioAplicacion, "%Y%m%d").date()
			dateDMenuFFA = datetime.strptime(recMenu.mFechaFinalAplicacion,"%Y%m%d").date()
			dateToday = datetime.today().date()
			if strActivo == Constantes.Constantes().mGMEstadoActivo:
				if dateToday < dateDMenuFFA and dateToday >= dateDMenuFIA:
					lstMenus.append(CMenu.CMenu(str(recMenu.mNombreMenu),str(recMenu.mDescripcion),str(recMenu.mFechaInicioAplicacion),str(recMenu.mFechaFinalAplicacion),str(recMenu.mEstadoAplicacion),str(recMenu.key.id())).jsonSerialize())
		self.mReturnValue = lstMenus


	def GetValue(self):
		return self.mReturnValue