class Pacientes:

    def __init__(self, id_paciente, documento, nombre, fecha_nacimiento, telefono, direccion, correo):
        self.ID_PA                = id_paciente
        self.DOCUMENTO_PA         = documento
        self.NOMBRE_PA            = nombre
        self.FECHA_NAC_PA         = fecha_nacimiento
        self.TELEFONO_PA          = telefono
        self.DIRECCION_PA         = direccion
        self.CORREO_PA            = correo

    def a_diccionario(self):
        return {
            "ID_PA"               : self.ID_PA              ,
            "DOCUMENTO_PA"        : self.DOCUMENTO_PA       ,
            "NOMBRE_PA"           : self.NOMBRE_PA          ,
            "FACHA_NAC_PA"        : self.FECHA_NAC_PA       ,
            "TELEFONO_PA"         : self.TELEFONO_PA        ,
            "DIRECCION_PA"        : self.DIRECCION_PA       ,
            "CORREO_PA"           : self.CORREO_PA       
        }