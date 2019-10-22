from app import db
from sqlalchemy.schema import Sequence
#id_seq is required for auto id generation(cx_Oracle)
id_seq = Sequence('id_seq')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    mname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    registerdate = db.Column(db.DateTime(timezone=True))
