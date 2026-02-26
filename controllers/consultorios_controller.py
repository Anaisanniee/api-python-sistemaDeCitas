from flask import jsonify, request
from services.consultorios_services import (
    listar_consultorios,
    registrar_consultorio,
    editar_consultorio_put,
    eliminar_consultorio
)

# LISTAR
def listar_Consultorios():
    datos = listar_consultorios()
    return jsonify(datos), 200

# REGISTRAR
def registrar_Consultorio():
    payload = request.json or {}

    required = [
        "numero", "piso", "area",
        "primer_nombre_responsable",
        "segundo_nombre_responsable",
        "primer_apellido_responsable",
        "segundo_apellido_responsable",
        "identificacion_responsable"
    ]

    for campo in required:
        if campo not in payload:
            return jsonify({"error": f"Falta el campo '{campo}'"}), 400

    numero = payload["numero"]
    piso = payload["piso"]
    area = payload["area"]

    p_nom = payload["primer_nombre_responsable"]
    s_nom = payload["segundo_nombre_responsable"]
    p_ape = payload["primer_apellido_responsable"]
    s_ape = payload["segundo_apellido_responsable"]
    docid = payload["identificacion_responsable"]

    nuevo = registrar_consultorio(
        numero, piso, area,
        p_nom, s_nom, p_ape, s_ape,
        docid
    )
    return jsonify(nuevo), 201

# ACTUALIZAR
def editar_consultorio_put(id):
    payload = request.json or {}

    actualizado = editar_consultorio_put(
        id,
        payload.get("numero"),
        payload.get("piso"),
        payload.get("area"),
        payload.get("primer_nombre_responsable"),
        payload.get("segundo_nombre_responsable"),
        payload.get("primer_apellido_responsable"),
        payload.get("segundo_apellido_responsable"),
        payload.get("identificacion_responsable")
    )

    if actualizado is None:
        return jsonify({"error": "Consultorio no encontrado"}), 404

    return jsonify(actualizado), 200

# ELIMINAR
def eliminar_Consultorio(id):
    eliminado = eliminar_consultorio(id)
    if not eliminado:
        return jsonify({"error": "Consultorio no encontrado"}), 404
    return jsonify({"mensaje": "Consultorio eliminado"}), 200