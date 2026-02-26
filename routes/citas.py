from flask import Blueprint, request, jsonify
from controllers.citas_controller import (
    listar_citas as svc_listar_citas, registrar_cita as svc_registar_cita,
    editar_cita_put as svc_editar_citas, eliminar_cita as svc_eliminar_citas
)
from controllers.pacientes_controller import listar_paciente as svc_listar_paciente
from controllers.doctores_controller import listar_doctores as svc_listar_doctores

citas_bp = Blueprint("citas_bp", __name__)

#REGISTRAR CITAS
@citas_bp.route("/", methods=["POST"])
def crear_cita():
    """
    Registrar una nueva cita médica
    ---
    tags:
      - Citas
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Datos necesarios para crear la cita
        schema:
          type: object
          required:
            - paciente_id
            - doctor_id
            - fecha
            - hora
          properties:
            paciente_id:
              type: integer
              description: ID único del paciente
              example: 1
            doctor_id:
              type: integer
              description: ID único del doctor
              example: 2
            fecha:
              type: string
              description: Fecha en formato AAAA-MM-DD
              example: "2025-12-20"
            hora:
              type: string
              description: Hora en formato HH:MM
              example: "10:30"
    responses:
      201:
        description: Cita creada exitosamente
      400:
        description: Error en los datos enviados o formato incorrecto
      404:
        description: El paciente o el doctor no fueron encontrados
      500:
        description: Error interno del servidor (posible recursión o fallo de DB)
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Debes enviar datos"}), 400

    campos = ["paciente_id", "doctor_id", "fecha", "hora"]
    faltantes = [c for c in campos if c not in data]

    if faltantes:
        return jsonify({"error": "Faltan datos", "faltan": faltantes}), 400

    # Valida QUE EL PACIENTE/USUARIO existe
    if not svc_listar_paciente(data["paciente_id"]):
        return jsonify({"error": "Paciente no existe"}), 404

    # Validar existencia del doctor
    if not svc_listar_doctores(data["doctor_id"]):
        return jsonify({"error": "Doctor no existe"}), 404

    nueva = svc_registar_cita(data)
    return jsonify({"mensaje": "Cita creada", "cita": nueva}), 201


#LISTAR CITAS
@citas_bp.route("/<int:id>", methods=["GET"])
def obtener_citas():
    """
    Obtener una lista en especifico (con filtros opcionales)
    ---
    tags:
      - Citas
    parameters:
      - name: paciente_id
        in: query
        type: integer
        description: Filtrar citas por el ID del paciente
        required: false
      - name: doctor_id
        in: query
        type: integer
        description: Filtrar citas por el ID del doctor
        required: false
    responses:
      200:
        description: Lista de citas obtenida correctamente
      500:
        description: Error interno o de recursión detectado
    """
    return jsonify(svc_listar_citas()), 200

@citas_bp.route("/", methods=["GET"])
def obtener_todas_citas():
    """
    Obtener la lista de citas (con filtros opcionales)
    ---
    tags:
      - Citas
    parameters:
      - name: paciente_id
        in: query
        type: integer
        description: Filtrar citas por el ID del paciente
        required: false
      - name: doctor_id
        in: query
        type: integer
        description: Filtrar citas por el ID del doctor
        required: false
    responses:
      200:
        description: Lista de citas obtenida correctamente
      500:
        description: Error interno o de recursión detectado
    """
    return jsonify(svc_listar_citas()), 200

#EDITAR INFORMACION DE CITA
@citas_bp.route("/<int:id>", methods=["PUT"])
def actualizar_cita(id):
    """
    Editar una cita médica
    ---
    tags:
      - Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la cita a editar
        example: 5

      - in: body
        name: body
        required: true
        description: Datos a actualizar de la cita
        schema:
          type: object
          properties:
            paciente_id:
              type: integer
              example: 1
            doctor_id:
              type: integer
              example: 2
            fecha:
              type: string
              example: "2025-12-25"
            hora:
              type: string
              example: "14:00"
          additionalProperties: false

    responses:
      200:
        description: Cita actualizada correctamente
        examples:
          application/json:
            mensaje: "Cita actualizada"

      400:
        description: No se enviaron datos

      404:
        description: Cita no encontrada
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar datos"}), 400

    actualizado = svc_editar_citas(id, data)

    if not actualizado:
        return jsonify({"error": "Cita no encontrada"}), 404

    return jsonify({"mensaje": "Cita actualizada"}), 200

#ELIMINAR CITA
@citas_bp.route("/<int:id>", methods=["DELETE"])
def borrar_cita(id):
    """
    Eliminar una cita médica
    ---
    tags:
      - Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la cita a eliminar
        example: 10

    responses:
      200:
        description: Cita eliminada correctamente
        examples:
          application/json:
            mensaje: "Cita eliminada"

      404:
        description: Cita no encontrada
        examples:
          application/json:
            error: "Cita no encontrada"
    """
    eliminado = svc_eliminar_citas(id)

    if not eliminado:
        return jsonify({"error": "Cita no encontrada"}), 404

    return jsonify({"mensaje": "Cita eliminada"}), 200
