from flask import Blueprint
from main import db

db_cmd = Blueprint("db", __name__)

@db_cmd.cli.command("create")
def create_db(): #-> 
    db.create_all()
    print ("Table are created yeyy")


@db_cmd.cli.command("drop")
def drop_db(): #-> 
    db.drop_all()
    print ("Table are dropped, oh no! ")
