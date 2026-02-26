class Consultorios:

    def __init__(self, id_consultorio, nombre, ubicacion, tipo):
        self.ID_CON                = id_consultorio
        self.NOMBRE_CON            = nombre
        self.UBICACION             = ubicacion
        self.TIPO                  = tipo

    def a_diccionario(self):
        return {
            "ID_CON"               : self.ID_CON                ,
            "NOMBRE_CON"           : self.NOMBRE_CON            ,
            "UBICACION"            : self.UBICACION             ,
            "TIPO"                 : self.TIPO        
        }