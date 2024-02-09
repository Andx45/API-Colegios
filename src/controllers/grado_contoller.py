from flask import jsonify, request
from models.grado_model import Ciclo, Seccion, GradoSec, Grado, db  
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CicloSchema(ma.Schema):
    class Meta:
        fields = ('IdCiclo', 'Detalle')

class SeccionSchema(ma.Schema):
    class Meta:
        fields = ('IdSeccion', 'Detalle')

class GradoSchema(ma.Schema):
    class Meta:
        fields = ('IdGrado', 'IdCiclo', 'Detalle')

class GradoSecSchema(ma.Schema):
    class Meta:
        fields = ('IdGradoSec', 'IdCiclo', 'IdGrado', 'IdSeccion', 'Anio')

gradsec_schema = GradoSecSchema()
gradsecs_schema = GradoSecSchema(many = True)

ciclo_schema = CicloSchema()
ciclos_schema = CicloSchema(many=True)

grado_schema = GradoSchema()
grados_schema = GradoSchema(many = True)

seccion_schema = SeccionSchema()
secciones_schema = SeccionSchema(many = True)

def get_cicles():
    all_cicles = Ciclo.query.all()
    result = ciclos_schema.dump(all_cicles)
    return jsonify(result)

def get_sections():
    all_sections = Seccion.query.all()
    result = secciones_schema.dump(all_sections)
    return jsonify(result)

def get_gradoSec():
    all_gradsec = GradoSec.query.all()
    result = gradsecs_schema.dump(all_gradsec)
    return jsonify(result)

def get_grados():
    all_grados = Grado.query.all()
    result = grados_schema.dump(all_grados)
    return jsonify(result)

def get_grados_ciclo(id_ciclo):
    grados = Grado.query.filter_by(IdCiclo=id_ciclo).all()
    result = grados_schema.dump(grados)
    return jsonify(result)

def insert_section():
    try:
        data = request.json
        IdSeccion = data['id']
        detalle = data['detalle']
        new_section = Seccion(IdSeccion = IdSeccion, Detalle = detalle)
        db.session.add(new_section)
        db.session.commit()
        return jsonify({'status': 'Agregado correctamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})