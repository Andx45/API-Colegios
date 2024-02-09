from flask import jsonify, request
from models.inscrip_model import Inscripcion 
from flask_marshmallow import Marshmallow
from models.grado_model import db
from sqlalchemy import func, and_, text

ma = Marshmallow()

class InscripSchema(ma.Schema):
    class Meta:
        fields = ('IdInscrip', 'CodigoEstudiante', 'FechaInscrip', 'IdCiclo', 'IdGrado', 'IdSeccion')

inscrip_schema = InscripSchema()
inscrips_schema = InscripSchema(many=True)

def get_inscrip():
    all_inscrip = Inscripcion.query.all()
    result = inscrips_schema.dump(all_inscrip)
    return jsonify(result)   

def insert_inscrip():
    data = request.get_json()
    required_fields = ['CodigoEstudiante', 'FechaInscrip', 'IdCiclo', 'IdGrado', 'IdSeccion']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'El campo {field} es requerido'}), 400
        
    try:
        next_id = db.session.query(func.coalesce(func.max(Inscripcion.IdInscrip), 0) + 1).scalar()

        new_inscrip = Inscripcion(
            IdInscrip=next_id,
            CodigoEstudiante=data['CodigoEstudiante'],
            FechaInscrip=data['FechaInscrip'],
            IdCiclo=data['IdCiclo'],
            IdGrado=data['IdGrado'],
            IdSeccion=data['IdSeccion']
        )

        db.session.add(new_inscrip)
        db.session.commit()

        return jsonify({'message': 'Inscripcion registrada correctamente'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
def get_listado(anio, grado, seccion):
    query = text(f"""
    SELECT
        I.CODIGOESTUDIANTE,
        E.NOMBREEST,
        E.APELLIDOSEST
    FROM COLEGIOS_ADM.COL_INSCRIPCION I
    INNER JOIN COLEGIOS_ADM.COL_ESTUDIANTE E ON I.CODIGOESTUDIANTE = E.CODIGO
    WHERE EXTRACT(YEAR FROM I.FECHAINSCRIP) = {anio}
    AND I.IDGRADO = {grado}
    AND I.IDSECCION = {seccion}
    ORDER BY E.APELLIDOSEST ASC
    """)

    # Ejecuta la consulta
    with db.engine.connect() as connection:
        result = connection.execute(query)
        result = [dict(zip(result.keys(), row)) for row in result]

    return jsonify(result)
