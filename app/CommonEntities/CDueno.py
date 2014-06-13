# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Libraries'))
import JsonEncoder

class CDueno:
        def __init__(self, pNombreDueno="", pCorreoDueno="", pResidenciaDueno="", pDescripcionDueno="", pKeyAlbumProductos="", pKeyAlbumServicios="", pKeyValue=""):
		self.mNombreDueno = ""
		self.mCorreoDueno = ""
		self.mResidenciaDueno = ""
		self.mDescripcionDueno = ""
		self.mKeyAlbumProductos = ""
		self.mKeyAlbumServicios = ""
		self.mKeyValue = ""
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
		if type(pKeyAlbumProductos) is str:
			self.mKeyAlbumProductos = pKeyAlbumProductos
		if type(pKeyAlbumServicios) is str:
			self.mKeyAlbumServicios = pKeyAlbumServicios
		if type(pNombreDueno) is str:
			self.mNombreDueno = pNombreDueno
		if type(pCorreoDueno) is str:
			self.mCorreoDueno = pCorreoDueno
		if type(pResidenciaDueno) is str:
			self.mResidenciaDueno = pResidenciaDueno
		if type(pDescripcionDueno) is str:
			self.mDescripcionDueno = pDescripcionDueno

			#Setters y Getters
	def setKeyValue(self,pKeyValue):
		if type(pKeyValue) is str:
			self.mKeyValue = pKeyValue
			
	def setNombreDueno(self, pNombreDueno=""):
		if type(pNombreDueno) is str:
			self.mNombreDueno = pNombreDueno
			
	def setCorreoDueno(self, pCorreoDueno=""):
                if type(pCorreoDueno) is str:
			self.mCorreoDueno = pCorreoDueno

        def setResidenciaDueno(self, pResidenciaDueno=""):
                if type(pResidenciaDueno) is str:
			self.mResidenciaDueno = pResidenciaDueno

        def setDescripcionDueno(self, pDescripcionDueno=""):
                if type(pDescripcionDueno) is str:
			self.mDescripcionDueno = pDescripcionDueno

	def getNombreDueno(self):
		return self.mNombreDueno

	def getCorreoDueno(self):
		return self.mCorreoDueno

	def getResidenciaDueno(self):
		return self.mResidenciaDueno

	def getDescripcionDueno(self):
		return self.mDescripcionDueno
        

	def jsonSerialize(self):
		return JsonEncoder.JsonEncoder().serializeJson(self)
