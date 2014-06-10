# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CContrato:
    def __init__(self, pTipoContrato="", pKeyValue=""):
		self.mTipoContrato = ""
		self.mKeyValue = ""
		if type(pTipoContrato) is str:
			self.mTipoContrato = pTipoContrato
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
		
	def setTipoContrato(self, pTipoContrato = ""):
		if type(pTipoContrato) is str:
			self.mTipoContrato = pTipoContrato
		
	def getTipoContrato(self):
		return self.mTipoContrato

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)