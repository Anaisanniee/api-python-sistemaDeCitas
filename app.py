from flask import Flask
from routes import cargarRutas
from flask_mysqldb import MySQL
from config import Config
from flasgger import Swagger

# Inicializamos MySQL de forma global (se configura dentro de create_app)
mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicialización de extensiones
    swagger_config = {
        "swagger": "2.0",
        "info": {
            "title": "Sistema de Gestión de Citas Médicas", # El nombre que desees
            "description": "API para la administración de servicios, pacientes y doctores",
            "version": "1.0.0",
            "contact": {
                "name": "Soporte Técnico",
                "email": "tu-correo@ejemplo.com"
            }
        },
        "specs_route": "/apidocs/" # Ruta donde se verá el Swagger
    }
    
    # Pasamos el diccionario 'template' a Swagger
    Swagger(app, template=swagger_config)
    mysql.init_app(app) # Importante para que los controladores funcionen
    
    # Carga de rutas
    cargarRutas(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    # Solo un app.run y dentro del bloque main
    app.run(debug=True, port=4000)