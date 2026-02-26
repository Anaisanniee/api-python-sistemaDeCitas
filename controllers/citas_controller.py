from flask import jsonify, request
from services.citas_services import (
    listar_citas,
    registrar_cita,
    editar_cita_put,
    eliminar_cita
)

# LISTAR CITAS
def listar_Citas():
    datos = listar_citas()
    return jsonify(datos), 200


# OBTENER CITA
#def obtener_Cita(id):
 #   cita = obtener_cita(id)
  #  if cita is None:
   #     return jsonify({"error": "Cita no encontrada"}), 404
    #return jsonify(cita), 200


# REGISTRAR CITA
def registrar_Cita():
    payload = request.json or {}

    required = [
        "id_paciente",
        "id_doctor",
        "id_servicio",
        "fecha",
        "hora",
        "motivo"
    ]

    for campo in required:
        if campo not in payload:
            return jsonify({"error": f"Falta el campo '{campo}'"}), 400

    id_paciente = payload["id_paciente"]
    id_doctor   = payload["id_doctor"]
    id_servicio = payload["id_servicio"]
    fecha       = payload["fecha"]
    hora        = payload["hora"]
    motivo      = payload["motivo"]

    nueva = registrar_cita(id_paciente, id_doctor, id_servicio, fecha, hora, motivo)
    return jsonify(nueva), 201


# ACTUALIZAR CITA
def actualizar_Cita(id):
    payload = request.json or {}

    actualizada = editar_cita_put(
        id,
        payload.get("id_paciente"),
        payload.get("id_doctor"),
        payload.get("id_servicio"),
        payload.get("fecha"),
        payload.get("hora"),
        payload.get("motivo")
    )

    if actualizada is None:
        return jsonify({"error": "Cita no encontrada"}), 404

    return jsonify(actualizada), 200


# ELIMINAR CITA
def eliminar_Cita(id):
    eliminado = eliminar_cita(id)
    if not eliminado:
        return jsonify({"error": "Cita no encontrada"}), 404
    return jsonify({"mensaje": "Cita eliminada"}), 200