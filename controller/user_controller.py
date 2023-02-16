from flask import Blueprint
from model.user import User  #-> bring the model user to conect here this file 
from schema.users_schema import user_schema, users_schema #-> this is the path connecting or bringing the USER SCHEMA 

home = Blueprint("user", __name__, url_prefix="/users") #-> it is connected with the user from user.py MODEL FOLDER

@home.get("/")
def get_users():
    users = User.query.all()
    return user_schema.dump(users) #-> It goes connected with SCHEMA 