from flask import Flask


def create_app(): 
# initialise flask app 
    app = Flask (__name__)

    # add configuration from object 
    app.config.from_object("config.app_config") # -> connecting from Main to app configuration on config.py 

    @app.get("/")
    def hello_world():
        return { "message": "hi there"}
    
    return app 
