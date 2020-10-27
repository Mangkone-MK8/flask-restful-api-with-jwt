from flask_sqlalchemy import SQLAlchemy, Model
from restful_api import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, public_id, username, email, password):
        self.public_id= public_id
        self.username = username
        self.email = email
        self.password = password



class User_schema(ma.Schema):
    class Meta:
        fields = ("public_id", "username", "email", "password")
        model = User

'''class User_schema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        #field = ("public_id", "username", "email", "password")
    public_id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()'''



user_schema = User_schema()
users_schema = User_schema(many=True)


        
