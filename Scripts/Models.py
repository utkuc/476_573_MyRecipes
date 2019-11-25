from datetime import datetime

from app import db
from sqlalchemy.schema import Sequence

# id_seq is required for auto id generation(cx_Oracle)
id_seq = Sequence('id_seq')

ingredientList = db.Table('Ingredient_List',
                          db.Column('Ingredient_name', db.String(255), db.ForeignKey('INGREDIENT.name')),
                          db.Column('Recipe_id', db.Integer(), db.ForeignKey('RECIPE.id'))
                          )
categoryList = db.Table('Category_List',
                        db.Column('Category_name', db.String(255), db.ForeignKey('CATEGORY.name')),
                        db.Column('Recipe_id', db.Integer(), db.ForeignKey('RECIPE.id'))
                        )


class User(db.Model):
    __tablename__ = 'USER'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    mname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    registerdate = db.Column(db.DateTime())
    menus = db.relationship('Menu', backref='USER', lazy=True)


class Recipe(db.Model):
    __tablename__ = 'RECIPE'
    id = db.Column(db.Integer(), primary_key=True)
    direction = db.Column(db.String(255))
    fat = db.Column(db.Integer())
    date = db.Column(db.DateTime(timezone=True))
    calories = db.Column(db.Integer())
    description = db.Column(db.String(255))
    protein = db.Column(db.Integer())
    rating = db.Column(db.Integer(),nullable=False)
    title = db.Column(db.String(255))
    ingredientList = db.relationship('Ingredient', secondary=ingredientList, lazy='subquery',
                                     backref=db.backref('Recipes', lazy=True))
    ingredientDescription = db.Column(db.String(255))
    sodium = db.Column(db.Integer())
    categoryList = db.relationship('Category', secondary=categoryList, lazy='subquery',
                                   backref=db.backref('Categories', lazy=True))


class Menu(db.Model):
    __tablename__ = 'MENU'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey('USER.id'), nullable=False)
    recipeList = db.Column(db.String(255))
    name = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'CATEGORY'
    name = db.Column(db.String(255), primary_key=True)


class Ingredient(db.Model):
    __tablename__ = 'INGREDIENT'
    name = db.Column(db.String(255), primary_key=True)


class MenuRate(db.Model):
    __tablename__ = 'MENURATE'
    id = db.Column(db.Integer(), id_seq,
                   server_default=id_seq.next_value(), primary_key=True)
    menuId = db.Column(db.Integer(), db.ForeignKey('MENU.id'), nullable=False)
    userId = db.Column(db.Integer(), db.ForeignKey('USER.id'), nullable=False)
    rate = db.Column(db.Integer())

class Review(db.Model):
    __tablename__ = "REVIEW"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), db.ForeignKey('USER.username'), nullable=False)
    rating = db.Column(db.Float())
    comments = db.Column(db.String(255))
    recipeid = db.Column(db.Integer(), db.ForeignKey('RECIPE.id'), nullable=False)
