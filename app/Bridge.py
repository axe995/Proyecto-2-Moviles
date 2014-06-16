# coding: utf-8

#Proyecto 1
#Electiva Desarrollo de Aplicaciones Moviles
#Andres Gonzalez
#David Montero
#Emanuel Avendano

import Business.GClienteCtrl
import Business.GDuenoCtrl
import Business.GEtiquetaCtrl
import Business.GTiendaCtrl
import Business.GContratoCtrl
import Business.GDisponibilidadCtrl
import Business.GTipoContactoCtrl
import Business.GMercaderiaCtrl
import Business.GProductoCtrl
import Business.GServicioCtrl
import Business.GBackpackCtrl
#import Business.GOrdenCtrl
import Libraries.Constantes
import Libraries.JsonEncoder

class Bridge:

	def __init__(self,pRequest):
		self.mOperation = ""
		self.mModuloExec = ""
		self.mRequest = pRequest
		self.mReturnValue = {'RETURNVALUE':""}

	def GetValue(self):
			return self.mReturnValue

	def IniciarEjecucion(self):
		self.mModuloExec = str(self.mRequest.get('MOD'))
		self.mOperation = self.mRequest.get("EXECOP")
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleCliente:
			self.mControl = Business.GClienteCtrl.GClienteCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleDueno:
			self.mControl = Business.GDuenoCtrl.GDuenoCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
                if self.mModuloExec == Libraries.Constantes.Constantes().mModuleEtiqueta:
			self.mControl = Business.GEtiquetaCtrl.GEtiquetaCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleTienda:
			self.mControl = Business.GTiendaCtrl.GTiendaCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleContrato:
			self.mControl = Business.GContratoCtrl.GContratoCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleDisponibilidad:
			self.mControl = Business.GDisponibilidadCtrl.GDisponibilidadCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleTipoContacto:
			self.mControl = Business.GTipoContactoCtrl.GTipoContactoCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleMercaderia:
			self.mControl = Business.GMercaderiaCtrl.GMercaderiaCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleProducto:
			self.mControl = Business.GProductoCtrl.GProductoCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleServicio:
			self.mControl = Business.GServicioCtrl.GServicioCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		if self.mModuloExec == Libraries.Constantes.Constantes().mModuleBackpack:
			self.mControl = Business.GBackpackCtrl.GBackpackCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)
		'''if self.mModuloExec == Libraries.Constantes.Constantes().mModuleOrden:
			self.mControl = Business.GOrdenCtrl.GOrdenCtrl(self.mRequest)
			self.mControl.mOperation = self.mOperation
			self.mControl.Execute()
			self.mReturnValue['RETURNVALUE'] = self.mControl.GetValue()
			self.mReturnValue = Libraries.JsonEncoder.JsonEncoder().serializeJson(self.mReturnValue)'''
