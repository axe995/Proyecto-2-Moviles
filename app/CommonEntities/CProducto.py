# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CProducto:
    def __init__(self, pCantidadDisponibleProd="", pPrecioUnitarioProd="", pFechaDevolucionProd="", pKeyValue=""):
		
		self.mCantidadDisponibleProd = ""
		self.mPrecioUnitarioProd = ""
		self.mFechaDevolucionProd = ""
		self.mKeyMerc = ""
		self.mKeyValue = ""
		if type(pCantidadDisponibleProd) is str:
			self.mCantidadDisponibleProd = pCantidadDisponibleProd
		if type(pPrecioUnitarioProd) is str:
			self.mPrecioUnitarioProd = pPrecioUnitarioProd
		if type(pFechaDevolucionProd) is str:
			self.mFechaDevolucionProd = pFechaDevolucionProd
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

	def setCantidadDisponibleProd(self, pCantidadDisponibleProd=""):
		if type(pCantidadDisponibleProd) is str:
			self.mCantidadDisponibleProd = pCantidadDisponibleProd

	def setPrecioUnitarioProd(self, pPrecioUnitarioProd = ""):
		if type(pPrecioUnitarioProd) is str:
			self.mPrecioUnitarioProd = pPrecioUnitarioProd
			
	def setFechaDevolucionProd(self, pFechaDevolucionProd = ""):
		if type(pFechaDevolucionProd) is str:
			self.mFechaDevolucionProd = pFechaDevolucionProd
			
	def getCantidadDisponibleProd(self):
		return self.mCantidadDisponibleProd

	def getPrecioUnitarioProd(self):
		return self.mPrecioUnitarioProd
		
	def getFechaDevolucionProd(self):
		return self.mFechaDevolucionProd

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)