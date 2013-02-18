from flask import Flask, g, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

#Create and specify config file for our app
app = Flask(__name__)
app.config.from_object('config')


#create our SQLAlchemy database ORM
db = SQLAlchemy(app)
db.init_app(app)

#Create Login manager
lm = LoginManager()
lm.setup_app(app)

import models, views

@app.before_request
def before_request():
    g.db = db

if __name__ == '__main__':
    app.run()   
