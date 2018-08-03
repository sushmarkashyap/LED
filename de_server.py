from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sushma:Sushsama.19@localhost/IOT'
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column('id', db.Integer, primary_key=True)
	full_name = db.Column('Full Name', db.Unicode)
    email = db.Column('E-mail', db.Unicode)
    password = db.Column('Password', db.Unicode)

    def __init__(self,id, full_name, email, password):
        self.id=id
        self.full_name=full_name
        self.email=email
        self.password=password

@app.route('/' methods=['GET'])


