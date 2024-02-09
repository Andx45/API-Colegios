from flask import Blueprint, request
from controllers.grado_contoller import get_cicles, get_sections, insert_section, get_gradoSec, get_grados, get_grados_ciclo

grado_routes = Blueprint('grado_routes', __name__)

@grado_routes.route('/api/ciclos', methods=['GET'])
def get_cicles_route():
    return get_cicles()

@grado_routes.route('/api/secciones', methods = ['GET'])
def get_sections_route():
    return get_sections()

@grado_routes.route('/insert/section', methods = ['POST'])
def insert_section_route():
    return insert_section()

@grado_routes.route('/grados_secciones', methods = ['GET'])
def get_grad_sec():
    return get_gradoSec()

@grado_routes.route('/grados', methods=['GET'])
def get_grados_route():
    return get_grados()

@grado_routes.route('/api/grados/ciclo/<int:id_ciclo>', methods=['GET'])
def grados_por_ciclo(id_ciclo):
    return get_grados_ciclo(id_ciclo)

