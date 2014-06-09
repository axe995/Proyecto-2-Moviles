# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CEtiqueta:
    def __init__(self, pNombreEtiqueta="", pKeyValue=""):
		self.mNombreEtiqueta = ""
		self.mKeyValue = ""
		if type(pNombreEtiqueta) is str:
			self.mNombreEtiqueta = pNombreEtiqueta
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

	def setNombreEtiqueta(self, pNombreEtiqueta=""):
		if type(pNombreEtiqueta) is str:
			self.mNombreEtiqueta = pNombreEtiqueta

	def getNombreEtiqueta(self):
		return self.mNombreEtiqueta

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)