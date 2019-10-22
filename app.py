# Main Application
from flask import Flask, jsonify, make_response, render_template, abort
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse, fields, marshal_with, marshal
from flask_restful.fields import DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from config import DevConfig  # Import sequence matters!

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
api = Api(app)
auth = HTTPBasicAuth()
from Scripts.Models import User


def initDatabase():  # Delete All Tables, Create tables according to Model Imports
    db.drop_all()
    db.create_all()
    db.session.commit()


initDatabase()

users = {  #  Test user for api calls
    "db_admin": generate_password_hash("123456789")
}

#  Api calls can be made by username-password
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'password': fields.String,
    'fname': fields.String,
    'mname': fields.String,
    'lname': fields.String,
    'registerdate': fields.DateTime(dt_format='rfc822'),
}


class UserAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=False,
                                   help='No id provided',
                                   location='json')
        self.reqparse.add_argument('email', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username provided',
                                   location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        self.reqparse.add_argument('fname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('mname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('lname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('registerdate', type=DateTime, default="",
                                   location='json')
        super(UserAPI, self).__init__()
    #Get Example: Get User with id
    @marshal_with(user_fields, envelope='User')
    def get(self, user_id):
        return User.query.from_statement(db.text('SELECT * FROM "user" WHERE id=:val')). \
            params(val=user_id).first_or_404(description='There is no data with {}'.format(user_id))


class UserList(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, default="", required=False,
                                   location='json')
        self.reqparse.add_argument('email', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username provided',
                                   location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        self.reqparse.add_argument('fname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('mname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('lname', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('registerdate', type=DateTime, default="",
                                   location='json')
        super(UserList, self).__init__()
    #Post Example(RAW SQL): Create user with given info, Id will be auto generated.
    def post(self):
        localvar = db.engine.raw_connection().cursor().var(int) # Required for getting id after Insertion(Works only for cx_Oracle)

        args = self.reqparse.parse_args()
        user = User(email=args['email'], username=args['username'], password=args['password'],
                    fname=args['fname'], mname=args['mname'], lname=args['lname'], registerdate=args['registerdate'])
        sql = """
        INSERT INTO "user" (email,username,password,fname,mname,lname,registerdate)
        VALUES(:emailval,:usernameval, :passwordval,:fnameval,:mnameval,:lnameval,:registerdateval)
        RETURNING ID INTO :localvar
        """
        #Try to create user, if database gives Integrity Error(eg. unique user name) rollback and abort
        try:
            db.session.execute(text(sql),{'emailval':user.email, 'usernameval':user.username,
                                                       'passwordval':user.password,
                                                       'fnameval':user.fname, 'mnameval':user.mname, 'lnameval':user.lname,
                                                       'registerdateval':user.registerdate, 'localvar':localvar} )
            db.session.commit()
            user.id = localvar.getvalue()[0]

        except IntegrityError as e:
            db.session.rollback()
            abort(409, str(e.orig) + " for parameters " + str(e.params))
        #### How to manage INSERT without RAW SQL:
        # db.session.add(user)
        # try:
        #     db.session.commit()
        # except IntegrityError as e:
        #     db.session.rollback()
        #     abort(409, str(e.orig) + " for parameters " + str(e.params))
        return marshal(user, user_fields), 201

# Applicaton Routes:
api.add_resource(UserAPI, '/api/users/<int:user_id>')
api.add_resource(UserList, '/api/users')

if __name__ == '__main__':
    app.run()
