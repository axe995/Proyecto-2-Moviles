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
    def __init__(self, pNombreTienda="", pDescripcionTienda="", pURLFotoTienda="", pUbicacionTienda="", pHorarioTienda="", pDuenoTienda="", pKeyValue=""):
		self.mNombreTienda = ""
		self.mDescripcionTienda = ""
		self.mURLFotoTienda = ""
		self.mUbicacionTienda = ""
		self.mHorarioTienda = ""
		self.mDuenoTienda = ""
		self.mKeyValue = ""
		if type(pNombreTienda) is str:
			self.mNombreTienda = pNombreTienda
		if type(pDescripcionTienda) is str:
			self.mDescripcionTienda = pDescripcionTienda
		if type(pURLFotoTienda) is str:
			self.mURLFotoTienda = pURLFotoTienda
		if type(pUbicacionTienda) is str:
			self.mUbicacionTienda = pUbicacionTienda
		if type(pHorarioTienda) is str:
			self.mHorarioTienda = pHorarioTienda
		if type(pDuenoTienda) is str:
			self.mDuenoTienda = pDuenoTienda
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
			
	def setUbicacionTienda(self, pUbicacionTienda = ""):
		if type(pUbicacionTienda) is str:
			self.mUbicacionTienda = pUbicacionTienda
			
	def setHorarioTienda(self, pHorarioTienda = ""):
		if type(pHorarioTienda) is str:
			self.mHorarioTienda = pHorarioTienda
			
	def setDuenoTienda(self, pDuenoTienda = ""):
		if type(pDuenoTienda) is str:
			self.mDuenoTienda = pDuenoTienda

	def getNombreTienda(self):
		return self.mNombreTienda

	def getDescripcionTienda(self):
		return self.mDescripcionTienda
		
	def getURLFotoTienda(self):
		return self.mURLFotoTienda
		
	def getUbicacionTienda(self):
		return self.mUbicacionTienda
		
	def getHorarioTienda(self):
		return self.mHorarioTienda
		
	def getDuenoTienda(self):
		return self.mDuenoTienda

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)