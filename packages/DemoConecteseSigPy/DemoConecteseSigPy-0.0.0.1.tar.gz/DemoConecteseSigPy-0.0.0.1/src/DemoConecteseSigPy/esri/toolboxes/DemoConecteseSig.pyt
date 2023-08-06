# -*- coding: utf-8 -*-
import arcpy

from DemoConecteseSigPy.Utiles import ARCGIS_HANDLER
from DemoConecteseSigPy.Herramientas import Procesos

class Toolbox(object):
    
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Demo Conéctese con SIG Python"
        self.alias = "DemoConecteseSigPy"
        
        # List of tool classes associated with this toolbox
        self.tools = [ActualizarFechas]

class ActualizarFechas(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Actualizar Fecha Actual"
        self.description = "Actualizar campo de fecha a la fecha actual"
        self.alias = "ActualizarFechaActual"
        
        self.canRunInBackground = True
        self.Params = {"portal": 0, 
                        "usuario": 1, 
                        "clave": 2, 
                        "servicio": 3, 
                        "tabla": 4,
                        "campo": 5}

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        param = arcpy.Parameter(
            displayName="URL del Portal",
            name="portal",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["portal"], param)

        param = arcpy.Parameter(
            displayName="Usuario",
            name="usuario",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["usuario"], param)

        param = arcpy.Parameter(
            displayName="Clave",
            name="clave",
            datatype="GPStringHidden",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["clave"], param)

        param = arcpy.Parameter(
            displayName="Servicio",
            name="servicio",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["servicio"], param)

        param = arcpy.Parameter(
            displayName="Tabla",
            name="tabla",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["tabla"], param)

        param = arcpy.Parameter(
            displayName="Campo",
            name="campo",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["campo"], param)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        portal = parameters[self.Params["portal"]].valueAsText
        usuario = parameters[self.Params["usuario"]].valueAsText
        clave = parameters[self.Params["clave"]].valueAsText
        servicio = parameters[self.Params["servicioFuente"]].valueAsText
        tabla = parameters[self.Params["servicioDestino"]].valueAsText
        campo = parameters[self.Params["versionDestino"]].valueAsText

        Procesos.ActualizarFecha(
            portal = portal,
            usuario = usuario, 
            clave = clave, 
            servicio= servicio,
            nombreTabla= tabla,
            campoFecha = campo)

        return

