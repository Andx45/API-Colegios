from flask_sqlalchemy import SQLAlchemy
from .grado_model import db

class Departamento(db.Model):
    __tablename__ = 'COL_DEPART'
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdDepart = db.Column('IDDEPART', db.Integer, primary_key=True)
    NombreDepart = db.Column('NOMBREDEPART', db.String(50))

class Municipio(db.Model):
    __tablename__ = 'COL_MUNIC'
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdMunic = db.Column('IDMUNIC', db.Integer, primary_key=True)
    IdDepart = db.Column('IDDEPART', db.Integer)
    NombreMunic = db.Column('NOMBREMUNIC', db.String(100))

