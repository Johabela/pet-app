from flask import Blueprint

home = Blueprint("home", __name__, url_prefix="/") #-> it is connected with the user from user.py MODEL FOLDER

@home.get("/")
def get_home_page():
    return {"message": "Hello HOME PAGE"}


# from main import ma

# class UserSchema(ma.Schema):
#     class Meta:

#         field = ("id", "username" "verified", 
#                  "mobile" , "post_code")
        

# user_schema = UserSchema ()