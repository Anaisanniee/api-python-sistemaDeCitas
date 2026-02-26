from flask import current_app
from models.servicios_model import Servicios


def listar_servicios():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM t_servicios"
    c.execute(sql)
    datos = c.fetchall()
    c.close()

    r = [
        Servicios(
            x[0],   
            x[1],   
            x[2],  
            x[3]    
        ).a_diccionario()
        for x in datos
    ]

    return r


def registrar_servicio(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO t_servicios(nombre, duracion_minutos, tipo)
        VALUES(%s, %s, %s)
    """

    valores = (
        data["nombre"],
        data["duracion_minutos"],
        data["tipo"]
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()
    return {"mensaje": "Servicio registrado correctamente"}


def editar_servicio_put(id, data):
    c = current_app.mysql.connection.cursor()

    sql = """
        UPDATE t_servicios
        SET nombre=%s,
            duracion_minutos=%s,
            tipo=%s
        WHERE id_servicio=%s
    """

    valores = (
        data["nombre"],
        data["duracion_minutos"],
        data["tipo"],
        id
    )

    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Servicio actualizado (PUT)"}


def eliminar_servicio(id):
    c = current_app.mysql.connection.cursor()
    sql = "DELETE FROM t_servicios WHERE id_servicio=%s"

    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    c.close()

    return {"mensaje": "Servicio eliminado correctamente"}
