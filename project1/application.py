import os

from flask import Flask, session, render_template, request

from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# __name__
# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")
#
# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
#
# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods =['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form['uname']
        psw = request.form['psw']
        data = {'username': username, 'psw': psw}
        return render_template('create_login.html', data = data)
    else:
        return render_template('index.html')
