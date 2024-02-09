from flask import jsonify, request
from flask_marshmallow import Marshmallow
from models.pagos_model import Pago
from models.grado_model import db
from sqlalchemy import func, and_, text
from datetime import datetime

ma = Marshmallow()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('IdPago', 'IdBoleta', 'CodigoEstudiante', 'FechaPago')

pago_Schema = PagosSchema()
pagos_Schema = PagosSchema(many  = True)


def insertPago():
    data = request.get_json()
    required_fields = ['IdBoleta', 'CodigoEstudiante', 'FechaPago', 'TipoPago']
    
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'El campo {field} es requerido'}), 400
        
    try:
        next_id = db.session.query(func.coalesce(func.max(Pago.IdPago), 0) + 1).scalar()

        new_pago = Pago(
            IdPago=next_id,
            IdBoleta=data['IdBoleta'],
            CodigoEstudiante=data['CodigoEstudiante'],
            FechaPago=data['FechaPago'],
            IdConcepto = data['TipoPago']
        )

        db.session.add(new_pago)
        
        db.session.execute(
            text("INSERT INTO \"COLEGIOS_ADM\".\"COL_CUENTA_EST\" (\"CODIGO\", \"FECHAMOV\", \"IDMOV\", \"IDCONCEPTO\") "
                "VALUES (:codigo, :fecha_mov, 2, :id_concepto)"),
            {
                "codigo": data['CodigoEstudiante'],  
                "fecha_mov": data['FechaPago'], 
                "id_concepto": data['TipoPago'],              
            }
        )

        db.session.commit()
        return jsonify({'message': 'Pago registrada correctamente'}), 201
    except Exception as e:
        print(f'Error en la API: {str(e)}')
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


def get_listado_pagos():
    query = text("""
    SELECT E.CODIGO, E.NOMBREEST, E.APELLIDOSEST
    FROM COLEGIOS_ADM.COL_ESTUDIANTE E
    INNER JOIN COLEGIOS_ADM.COL_REGISTRO_PAGOS RP ON E.CODIGO = RP.CODIGOESTUDIANTE
    """)
    

    with db.engine.connect() as connection:
        result = connection.execute(query)
        result = [dict(zip(result.keys(), row)) for row in result]

    return jsonify(result)


def get_pagos_montos():
    query = text("""
                 
   SELECT RP.IDPAGO, 
    TO_CHAR(RP.FECHAPAGO, 'DD/MM/YYYY') AS FECHAPAGO,
    RP.CODIGOESTUDIANTE,
    CP.NOMBRE,
    CP.MONTO,
    RP.IDBOLETA
    FROM COLEGIOS_ADM.COL_REGISTRO_PAGOS RP
    JOIN COLEGIOS_ADM.COL_CONC_PAGOS CP
    ON RP.IDCONCEPTO = CP.IDCONCEPTO
    """)
    

    with db.engine.connect() as connection:
        result = connection.execute(query)
        result = [dict(zip(result.keys(), row)) for row in result]

    return jsonify(result)


def deletePago(Id):
    pagoEliminar = Pago.query.filter_by(IdPago=Id).first()
    if pagoEliminar:
        db.session.delete(pagoEliminar)
        db.session.commit()
        return jsonify({'message': 'Pago eliminado correctamente'}), 200
    else:
        return jsonify({'message': 'Pago no encontrado'}), 404
    

def get_estado_cuenta(Id):
    query = text(f"""
        SELECT
        TO_CHAR(CUENTA.FECHAMOV, 'DD/MM/YYYY') AS FECHAMOV, 
        MOV.DETALLE,
        CONCE.NOMBRE,
        CUENTA.MONTO,
        CUENTA.SALDO
        FROM COLEGIOS_ADM.COL_CUENTA_EST CUENTA
        JOIN COLEGIOS_ADM.COL_MOVIMIENTOS MOV ON CUENTA.IDMOV = MOV.IDMOV
        JOIN COLEGIOS_ADM.COL_CONC_PAGOS CONCE ON CUENTA.IDCONCEPTO = CONCE.IDCONCEPTO
        WHERE CODIGO = \'{Id}\'
        ORDER BY CUENTA.IDCUENTAEST ASC
    """)

    with db.engine.connect() as connection:
        result = connection.execute(query)
        result = [dict(zip(result.keys(), row)) for row in result]

    return jsonify(result)


