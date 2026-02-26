class Citas:

    def __init__(self, id_cita, id_paciente, id_profesional, id_servicio, id_consultorio, fecha, hora_inicio, hora_fin, estado, notas):
        self.ID_CITA                    = id_cita
        self.ID_PACIENTE                = id_paciente
        self.ID_PROFESIONAL             = id_profesional
        self.ID_SERVICIO                = id_servicio
        self.ID_CONSULTORIO             = id_consultorio
        self.FECHA                      = fecha
        self.HORA_INICIO                = hora_inicio
        self.HORA_FIN                   = hora_fin
        self.ESTADO                     = estado
        self.NOTAS                      = notas

    def a_diccionario(self):
        return {
            "ID_CITA"                   : self.ID_CITA                  ,
            "ID_PACIENTE"               : self.ID_PACIENTE              ,
            "ID_PROFESIONAL"            : self.ID_PROFESIONAL           ,
            "ID_SERVICIO"               : self.ID_SERVICIO              ,
            "ID_CONSULTORIO"            : self.ID_CONSULTORIO           ,
            "FECHA"                     : self.FECHA                    ,
            "HORA_INICIO"               : self.HORA_INICIO              ,     
            "HORA_FIN"                  : self.HORA_FIN                 ,
            "ESTADO"                    : self.ESTADO                   ,
            "NOTAS"                     : self.NOTAS
        }