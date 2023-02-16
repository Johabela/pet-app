from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(): 
# initialise flask app 
    app = Flask (__name__)

    # add configuration from object 
    app.config.from_object("config.app_config") # -> connecting from Main to app configuration on config.py 

    # @app.get("/")
    # def hello_world():
    #     return { "message": "hi there"}
    # return app 

    # BLUE PRINT 
    db.init_app(app)    #-> this is to initialise the app with the DATABASE
    ma.init_app(app)    #-> this is to initialise the app with the Marshmallow
    
#COMMUNICATING WITH THE APP 
    from commands.db import db_cmd 
    app.register_blueprint(db_cmd)




    from controller import registerable_controllers #-> connecting with __Init__ 
    for controller in registerable_controllers:
       app.register_blueprint(controller)
    
    return app 