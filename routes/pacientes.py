from flask import Blueprint, request, jsonify
from controllers.pacientes_controller import (
    listar_paciente as svc_listar_paciente, registrar_paciente as svc_registrar_pacientes,
    editar_paciente_put as svc_editar_paciente, eliminar_paciente as svc_eliminar_paciente
)

pacientes_bp = Blueprint("pacientes_bp", __name__)

#REGISTRAR NUEVO PACIENTE
@pacientes_bp.route("/", methods=["POST"])
def crear_paciente():
    """
    Registrar un nuevo paciente
    ---
    tags:
      - Pacientes
    summary: Crear paciente
    description: Registra un nuevo paciente en el sistema.
    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        description: Datos del paciente
        schema:
          type: object
          required:
            - nombre
            - documento
            - fecha_nacimiento
            - correo
          properties:
            nombre:
              type: string
              description: Nombre completo del paciente
              example: María López
            documento:
              type: string
              description: Documento de identidad
              example: "1023456789"
            fecha_nacimiento:
              type: string
              format: date
              description: Fecha de nacimiento (YYYY-MM-DD)
              example: "1998-05-20"
            correo:
              type: string
              format: email
              description: Correo electrónico del paciente
              example: maria.lopez@gmail.com

    responses:
      201:
        description: Paciente registrado correctamente
        examples:
          application/json:
            mensaje: Paciente registrado
            paciente:
              id: 1
              nombre: María López
              documento: "1023456789"
              fecha_nacimiento: "1998-05-20"
              correo: maria.lopez@gmail.com

      400:
        description: Error de validación
        examples:
          application/json:
            error: Faltan campos obligatorios
            faltan:
              - documento
              - correo

      500:
        description: Error interno del servidor
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar datos"}), 400

    campos_obligatorios = [
        "nombre", "documento", "fecha_nacimiento", "correo"
    ]

    faltantes = [c for c in campos_obligatorios if c not in data]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltan": faltantes
        }), 400

    nuevo = svc_registrar_pacientes(data)
    return jsonify({"mensaje": "Paciente registrado", "paciente": nuevo}), 201

@pacientes_bp.route("/<int:id>", methods=["GET"])
def obtener_paciente_route(id):
    """
    Obtener un paciente por ID
    ---
    tags:
      - Pacientes
    summary: Consultar paciente específico
    description: Retorna los datos de un paciente filtrado por su ID único.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID numérico del paciente en la base de datos
        example: 1
    responses:
      200:
        description: Datos del paciente encontrados con éxito
        schema:
          type: object
          properties:
            id:
              type: integer
            nombre:
              type: string
            apellido:
              type: string
            telefono:
              type: string
      404:
        description: El ID solicitado no existe en el sistema
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Paciente no encontrado"
      500:
        description: Error interno al procesar la solicitud
    """
    # Llamada al controlador pasando el ID
    paciente = svc_listar_paciente(id)

    # Aquí manejamos el "None" que mencionaste al principio
    if paciente is None:
        return jsonify({"error": "Paciente no encontrado"}), 404

    return jsonify(paciente), 200

#LISTAR TODOS LOS PACIENTES
@pacientes_bp.route("/", methods=["GET"])
def obtener_pacientes():
    """
    Obtener la lista de pacientes
    ---
    tags:
      - Pacientes
    summary: Listar pacientes
    description: Obtiene la lista completa de pacientes registrados en el sistema.

    responses:
      200:
        description: Lista de pacientes obtenida correctamente
        examples:
          application/json:
            - id: 1
              nombre: Juan Pérez
              documento: "123456789"
              fecha_nacimiento: "1995-03-10"
              correo: juan@gmail.com
            - id: 2
              nombre: María López
              documento: "987654321"
              fecha_nacimiento: "1998-05-20"
              correo: maria@gmail.com

      500:
        description: Error interno del servidor
    """
    return jsonify(svc_listar_paciente()), 200

#EDITAR INFORMACION DE PACIENTE
@pacientes_bp.route("/<int:id>", methods=["PUT"])
def editar_paciente(id):
    """
    Actualizar un paciente
    ---
    tags:
      - Pacientes
    summary: Editar paciente
    description: Actualiza la información de un paciente existente usando su ID.

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del paciente a actualizar
        example: 5

      - in: body
        name: body
        required: true
        description: Datos del paciente a actualizar
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: Juan Pérez
            documento:
              type: string
              example: "123456789"
            fecha_nacimiento:
              type: string
              example: "1995-03-10"
            correo:
              type: string
              example: juan@gmail.com
          additionalProperties: false

    responses:
      200:
        description: Paciente actualizado correctamente
        examples:
          application/json:
            mensaje: Paciente actualizado

      400:
        description: No se enviaron datos
        examples:
          application/json:
            error: Debes enviar datos

      404:
        description: Paciente no encontrado
        examples:
          application/json:
            error: Paciente no encontrado

      500:
        description: Error interno del servidor
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar datos"}), 400

    actualizado = svc_editar_paciente(id, data)

    if not actualizado:
        return jsonify({"error": "Paciente no encontrado"}), 404

    return jsonify({"mensaje": "Paciente actualizado"}), 200

#ELIMINAR PACIENTE
@pacientes_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_paciente(id):
    """
    Eliminar un paciente
    ---
    tags:
      - Pacientes
    summary: Eliminar paciente
    description: Elimina un paciente del sistema usando su ID.

    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del paciente a eliminar
        example: 8

    responses:
      200:
        description: Paciente eliminado correctamente
        examples:
          application/json:
            mensaje: Paciente eliminado

      404:
        description: Paciente no encontrado
        examples:
          application/json:
            error: Paciente no encontrado

      500:
        description: Error interno del servidor
    """
    eliminado = svc_eliminar_paciente(id)

    if not eliminado:
        return jsonify({"error": "Paciente no encontrado"}), 404

    return jsonify({"mensaje": "Paciente eliminado"}), 200
