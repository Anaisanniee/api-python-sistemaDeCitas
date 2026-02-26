from flask import current_app
from models.doctores_model import Doctores

def listar_doctores():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT id_profesional, nombre, especialidad, telefono, correo FROM t_doctores"
    c.execute(sql)
    datos = c.fetchall()
    c.close()

    r = [
        Doctores(
            x[0], x[1], x[2], x[3], x[4]
        ).a_diccionario()
        for x in datos
    ]
    return r

def registrar_doctor(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO t_doctores (nombre, especialidad, telefono, correo)
        VALUES (%s, %s, %s, %s)
    """

    valores = (
        data["nombre"],
        data["especialidad"],
        data["telefono"],
        data["correo"]
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Doctor registrado correctamente"}


def editar_doctor_put(id_profesional, data):
    c = current_app.mysql.connection.cursor()
    sql = """
        UPDATE t_doctores
        SET nombre=%s, especialidad=%s, telefono=%s, correo=%s
        WHERE id_profesional=%s
    """

    valores = (
        data["nombre"],
        data["especialidad"],
        data["telefono"],
        data["correo"],
        id_profesional
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Doctor actualizado (PUT)"}


def eliminar_doctor(id_profesional):
    c = current_app.mysql.connection.cursor()
    sql = "DELETE FROM t_doctores WHERE id_profesional=%s"

    c.execute(sql, (id_profesional,))
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Doctor eliminado correctamente"}

#segundo 