class Doctores:

    def __init__(self, id_profesional, nombre, especialidad, telefono, correo):
        self.ID_PRO                 = id_profesional
        self.NOMBRE_PRO             = nombre
        self.ESPECIALIDAD           = especialidad
        self.TELEFONO_PRO           = telefono
        self.CORREO_PRO             = correo

    def a_diccionario(self):
        return {
            "ID_PRO"               : self.ID_PRO              ,
            "NOMBRE_PRO"           : self.NOMBRE_PRO          ,
            "ESPECIALIDAD"         : self.ESPECIALIDAD        ,
            "TELEFONO_PRO"         : self.TELEFONO_PRO        ,
            "CORREO_PRO"           : self.CORREO_PRO       
        }