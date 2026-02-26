from .pacientes import pacientes_bp
from .citas import citas_bp
from .consultorios import consultorios_bp
from .doctores import doctores_bp
from .servicios import servicios_bp
# from .facturas import facturas_bp
# from .productos import productos_bp

def cargarRutas(app):
    app.register_blueprint(pacientes_bp, url_prefix="/pacientes")
    app.register_blueprint(citas_bp, url_prefix="/citas")
    app.register_blueprint(consultorios_bp, url_prefix="/consultorios")
    app.register_blueprint(doctores_bp, url_prefix="/doctores")
    app.register_blueprint(servicios_bp, url_prefix="/servicios")
    # app.register_blueprint(facturas_bp, url_prefix="/x")
    # app.register_blueprint(facturas_bp, url_prefix="/y")
    # app.register_blueprint(facturas_bp, url_prefix="/z")
    # app.register_blueprint(facturas_bp, url_prefix="/y")