from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Usuario import Usuario
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from db import db

sesion = Blueprint('sesion', __name__)

@sesion.route('/Sesion', methods = ['POST']) #cambiar el nombre del CUS
def Validar_Sesion():
    username = request.json.get('username') 
    contraseña = request.json.get('contraseña')
    print(username)

    usuario = Usuario.query.filter_by(username = username).first()
    print(usuario)
    if not usuario:
        return make_response(jsonify({"message": "Usuario no encontrado"}), 404)    
    print(usuario.contraseña)

    # Verificar la contraseña
    if not check_password_hash(usuario.contraseñahash, contraseña):
        return make_response(jsonify({"message": "Contraseña incorrecta"}), 401)
    
    acces_token = create_access_token(identity=username)
    
    return make_response(jsonify(token = acces_token), 201)    


#Temporal
@sesion.route('/CrearUsuario', methods = ['POST'])
def Generar_contrasenia():
    username = request.json.get('username') 
    contraseña = request.json.get('contraseña')
    

    # Hashea la contraseña generada
    contraseñahash= generate_password_hash(contraseña)  
      

    new_usuario = Usuario(username, contraseña, contraseñahash)
    db.session.add(new_usuario)
    db.session.commit()

    data = {
        'message': 'Usuario registrado',
        'status': 201
    }

    return make_response(jsonify(data),201)

