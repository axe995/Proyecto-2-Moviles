# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CDisponibilidad:
        def __init__(self, pTipoDisponibilidad="", pKeyValue=""):
		self.mTipoDisponibilidad = ""
		self.mKeyValue = ""
		if type(pTipoDisponibilidad) is str:
			self.mTipoDisponibilidad = pTipoDisponibilidad
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

	def setTipoDisponibilidad(self, pTipoDisponibilidad=""):
		if type(pTipoDisponibilidad) is str:
			self.mTipoDisponibilidad = pTipoDisponibilidad

	def getTipoDisponibilidad(self):
		return self.mTipoDisponibilidad

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
