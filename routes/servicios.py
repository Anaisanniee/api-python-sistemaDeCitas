from flask import Blueprint, request, jsonify
from controllers.servicios_controller import (
    listar_servicios as svc_listar_servicio, registrar_servicio as svc_registrar_servicio, 
    actualizar_servicio as svc_actualizar_servicio, eliminar_servicio as svc_eliminar_servicio
)

servicios_bp = Blueprint("servicios_bp", __name__)

# ------------------ LISTAR ------------------
@servicios_bp.route("/", methods=["GET"])
def obtener_servicios():
    """
    Listar todos los servicios disponibles
    ---
    tags:
      - Servicios
    summary: Obtener lista de servicios
    description: Retorna un listado completo de los servicios médicos registrados.
    responses:
      200:
        description: Lista de servicios obtenida con éxito
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nombre:
                type: string
                example: "Cardiología"
      500:
        description: Error de recursión o de base de datos
    """
    return jsonify(svc_listar_servicio()), 200


#OBTENER UN SERVICIO
@servicios_bp.route("/<int:id>", methods=["GET"])
def obtener_servicio(id):
    """
    Obtener detalles de un servicio específico
    ---
    tags:
      - Servicios
    summary: Buscar servicio por ID
    description: Retorna la información detallada de un solo servicio médico usando su ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID numérico del servicio a consultar
        example: 1
    responses:
      200:
        description: Servicio encontrado correctamente
        schema:
          type: object
          properties:
            id:
              type: integer
            nombre:
              type: string
            descripcion:
              type: string
      404:
        description: No se encontró un servicio con ese ID
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Servicio no encontrado"
      500:
        description: Error interno del servidor (posible recursión o fallo de DB)
    """
    servicio = svc_listar_servicio(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404
    return jsonify(servicio), 200


#REGISTRAR (ADMIN)
@servicios_bp.route("/", methods=["POST"])
def registrar():
    """
    Registrar un nuevo servicio médico
    ---
    tags:
      - Servicios
    summary: Crear servicio
    description: Crea un nuevo registro de servicio. Requiere un JSON con nombre y duración.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Datos del nuevo servicio
        schema:
          type: object
          required:
            - nombre
            - duracion
          properties:
            nombre:
              type: string
              example: "Consulta General"
            duracion:
              type: string
              example: "30 min"
    responses:
      201:
        description: Servicio creado con éxito
        schema:
          type: object
          properties:
            mensaje:
              type: string
            servicio:
              type: object
      400:
        description: Error en los datos enviados (Faltan campos)
      415:
        description: Error de tipo de medio (No se envió application/json)
      500:
        description: Error interno del servidor
    """
    data = request.get_json()

    if "nombre" not in data or "duracion" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    nuevo = svc_registrar_servicio(data)
    return jsonify({"mensaje": "Servicio creado", "servicio": nuevo}), 201


#ACTUALIZAR (ADMIN)
@servicios_bp.route("/<int:id>", methods=["PUT"])
def actualizar(id):
    """
    Actualizar un servicio existente
    ---
    tags:
      - Servicios
    summary: Editar servicio por ID
    description: Modifica los datos de un servicio. Requiere el ID en la URL y el JSON en el cuerpo.
    consumes:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del servicio a editar
        example: 1
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: "Consulta Especializada"
            duracion:
              type: string
              example: "45 min"
    responses:
      200:
        description: Servicio actualizado correctamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
            servicio:
              type: object
      404:
        description: No se encontró el servicio con ese ID
      415:
        description: Error de Content-Type. Olvidaste el application/json
      500:
        description: Error interno del servidor o recursión infinita
    """
    data = request.get_json()
    actualizado = svc_actualizar_servicio(id, data)

    if not actualizado:
        return jsonify({"error": "Servicio no encontrado"}), 404

    return jsonify({"mensaje": "Servicio actualizado", "servicio": actualizado}), 200


#ELIMINAR (ADMIN)
@servicios_bp.route("/<int:id>", methods=["DELETE"])
def eliminar(id):
    """
    Eliminar un servicio por ID
    ---
    tags:
      - Servicios
    summary: Borrar servicio
    description: Elimina permanentemente un servicio de la base de datos usando su ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del servicio que se desea eliminar
        example: 1
    responses:
      200:
        description: Servicio eliminado correctamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Servicio eliminado"
      404:
        description: No se encontró el servicio con el ID proporcionado
      500:
        description: Error interno o de recursión en el servidor
    """
    eliminado = svc_eliminar_servicio(id)
    if not eliminado:
        return jsonify({"error": "Servicio no encontrado"}), 404

    return jsonify({"mensaje": "Servicio eliminado"}), 200
