from urllib import request
from flask import Blueprint, jsonify
from controllers.doctores_controller import ( 
    listar_doctores as svc_listar_doctores, registrar_doctor as svc_registrar_doctores, 
    editar_doctor_put as svc_editar_doctor, eliminar_doctor as svc_eliminar_doctor
    )

doctores_bp = Blueprint("doctores_bp", __name__)

@doctores_bp.route("/", methods=["POST"])
def crear_doctor():
    """
    Registrar un nuevo doctor
    ---
    tags:
      - Doctores
    summary: Crear doctor
    description: Registra un nuevo doctor en el sistema.
    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        description: Datos del doctor
        schema:
          type: object
          required:
            - nombre
            - id_servicio
          properties:
            nombre:
              type: string
              description: Nombre completo del doctor
              example: Juan Pérez
            id_servicio:
              type: integer
              description: ID del servicio médico asignado
              example: 2

    responses:
      201:
        description: Doctor creado correctamente
        examples:
          application/json:
            mensaje: Doctor creado
            doctor:
              id: 1
              nombre: Juan Pérez
              id_servicio: 2

      400:
        description: Faltan campos obligatorios
        examples:
          application/json:
            error: Faltan campos obligatorios

      500:
        description: Error interno del servidor
    """
    data = request.get_json()

    if not data or "nombre" not in data or "id_servicio" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    nuevo = svc_registrar_doctores(data)
    return jsonify({"mensaje": "Doctor creado", "doctor": nuevo}), 201


#LISTAR DOCTORES
@doctores_bp.route("/", methods=["GET"])
def obtener_doctores():
    """
    Listar doctores
    ---
    tags:
      - Doctores
    summary: Obtener lista de doctores
    description: Retorna la lista completa de doctores registrados en el sistema.

    responses:
      200:
        description: Lista de doctores obtenida correctamente
        examples:
          application/json:
            - id: 1
              nombre: "Juan Pérez"
              especialidad: "Cardiología"
            - id: 2
              nombre: "María Gómez"
              especialidad: "Pediatría"

      500:
        description: Error interno del servidor
        examples:
          application/json:
            error: Error interno del servidor
    """
    return jsonify(svc_listar_doctores()), 200

@doctores_bp.route("/<int:id>", methods=["GET"])
def obtener_doctor(id):
    """
    Obtener un doctor por ID
    ---
    tags:
      - Doctores
    summary: Obtener doctor
    description: Obtiene la información de un doctor específico usando su ID.

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del doctor
        example: 3

    responses:
      200:
        description: Doctor obtenido correctamente
        examples:
          application/json:
            id: 3
            nombre: "Doctor 1"
            id_servicio: 2

      404:
        description: Doctor no encontrado
        examples:
          application/json:
            error: "Doctor no encontrado"

      500:
        description: Error interno del servidor
    """
    Doctor = svc_listar_doctores(id)

    if not Doctor:
        return jsonify({"error": "Consultorio no encontrado"}), 404

    return jsonify(Doctor), 200

#ACTUALIZAR (ADMIN)
@doctores_bp.route("/<int:id>", methods=["PUT"])
def editar_doctor(id):
    """
    Editar doctor
    ---
    tags:
      - Doctores
    summary: Actualizar información de un doctor
    description: |
      Actualiza los datos de un doctor existente.
      **Este endpoint debería ser usado solo por usuarios ADMIN.**

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del doctor a actualizar
        example: 3

      - in: body
        name: body
        required: true
        description: Datos a actualizar del doctor
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: "Carlos Ramírez"
            especialidad:
              type: string
              example: "Neurología"
            id_servicio:
              type: integer
              example: 2
          additionalProperties: false

    responses:
      200:
        description: Doctor actualizado correctamente
        examples:
          application/json:
            mensaje: "Doctor actualizado"
            doctor:
              id: 3
              nombre: "Carlos Ramírez"
              especialidad: "Neurología"

      400:
        description: Datos inválidos o cuerpo vacío
        examples:
          application/json:
            error: "Datos inválidos"

      404:
        description: Doctor no encontrado
        examples:
          application/json:
            error: "Doctor no encontrado"

      500:
        description: Error interno del servidor
    """
    data = request.get_json()
    actualizado = svc_editar_doctor(id, data)

    if not actualizado:
        return jsonify({"error": "Doctor no encontrado"}), 404

    return jsonify({"mensaje": "Doctor actualizado", "doctor": actualizado}), 200

#ELIMINAR PACIENTE
@doctores_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_doctor_route(id):
    """
    Eliminar doctor
    ---
    tags:
      - Doctores
    summary: Eliminar un doctor
    description: |
      Elimina un doctor por su ID.
      **Este endpoint debería ser usado solo por ADMIN.**

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del doctor a eliminar
        example: 7

    responses:
      200:
        description: Doctor eliminado correctamente
        examples:
          application/json:
            mensaje: "Doctor eliminado"

      404:
        description: Doctor no encontrado
        examples:
          application/json:
            error: "Doctor no encontrado"

      500:
        description: Error interno del servidor
    """
    eliminado = svc_eliminar_doctor(id)

    if not eliminado:
        return jsonify({"error": "Paciente no encontrado"}), 404

    return jsonify({"mensaje": "Paciente eliminado"}), 200