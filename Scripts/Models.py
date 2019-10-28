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

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    direction = db.Column(db.String(255))
    fat = db.Column(db.Integer())
    date = db.Column(db.DateTime(timezone=True))
    calories = db.Column(db.Integer())
    description = db.Column(db.String(255))
    protein = db.Column(db.Integer())
    rating = db.Column(db.Integer())
    title = db.Column(db.String(255))
    ingredientList = db.Column(db.String(255))
    ingredientDescription = db.Column(db.String(255))
    sodium = db.Column(db.Integer())
    categoryName = db.Column(db.String(255))

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    uId = db.Column(db.Integer())
    recipeList = db.Column(db.String(255))
    name = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'category'
    name = db.Column(db.String(255), primary_key=True)

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    name = db.Column(db.String(255), primary_key=True)

class MenuRate(db.Model):
    __tablename__ = 'menurate'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    menuId = db.Column(db.Integer())
    uId = db.Column(db.Integer())
    rate = db.Column(db.Integer())


