from flask import jsonify, request
from services.doctores_services import (
    listar_doctores,
    registrar_doctor,
    editar_doctor_put,
    eliminar_doctor
)

# LISTAR
def listar_Doctores():
    datos = listar_doctores()
    return jsonify(datos), 200

# OBTENER
#def obtener_Doctor(id):
 #   doctor = obtener_doctor(id)
  #  if doctor is None:
   #     return jsonify({"error": "Doctor no encontrado"}), 404
    #return jsonify(doctor), 200

# REGISTRAR
def registrar_Doctor():
    payload = request.json or {}

    required = [
        "primer_nombre", "segundo_nombre",
        "primer_apellido", "segundo_apellido",
        "especialidad", "identificacion"
    ]

    for campo in required:
        if campo not in payload:
            return jsonify({"error": f"Falta el campo '{campo}'"}), 400

    p_nom = payload["primer_nombre"]
    s_nom = payload["segundo_nombre"]
    p_ape = payload["primer_apellido"]
    s_ape = payload["segundo_apellido"]
    esp   = payload["especialidad"]
    docid = payload["identificacion"]

    nuevo = registrar_doctor(p_nom, s_nom, p_ape, s_ape, esp, docid)
    return jsonify(nuevo), 201

# ACTUALIZAR
def actualizar_Doctor(id):
    payload = request.json or {}

    actualizado = editar_doctor_put(
        id,
        payload.get("primer_nombre"),
        payload.get("segundo_nombre"),
        payload.get("primer_apellido"),
        payload.get("segundo_apellido"),
        payload.get("especialidad"),
        payload.get("identificacion")
    )

    if actualizado is None:
        return jsonify({"error": "Doctor no encontrado"}), 404

    return jsonify(actualizado), 200

# ELIMINAR
def eliminar_Doctor(id):
    eliminado = eliminar_doctor(id)
    if not eliminado:
        return jsonify({"error": "Doctor no encontrado"}), 404
    return jsonify({"mensaje": "Doctor eliminado"}), 200