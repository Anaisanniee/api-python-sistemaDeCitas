class Servicios:

    def __init__(self, id_servicio, nombre, duracion_minutos, tipo):
        self.ID_SER                = id_servicio
        self.NOMBRE_SER            = nombre
        self.DURACION_MIN          = duracion_minutos
        self.TIPO                  = tipo

    def a_diccionario(self):
        return {
            "ID_SER"               : self.ID_SER                ,
            "NOMBRE_SER"           : self.NOMBRE_SER            ,
            "DURACION_MIN"         : self.DURACION_MIN          ,
            "TIPO"                 : self.TIPO        
        }