from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GradoSec(db.Model):
    __tablename__ = "COL_GRADO_SEC"
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdGradoSec = db.Column('IDGRADOSEC', db.Integer, primary_key=True)
    IdCiclo = db.Column('IDCICLO', db.Integer)
    IdGrado = db.Column('IDGRADO', db.Integer)
    IdSeccion = db.Column('IDSECCION', db.Integer)
    Anio = db.Column('ANIO', db.Integer)

class Ciclo(db.Model):
    __tablename__ = "COL_CICLO"
    __table_args__ = {'schema': 'COLEGIOS_ADM'} 
    IdCiclo = db.Column('IDCICLO', db.Integer, primary_key=True)
    Detalle = db.Column('DETALLE', db.String(100))

class Seccion(db.Model):
    __tablename__ = "COL_SECCION"
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdSeccion = db.Column('IDSECCION', db.Integer, primary_key = True)
    Detalle = db.Column('DETALLE', db.String(1))

class Grado(db.Model):
    __tablename__ = "COL_GRADO"
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdGrado = db.Column('IDGRADO', db.Integer, primary_key = True)
    IdCiclo = db.Column('IDCICLO', db.Integer)
    Detalle = db.Column('DETALLE', db.String(150))
