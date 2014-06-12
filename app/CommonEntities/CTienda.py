# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CTienda:
        def __init__(self, pNombreTienda="", pDescripcionTienda="", pURLFotoTienda="", pLongitud="", pLatitud="", pHorarioTienda="", pKeyDuenoTienda="", pKeyValue=""):
		self.mNombreTienda = ""
		self.mDescripcionTienda = ""
		self.mURLFotoTienda = ""
		self.mLongitud = ""
		self.mLatitud = ""
		self.mHorarioTienda = ""
		self.mKeyDuenoTienda = ""
		self.mKeyValue = ""
		if type(pNombreTienda) is str:
			self.mNombreTienda = pNombreTienda
		if type(pDescripcionTienda) is str:
			self.mDescripcionTienda = pDescripcionTienda
		if type(pURLFotoTienda) is str:
			self.mURLFotoTienda = pURLFotoTienda
		if type(pLongitud) is str:
			self.mLongitud = pLongitud
		if type(pLatitud) is str:
			self.mLatitud = pLatitud
		if type(pHorarioTienda) is str:
			self.mHorarioTienda = pHorarioTienda
		if type(pKeyDuenoTienda) is str:
			self.mKeyDuenoTienda = pKeyDuenoTienda
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

	def setNombreTienda(self, pNombreTienda=""):
		if type(pNombreTienda) is str:
			self.mNombreTienda = pNombreTienda

	def setDescripcionTienda(self, pDescripcionTienda = ""):
		if type(pDescripcionTienda) is str:
			self.mDescripcionTienda = pDescripcionTienda
			
	def setURLFotoTienda(self, pURLFotoTienda = ""):
		if type(pURLFotoTienda) is str:
			self.mURLFotoTienda = pURLFotoTienda
			
	def setLongitud(self, pLongitud = ""):
		if type(pLongitud) is str:
			self.mLongitud = pLongitud
			
	def setHorarioTienda(self, pHorarioTienda = ""):
		if type(pHorarioTienda) is str:
			self.mHorarioTienda = pHorarioTienda
			
	def setKeyDuenoTienda(self, pKeyDuenoTienda = ""):
		if type(pKeyDuenoTienda) is str:
			self.mKeyDuenoTienda = pKeyDuenoTienda

	def getNombreTienda(self):
		return self.mNombreTienda

	def getDescripcionTienda(self):
		return self.mDescripcionTienda
		
	def getURLFotoTienda(self):
		return self.mURLFotoTienda
		
	def getLongitud(self):
		return self.mLongitud
		
	def getHorarioTienda(self):
		return self.mHorarioTienda
		
	def getKeyDuenoTienda(self):
		return self.mKeyDuenoTienda

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
