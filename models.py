from antioch import db
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, date, time, timedelta

class User(db.Model):
    """
    User model for Antioch
    """
    __tablename__ = users
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.SmallInteger)
    status = db.Column(db.SmallInteger)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def get_role(self):
        return self.role

    def get_status(self):
        return self.status

