from flask import current_app
from models.consultorios_model import Consultorios

def listar_consultorios():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT id_consultorio, nombre, ubicacion, tipo FROM t_consultorios"
    c.execute(sql)
    datos = c.fetchall()
    c.close()

    r = [
        Consultorios(
            x[0], x[1], x[2], x[3]
        ).a_diccionario()
        for x in datos
    ]
    return r

def registrar_consultorio(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO t_consultorios (nombre, ubicacion, tipo)
        VALUES (%s, %s, %s)
    """

    valores = (
        data["nombre"],
        data["ubicacion"],
        data["tipo"]
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Consultorio registrado correctamente"}

def editar_consultorio_put(id_consultorio, data):
    c = current_app.mysql.connection.cursor()
    sql = """
        UPDATE t_consultorios
        SET nombre=%s, ubicacion=%s, tipo=%s
        WHERE id_consultorio=%s
    """

    valores = (
        data["nombre"],
        data["ubicacion"],
        data["tipo"],
        id_consultorio
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Consultorio actualizado (PUT)"}


def eliminar_consultorio(id_consultorio):
    c = current_app.mysql.connection.cursor()
    sql = "DELETE FROM t_consultorios WHERE id_consultorio=%s"

    c.execute(sql, (id_consultorio,))
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Consultorio eliminado correctamente"}

# tercero