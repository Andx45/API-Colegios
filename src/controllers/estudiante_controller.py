from flask import jsonify, request
from models.estudiante_model import Estudiante, Sexo
from flask_marshmallow import Marshmallow
from models.grado_model import db
from datetime import datetime

ma = Marshmallow()

class EstudianteSchema(ma.Schema):
    class Meta:
        fields = ('Codigo', 'Nombres', 'Apellidos', 'FechaNac', 'IdSexo', 'IdDepart', 'IdMunic', 'Direccion')

estudiante_Schema = EstudianteSchema()
estudiantes_Schema = EstudianteSchema(many  = True)

def getStudents():
    all_students = Estudiante.query.all()
    result = estudiantes_Schema.dump(all_students)
    return jsonify(result)

def getStudent(codigo):
    student_data = db.session.query(Estudiante.Codigo, Estudiante.Nombres, Estudiante.Apellidos, 
        Estudiante.FechaNac, Estudiante.IdSexo, Sexo.NombreSexo, Estudiante.IdDepart, Estudiante.IdMunic, Estudiante.Direccion) \
        .join(Sexo, Estudiante.IdSexo == Sexo.IdSexo) \
        .filter(Estudiante.Codigo == codigo) \
        .first()

    if student_data:
        student = {
            "Codigo": student_data[0],
            "Nombres": student_data[1],
            "Apellidos": student_data[2],
            "FechaNac": student_data[3].strftime("%Y-%m-%d") if student_data[3] else None,
            "IdSexo": student_data[4],
            "NombreSexo": student_data[5],
            "IdDepart": student_data[6],
            "IdMunic": student_data[7],
            "Direccion": student_data[8]
        }
        return jsonify(student)
    else:
        return jsonify({'message': 'Estudiante no encontrado'}), 404


def insertStudent():
    data = request.get_json()
    required_fields = ['Codigo', 'Nombres', 'Apellidos', 'FechaNac', 'IdSexo', 'IdDepart', 'IdMunic']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'El campo {field} es requerido'}), 400

    try:
        new_student = Estudiante(
            Codigo=data['Codigo'],
            Nombres=data['Nombres'],
            Apellidos=data['Apellidos'],
            FechaNac=data['FechaNac'],
            IdSexo=data['IdSexo'],
            IdDepart=data['IdDepart'],
            IdMunic=data['IdMunic'],
            Direccion=data['Direccion']
        )

        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'Estudiante insertado correctamente'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
def deleteStudent(codigo):
    student = Estudiante.query.filter_by(Codigo=codigo).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Estudiante eliminado correctamente'}), 200
    else:
        return jsonify({'message': 'Estudiante no encontrado'}), 404

def updateStudent(codigo):
    estudiante = Estudiante.query.filter_by(Codigo=codigo).first()

    if not estudiante:
        return jsonify({'message': 'Estudiante no encontrado'}), 404

    datos = request.get_json()  

    estudiante.Nombres = datos['Nombres']
    estudiante.Apellidos = datos['Apellidos']
    estudiante.FechaNac = datos['FechaNac']
    estudiante.IdSexo = datos['IdSexo']
    estudiante.IdDepart = datos['IdDepart']
    estudiante.IdMunic = datos['IdMunic']
    estudiante.Direccion = datos['Direccion']

    db.session.commit()  

    return estudiante_Schema.jsonify(estudiante)

