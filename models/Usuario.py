from db import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    contraseña = db.Column(db.String)
    contraseñahash = db.Column(db.String)

    def __init__(self, username, contraseña, contraseñahash):
        self.username = username
        self.contraseña = contraseña
        self.contraseñahash = contraseñahash