
from flask import Flask, make_response, jsonify 
from flask_migrate import Migrate

from models import db, Earthquake 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()

    if earthquake:
       
        response_body = earthquake.to_dict()
        return make_response(response_body, 200)
    else:
        response_body = {"message": f"Earthquake {id} not found."}
        return make_response(response_body, 404)



@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    
    quakes_data = [quake.to_dict() for quake in quakes]
    
    response_body = {
        "count": len(quakes_data),
        "quakes": quakes_data
    }
    return make_response(response_body, 200)




if __name__ == '__main__':
    app.run(port=5555, debug=True)