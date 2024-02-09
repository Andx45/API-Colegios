from flask_sqlalchemy import SQLAlchemy
from .grado_model import db

class Pago(db.Model):
    __tablename__= "COL_REGISTRO_PAGOS"
    __table_args__ = {'schema': 'COLEGIOS_ADM'}
    IdPago = db.Column('IDPAGO', db.Integer, primary_key=True)
    IdBoleta = db.Column('IDBOLETA', db.String(10))
    CodigoEstudiante = db.Column('CODIGOESTUDIANTE', db.String(15))
    FechaPago = db.Column('FECHAPAGO', db.Date)
    IdConcepto = db.Column('IDCONCEPTO', db.Integer)
    