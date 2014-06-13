# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CTipoContacto:
        def __init__(self, pNombreTipoC="", pKeyValue=""):
		self.mNombreTipoC = ""
		self.mKeyValue = ""
		if type(pNombreTipoC) is str:
			self.mNombreTipoC = pNombreTipoC
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

	def setNombreTipoC(self, pNombreTipoC=""):
		if type(pNombreTipoC) is str:
			self.mNombreTipoC = pNombreTipoC

	def getNombreTipoC(self):
		return self.mNombreTipoC

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
