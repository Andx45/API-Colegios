from flask import jsonify, request
from models.datasel_model import Departamento, Municipio
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class DepartamentoSchema(ma.Schema):
    class Meta:
        fields = ('IdDepart', 'NombreDepart')

class MunicipioSchema(ma.Schema):
    class Meta:
        fields = ('IdMunic', 'IdDepart', 'NombreMunic')

depart_schema = DepartamentoSchema()
departs_schema = DepartamentoSchema(many=True)

munic_schema = MunicipioSchema()
munics_schema = MunicipioSchema(many=True)

def getDepart():
    all_departs = Departamento.query.all()
    result = departs_schema.dump(all_departs)
    return jsonify(result)

def getMunic(IdDepart):
    all_munics = Municipio.query.filter_by(IdDepart=IdDepart).all()
    result = munics_schema.dump(all_munics)
    return jsonify(result)
