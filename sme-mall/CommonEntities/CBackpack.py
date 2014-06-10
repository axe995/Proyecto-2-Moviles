# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CBackpack:
    def __init__(self, pKeyCliente="", pKeyValue=""):
		self.mKeyCliente = ""
		self.mKeyValue = ""
		
		if type(pKeyCliente) is str:
			self.mKeyCliente = pKeyCliente
		
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
			
	def setKeyCliente(self,pKeyCliente):
		if type(pKeyCliente) is str:
			self.mKeyCliente = pKeyCliente

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)