from flask import Blueprint
from controllers.inscrip_controller import get_inscrip, insert_inscrip, get_listado
from controllers.cuentas_contoller import get_listado_pagos, get_pagos_montos, insertPago, deletePago, get_estado_cuenta

inscrip_routes = Blueprint('inscrip_routes', __name__)

@inscrip_routes.route('/api/inscripciones', methods=['GET'])
def get_inscrip_route():
    return get_inscrip()

@inscrip_routes.route('/api/insert/inscripcion', methods=['POST'])
def insert_inscrip_route():
    return insert_inscrip()

@inscrip_routes.route('/api/get/listado/<int:anio>/<int:grado>/<int:seccion>', methods=['GET'])
def get_listado_route(anio, grado, seccion):
    return get_listado(anio, grado, seccion)


@inscrip_routes.route('/api/get/pagos', methods=['GET'])
def get_pagos_rout():
    return get_pagos_montos()

@inscrip_routes.route('/api/insert/pago', methods=['POST'])
def insert_pago_route():
    return insertPago()


@inscrip_routes.route('/api/delete/pago/<Id>', methods=['DELETE'])
def delete_pago_route(Id):
    return deletePago(Id)

@inscrip_routes.route('/api/cuenta/<Id>', methods=['GET'])
def estado_cuenta_route(Id):
    return get_estado_cuenta(Id)