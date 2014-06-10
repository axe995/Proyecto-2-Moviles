# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CMercaderia:
    def __init__(self, pNombreMerc="", pDescripcionMerc="", pURLFotoMerc="", pTipoMerc="", pKeyTienda="", pKeyContrato="", pKeyDisponibilidad="", pKeyValue=""):
		self.mNombreMerc = ""
		self.mDescripcionMerc = ""
		self.mURLFotoMerc = ""
		self.mTipoMerc = ""
		self.mKeyValue = ""
		if type(pNombreMerc) is str:
			self.mNombreMerc = pNombreMerc
		if type(pDescripcionMerc) is str:
			self.mDescripcionMerc = pDescripcionMerc
		if type(pURLFotoMerc) is str:
			self.mURLFotoMerc = pURLFotoMerc
		if type(pTipoMerc) is str:
			self.mTipoMerc = pTipoMerc
		if type(pKeyTienda) is str:
			self.mKeyTienda = pKeyTienda
		if type(pKeyContrato) is str:
			self.mKeyContrato = pKeyContrato
		if type(pKeyDisponibilidad) is str:
			self.mKeyDisponibilidad = pKeyDisponibilidad
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
			
	def setKeyTienda(self,pKeyTienda):
		if type(pKeyTienda) is str:
			self.mKeyTienda = pKeyTienda
			
	def setKeyContrato(self,pKeyContrato):
		if type(pKeyContrato) is str:
			self.mKeyContrato = pKeyContrato
			
	def setKeyDisponibilidad(self,pKeyDisponibilidad):
		if type(pKeyDisponibilidad) is str:
			self.mKeyDisponibilidad = pKeyDisponibilidad

	def setNombreMerc(self, pNombreMerc=""):
		if type(pNombreMerc) is str:
			self.mNombreMerc = pNombreMerc

	def setDescripcionMerc(self, pDescripcionMerc = ""):
		if type(pDescripcionMerc) is str:
			self.mDescripcionMerc = pDescripcionMerc
			
	def setURLFotoMerc(self, pURLFotoMerc = ""):
		if type(pURLFotoMerc) is str:
			self.mURLFotoMerc = pURLFotoMerc
			
	def setTipoMerc(self, pTipoMerc = ""):
		if type(pTipoMerc) is str:
			self.mTipoMerc = pTipoMerc

	def getNombreMerc(self):
		return self.mNombreMerc

	def getDescripcionMerc(self):
		return self.mDescripcionMerc
		
	def getURLFotoMerc(self):
		return self.mURLFotoMerc
		
	def getTipoMerc(self):
		return self.mTipoMerc

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)