from flask import Blueprint, request
from controllers.estudiante_controller import getStudents, insertStudent, getStudent, deleteStudent, updateStudent

estudiante_routes = Blueprint('estudiante_routes', __name__)

@estudiante_routes.route('/api/estudiantes', methods=['GET'])
def get_students_route():
    return getStudents()

@estudiante_routes.route('/api/estudiante/<codigo>', methods=['GET'])
def get_student_route(codigo):
    return getStudent(codigo)

@estudiante_routes.route('/api/new/estudiante', methods=['POST'])
def insert_student_route():
    return insertStudent()

@estudiante_routes.route('/api/delete/estudiante/<codigo>', methods=['DELETE'])
def delete_student_route(codigo):
    return deleteStudent(codigo)

@estudiante_routes.route('/api/update/estudiante/<codigo>', methods=['PUT'])
def update_student_route(codigo):
    return updateStudent(codigo)