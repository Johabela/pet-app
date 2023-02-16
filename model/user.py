#SINGLE model NOT PLURAL for file name conventions inside CONTROLLER 

from flask_sqlalchemy import db #- > getting the DATABASE from main.py 

class user (db.model):
    ___tablename__ = "users" 


    id = db.Column (db.Integer(), primary_key=True)

    username = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean())
    mobile_number =db.Column(db.String())  # -->user string for bank account , crypto address , long number, postcode  
    post_code = db.Column(db.String())
class User(db.Model):
    ___tablename__ = "users" 


    id = db.Column(db.String(), nullable )
