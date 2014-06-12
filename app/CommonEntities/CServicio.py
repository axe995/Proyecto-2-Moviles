# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CServicio:
    def __init__(self, pPrecioContrato="", pFechaInicioContrato="", pFechaLiberacionContrato="", pKeyMerc="", pKeyValue=""):
		self.mPrecioContrato = ""
		self.mFechaInicioContrato = ""
		self.mFechaLiberacionContrato = ""
		self.mKeyMerc = ""
		self.mKeyValue = ""
		if type(pPrecioContrato) is str:
			self.mPrecioContrato = pPrecioContrato
		if type(pFechaInicioContrato) is str:
			self.mFechaInicioContrato = pFechaInicioContrato
		if type(pFechaLiberacionContrato) is str:
			self.mFechaLiberacionContrato = pFechaLiberacionContrato
		if type(pKeyMerc) is str:
			self.mKeyMerc = pKeyMerc
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
			
	def setKeyMerc(self,pKeyMerc):
		if type(pKeyMerc) is str:
			self.mKeyMerc = pKeyMerc

	def setPrecioContrato(self, pPrecioContrato=""):
		if type(pPrecioContrato) is str:
			self.mPrecioContrato = pPrecioContrato

	def setFechaInicioContrato(self, pFechaInicioContrato = ""):
		if type(pFechaInicioContrato) is str:
			self.mFechaInicioContrato = pFechaInicioContrato
			
	def setFechaLiberacionContrato(self, pFechaLiberacionContrato = ""):
		if type(pFechaLiberacionContrato) is str:
			self.mFechaLiberacionContrato = pFechaLiberacionContrato
			
	def getPrecioContrato(self):
		return self.mPrecioContrato

	def getFechaInicioContrato(self):
		return self.mFechaInicioContrato
		
	def getFechaLiberacionContrato(self):
		return self.mFechaLiberacionContrato

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)