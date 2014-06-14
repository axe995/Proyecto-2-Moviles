# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CContactoxTienda:
        def __init__(self, pValorC="", pKeyTienda="", pKeyTipoC="",pTipo="", pKeyValue=""):
		self.mValorC = ""
		self.mKeyTienda = ""
		self.mKeyTipoC = ""
		self.mKeyValue = ""
		self.mTipo = ""
		if type(pValorC) is str:
			self.mValorC = pValorC
		if type(pKeyTienda) is str:
			self.mKeyTienda = pKeyTienda
		if type(pKeyTipoC) is str:
			self.mKeyTipoC = pKeyTipoC
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
		if type(pTipo) is str:
			self.mTipo = pTipo

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
			
	def setKeyTienda(self,pKeyTienda):
		if type(pKeyTienda) is str:
			self.mKeyTienda = pKeyTienda
			
	def setKeyTipoC(self,pKeyTipoC):
		if type(pKeyTipoC) is str:
			self.mKeyTipoC = pKeyTipoC
		
	def setValorC(self, pValorC=""):
		if type(pValorC) is str:
			self.mValorC = pValorC

	def getValorC(self):
		return self.mValorC

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
