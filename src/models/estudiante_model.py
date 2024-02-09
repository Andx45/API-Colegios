from flask_sqlalchemy import SQLAlchemy
from .grado_model import db

class Estudiante(db.Model):
    __tablename__='COL_ESTUDIANTE'
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    Codigo = db.Column('CODIGO', db.String(15), primary_key=True)
    Nombres = db.Column('NOMBREEST', db.String(150))
    Apellidos = db.Column('APELLIDOSEST', db.String(150))
    FechaNac = db.Column('FECHANAC', db.Date)
    IdSexo = db.Column('IDSEXO', db.Integer)
    IdDepart = db.Column('IDDEPART', db.Integer)
    IdMunic = db.Column('IDMUNIC', db.Integer)
    Direccion = db.Column('DIRECCION', db.String(300))

class Sexo(db.Model):
    __tablename__='COL_SEXO'
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdSexo = db.Column('IDSEXO', db.Integer, primary_key = True)
    NombreSexo = db.Column('NOMBRESEXO', db.String(20))