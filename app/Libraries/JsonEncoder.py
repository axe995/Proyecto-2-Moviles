# coding: utf-8

#Proyecto 2
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import json

class JsonEncoder(json.JSONEncoder):

	def default(self, pObject):
		return pObject.__dict__

	def serializeJson(self,pObject):
		serialize = json.dumps(pObject, cls=JsonEncoder, indent=4)
		return serialize