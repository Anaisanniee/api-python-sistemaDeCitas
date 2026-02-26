from flask import Blueprint, request, jsonify
from controllers.consultorios_controller import (
    listar_consultorios as svc_listar_consultorios, registrar_consultorio as svc_registrar_consultorio, 
    editar_consultorio_put as svc_editar_consultorio, eliminar_consultorio as svc_eliminar_consultorio
)

consultorios_bp = Blueprint("consultorios_bp", __name__)

#LISTAR
@consultorios_bp.route("/", methods=["GET"])
def obtener_consultorios():
    """
    Listar consultorios
    ---
    tags:
      - Consultorios
    summary: Obtener lista de consultorios
    description: Retorna todos los consultorios o permite filtrarlos por parámetros.
    parameters:
      - in: query
        name: nombre
        required: false
        type: string
        description: Filtrar consultorios por nombre
        example: Consultorio General
      - in: query
        name: id_servicio
        required: false
        type: integer
        description: Filtrar consultorios por ID del servicio
        example: 1
    responses:
      200:
        description: Lista de consultorios obtenida correctamente
        content:
          application/json:
            example:
              - id: 1
                nombre: Consultorio General
                id_servicio: 1
              - id: 2
                nombre: Consultorio Odontología
                id_servicio: 2
      404:
        description: No se encontraron consultorios
      500:
        description: Error interno del servidor
    """
    return jsonify(svc_listar_consultorios()), 200

@consultorios_bp.route("/<int:id>", methods=["GET"])
def obtener_citas():
    """
    Obtener un consultorio por ID
    ---
    tags:
      - Consultorios
    summary: Obtener consultorio
    description: Obtiene la información de un consultorio específico usando su ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del consultorio
        example: 3

    responses:
      200:
        description: Consultorio obtenido correctamente
        examples:
          application/json:
            id: 3
            nombre: "Consultorio 1"
            id_servicio: 2

      404:
        description: Consultorio no encontrado
        examples:
          application/json:
            error: Consultorio no encontrado

      500:
        description: Error interno del servidor
    """
    return jsonify(svc_listar_consultorios()), 200

#REGISTRAR (ADMIN)
@consultorios_bp.route("/", methods=["POST"])
def crear_consultorio():
    """
    Registrar un nuevo consultorio
    ---
    tags:
      - Consultorios
    summary: Crear consultorio
    description: Registra un nuevo consultorio en el sistema.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Datos del consultorio
        schema:
          type: object
          required:
            - nombre
            - id_servicio
          properties:
            nombre:
              type: string
              description: Nombre del consultorio
              example: Consultorio General
            id_servicio:
              type: integer
              description: ID del servicio asociado
              example: 1
    responses:
      201:
        description: Consultorio creado correctamente
        content:
          application/json:
            example:
              mensaje: Consultorio creado
              consultorio:
                id: 1
                nombre: Consultorio General
                id_servicio: 1
      400:
        description: Faltan campos obligatorios
        content:
          application/json:
            example:
              error: Faltan campos obligatorios
      500:
        description: Error interno del servidor
    """
    data = request.get_json()

    if "nombre" not in data or "id_servicio" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    nuevo = svc_registrar_consultorio(data)
    return jsonify({"mensaje": "Consultorio creado", "consultorio": nuevo}), 201


#ACTUALIZAR (ADMIN)
@consultorios_bp.route("/<int:id>", methods=["PUT"])
def editar_consultorio(id):
    """
    Actualizar un consultorio
    ---
    tags:
      - Consultorios
    summary: Actualizar consultorio por ID
    description: Actualiza la información de un consultorio existente.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del consultorio a actualizar
        example: 3

      - in: body
        name: body
        required: true
        description: Datos del consultorio a actualizar
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: Consultorio Pediatría
            id_servicio:
              type: integer
              example: 2
          additionalProperties: false

    responses:
      200:
        description: Consultorio actualizado correctamente
        examples:
          application/json:
            mensaje: Consultorio actualizado
            consultorio:
              id: 3
              nombre: Consultorio Pediatría
              id_servicio: 2

      404:
        description: Consultorio no encontrado
        examples:
          application/json:
            error: Consultorio no encontrado

      400:
        description: Datos inválidos o cuerpo vacío
    """
    data = request.get_json()
    actualizado = svc_editar_consultorio(id, data)

    if not actualizado:
        return jsonify({"error": "Consultorio no encontrado"}), 404

    return jsonify({"mensaje": "Consultorio actualizado", "consultorio": actualizado}), 200


#ELIMINAR (ADMIN)
@consultorios_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_consultorio(id):
    """
    Eliminar un consultorio
    ---
    tags:
      - Consultorios
    summary: Eliminar consultorio por ID
    description: Elimina un consultorio existente usando su ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del consultorio a eliminar
        example: 5

    responses:
      200:
        description: Consultorio eliminado correctamente
        examples:
          application/json:
            mensaje: Consultorio eliminado

      404:
        description: Consultorio no encontrado
        examples:
          application/json:
            error: Consultorio no encontrado
    """
    eliminado = svc_eliminar_consultorio(id)
    if not eliminado:
        return jsonify({"error": "Consultorio no encontrado"}), 404

    return jsonify({"mensaje": "Consultorio eliminado"}), 200
