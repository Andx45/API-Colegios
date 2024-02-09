from flask import Blueprint, request
from controllers.datasel_controller import getDepart, getMunic

datasel_routes = Blueprint('datasel_routes', __name__)

@datasel_routes.route('/api/departamentos', methods=['GET'])
def get_depart_route():
    return getDepart()

@datasel_routes.route('/api/municipios/<int:IdDepart>', methods=['GET'])
def get_munic_route(IdDepart):
    return getMunic(IdDepart)