from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from models.grado_model import db
from routes.grado_routes import grado_routes
from routes.estudiante_routes import estudiante_routes
from routes.datasel_routes import datasel_routes
from routes.inscrip_routes import inscrip_routes

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://localhost:44377"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://COLEGIOS_CRUD:crudpasCo123@localhost:1521/xe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma = Marshmallow(app)

app.register_blueprint(grado_routes)
app.register_blueprint(estudiante_routes)
app.register_blueprint(datasel_routes)
app.register_blueprint(inscrip_routes)

if __name__ == '__main__':
    app.run(port=5000, debug=True)