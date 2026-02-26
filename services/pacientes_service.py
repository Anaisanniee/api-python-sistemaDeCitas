from flask import current_app
from models.pacientes_model import Pacientes


def listar_paciente():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT id_paciente, documento, nombre, fecha_nacimiento, telefono, direccion, correo FROM t_pacientes"
    c.execute(sql)
    datos = c.fetchall()
    c.close()

    r = [
        Pacientes(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6]
        ).a_diccionario()
        for x in datos
    ]
    return r


def registrar_paciente(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO t_pacientes (documento, nombre, fecha_nacimiento, telefono, direccion, correo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        data["documento"],
        data["nombre"],
        data["fecha_nacimiento"],
        data["telefono"],
        data["direccion"],
        data["correo"]
    )
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()
    return {"mensaje": "Paciente registrado correctamente"}


def editar_paciente_put(id_paciente, data):
    c = current_app.mysql.connection.cursor()

    sql = """
        UPDATE t_pacientes
        SET documento=%s, nombre=%s, fecha_nacimiento=%s, telefono=%s, direccion=%s, correo=%s
        WHERE id_paciente=%s
    """
    valores = (
        data["documento"],
        data["nombre"],
        data["fecha_nacimiento"],
        data["telefono"],
        data["direccion"],
        data["correo"],
        id_paciente
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()
    return {"mensaje": "Paciente actualizado (PUT)"}


def eliminar_paciente(id_paciente):
    c = current_app.mysql.connection.cursor()
    sql = "DELETE FROM t_pacientes WHERE id_paciente=%s"
    c.execute(sql, (id_paciente,))
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Paciente eliminado correctamente"}

    #primero
