from flask import jsonify, request
from services.servicios_services import (
    listar_servicios,
    registrar_servicio,
    editar_servicio_put,
    eliminar_servicio
)

# LISTAR
def listar_Servicios():
    datos = listar_servicios()
    return jsonify(datos), 200

# OBTENER POR ID
#def obtener_servicio(id):
 #   datos = obtener_servicio(id)
  #  if datos is None:
   #     return jsonify({"error": "Servicio no encontrado"}), 404
    #return jsonify(datos), 200

# REGISTRAR
def registrar_servicio():
    payload = request.json or {}

    required = ["nombre_servicio", "descripcion"]
    for campo in required:
        if campo not in payload:
            return jsonify({"error": f"Falta el campo '{campo}'"}), 400

    nombre = payload["nombre_servicio"]
    descripcion = payload["descripcion"]

    nuevo = registrar_servicio(nombre, descripcion)
    return jsonify(nuevo), 201

# ACTUALIZAR
def actualizar_servicio(id):
    payload = request.json or {}

    nombre = payload.get("nombre_servicio")
    descripcion = payload.get("descripcion")

    actualizado = editar_servicio_put(id, nombre, descripcion)
    if actualizado is None:
        return jsonify({"error": "Servicio no encontrado"}), 404

    return jsonify(actualizado), 200

# ELIMINAR
def eliminar_servicio(id):
    eliminado = eliminar_servicio(id)
    if not eliminado:
        return jsonify({"error": "Servicio no encontrado"}), 404
    return jsonify({"mensaje": "Servicio eliminado"}), 200