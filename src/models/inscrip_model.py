from flask_sqlalchemy import SQLAlchemy
from .grado_model import db

class Inscripcion(db.Model):
    __tablename__= "COL_INSCRIPCION"
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdInscrip = db.Column('IDINSCRIP', db.Integer, primary_key=True)
    CodigoEstudiante = db.Column('CODIGOESTUDIANTE', db.String(15))
    FechaInscrip = db.Column('FECHAINSCRIP', db.Date)
    IdCiclo = db.Column('IDCICLO', db.Integer)
    IdGrado = db.Column('IDGRADO', db.Integer)
    IdSeccion = db.Column('IDSECCION', db.Integer)