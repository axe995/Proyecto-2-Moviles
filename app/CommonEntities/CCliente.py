# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CCliente:
        def __init__(self, pNombreCliente="", pCorreoCliente="", pUltimaFechaActividad="", pKeyValue=""):
		self.mNombreCliente = ""
		self.mCorreoCliente = ""
		self.mUltimaFechaActividad = ""
		self.mKeyValue = ""
		if type(pNombreCliente) is str:
			self.mNombreCliente = pNombreCliente
		if type(pCorreoCliente) is str:
			self.mCorreoCliente = pCorreoCliente
		if type(pUltimaFechaActividad) is str:
			self.mUltimaFechaActividad = pUltimaFechaActividad
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue

	def setNombreCliente(self, pNombreCliente=""):
		if type(pNombreCliente) is str:
			self.mNombreCliente = pNombreCliente

	def setCorreoCliente(self, pCorreoCliente = ""):
		if type(pCorreoCliente) is str:
			self.mCorreoCliente = pCorreoCliente
			
	def setUltimaFechaActividad(self, pUltimaFechaActividad = ""):
		if type(pUltimaFechaActividad) is str:
			self.mUltimaFechaActividad = pUltimaFechaActividad

	def getNombreCliente(self):
		return self.mNombreCliente

	def getCorreoCliente(self):
		return self.mCorreoCliente
		
	def getUltimaFechaActividad(self):
		return self.mUltimaFechaActividad

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
