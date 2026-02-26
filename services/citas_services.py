from flask import current_app
from models.citas_model import Citas

def listar_citas():
    c = current_app.mysql.connection.cursor()
    sql = """
        SELECT id_cita, id_paciente, id_profesional, id_servicio, id_consultorio,
               fecha, hora_inicio, hora_fin, estado, notas
        FROM t_citas
    """
    c.execute(sql)
    datos = c.fetchall()
    c.close()

    r = [
        Citas(
            x[0], x[1], x[2], x[3], x[4],
            x[5], x[6], x[7], x[8], x[9]
        ).a_diccionario()
        for x in datos
    ]
    return r

def registrar_cita(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO t_citas (
            id_paciente, id_profesional, id_servicio, id_consultorio,
            fecha, hora_inicio, hora_fin, estado, notas
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        data["id_paciente"],
        data["id_profesional"],
        data["id_servicio"],
        data["id_consultorio"],
        data["fecha"],
        data["hora_inicio"],
        data["hora_fin"],
        data["estado"],
        data.get("notas", None)   # notas puede ser opcional
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Cita registrada correctamente"}

def editar_cita_put(id_cita, data):
    c = current_app.mysql.connection.cursor()
    sql = """
        UPDATE t_citas
        SET id_paciente=%s, id_profesional=%s, id_servicio=%s,
            id_consultorio=%s, fecha=%s, hora_inicio=%s, hora_fin=%s,
            estado=%s, notas=%s
        WHERE id_cita=%s
    """

    valores = (
        data["id_paciente"],
        data["id_profesional"],
        data["id_servicio"],
        data["id_consultorio"],
        data["fecha"],
        data["hora_inicio"],
        data["hora_fin"],
        data["estado"],
        data["notas"],
        id_cita
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Cita actualizada (PUT)"}

def eliminar_cita(id_cita):
    c = current_app.mysql.connection.cursor()
    sql = "DELETE FROM t_citas WHERE id_cita=%s"

    c.execute(sql, (id_cita,))
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Cita eliminada correctamente"}

# cuarto