from flask import Blueprint, request, jsonify, make_response
from restful_api.models import User, users_schema, user_schema
from restful_api import db
from werkzeug.security import generate_password_hash, check_password_hash
from restful_api.config import Config 
from flask_jwt_extended import (jwt_optional, jwt_required, create_access_token, get_jwt_identity)
import uuid
import datetime, os



users = Blueprint('user', __name__)
        

@users.route("/", methods=['GET'])
@jwt_required
def home():
    current_user = get_jwt_identity()
    #all_user = User.query.all()
    
    return jsonify({"user" : current_user}), 200
    #return jsonify({"user" : users_schema.dump(all_user)}), 200

@users.route("/register", methods=['POST'])
def register():
    
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']


    hash_password = generate_password_hash(password, method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), username=username, email=email, password=hash_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message" : "user has been created!"}), 200


@users.route("/login", methods=['GET'])
def login():
    auth = request.authorization

    if  not auth or not auth.username or not auth.password:
        return make_response('Could not verify1', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'}) 

    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return make_response('Could not verify2', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'}) 

    if  check_password_hash(user.password, auth.password):
        acess_token = create_access_token(identity=user.email)
            #token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)

        return jsonify({'token': acess_token}), 200
            
    
    return make_response('Could not verify3', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})



   