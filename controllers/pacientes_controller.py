from flask import jsonify, request
from services.pacientes_service import (
    listar_paciente,
    registrar_paciente,
    editar_paciente_put,
    eliminar_paciente
)

# LISTAR PACIENTES
def listar_Paciente():
    datos = listar_paciente()
    return jsonify(datos), 200


# OBTENER PACIENTE
#def obtener_Paciente(id):
 #   paciente = obtener_paciente(id)
  #  if paciente is None:
   #     return jsonify({"error": "Paciente no encontrado"}), 404
    #return jsonify(paciente), 200


# REGISTRAR PACIENTE
def registrarPaciente():
    payload = request.json or {}

    required = [
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "fecha_nacimiento",
        "identificacion"
    ]

    for campo in required:
        if campo not in payload:
            return jsonify({"error": f"Falta el campo '{campo}'"}), 400

    p_nom  = payload["primer_nombre"]
    s_nom  = payload["segundo_nombre"]
    p_ape  = payload["primer_apellido"]
    s_ape  = payload["segundo_apellido"]
    fecha  = payload["fecha_nacimiento"]
    docid  = payload["identificacion"]

    nuevo = registrar_paciente(p_nom, s_nom, p_ape, s_ape, fecha, docid)
    return jsonify(nuevo), 201


# ACTUALIZAR PACIENTE
def editar_paciente_put(id):
    payload = request.json or {}

    actualizado = editar_paciente_put(
        id,
        payload.get("primer_nombre"),
        payload.get("segundo_nombre"),
        payload.get("primer_apellido"),
        payload.get("segundo_apellido"),
        payload.get("fecha_nacimiento"),
        payload.get("identificacion")
    )

    if actualizado is None:
        return jsonify({"error": "Paciente no encontrado"}), 404

    return jsonify(actualizado), 200


# ELIMINAR PACIENTE
def eliminar_Paciente(id):
    eliminado = eliminar_paciente(id)
    if not eliminado:
        return jsonify({"error": "Paciente no encontrado"}), 404
    return jsonify({"mensaje": "Paciente eliminado"}), 200