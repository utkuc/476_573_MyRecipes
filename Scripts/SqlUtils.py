from Scripts.Models import User,Menu,MenuRate,Ingredient,Recipe,Category
from flask import Flask, jsonify, make_response, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError


from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class SqlUtils:
    def Insert(self, source: object):
        localvar = db.engine.raw_connection().cursor().var(
            int)  # Required for getting id after Insertion(Works only for cx_Oracle)
        typeofSource=str(type(source)).lower()
        if typeofSource == "user".lower():
            source: User

            sql = """
                    INSERT INTO "user" (email,username,password,fname,mname,lname,registerdate)
                    VALUES(:emailval,:usernameval, :passwordval,:fnameval,:mnameval,:lnameval,:registerdateval)
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'emailval': source.email, 'usernameval': source.username,
                                               'passwordval': source.password,
                                               'fnameval': source.fname, 'mnameval': source.mname, 'lnameval': source.lname,
                                               'registerdateval': source.registerdate, 'localvar': localvar})
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1
        if typeofSource == "recipe".lower():
            source: Recipe
            sql = """
                    INSERT INTO "RECIPE" (direction,fat,date,calories,description,protein,rating,title,ingredientList,ingredientDescription,sodium,categoryName)
                    VALUES(:direction,:fat, :date,:calories,:description,:protein,:rating, :title,:ingredientList,:ingredientDescription,:sodium,:categoryName )
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'direction': source.direction, 'fat': source.fat,
                                               'date': source.date,
                                               'calories': source.calories, 'description': source.description,
                                               'protein': source.protein,
                                               'rating': source.rating, 'title': source.title,
                                               'ingredientList': source.ingredientList,
                                               'ingredientDescription': source.ingredientDescription,
                                               'sodium': source.sodium,'categoryName': source.categoryName})
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1
        if typeofSource == "Menu".lower():
            source: Menu
            sql = """
                    INSERT INTO "MENU" (uId,recipeList,name)
                    VALUES(:uId,:recipeList, :name)
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'uId': source.uId, 'recipeList': source.recipeList,
                                               'name': source.name
                                               })
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1
        if typeofSource == "Category".lower():
            source: Category
            sql = """
                    INSERT INTO "Category" (name)
                    VALUES(:name)
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'name': source.name
                                               })
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1
        if typeofSource == "Ingredient".lower():
            source: Ingredient
            sql = """
                    INSERT INTO "Ingredient" (name)
                    VALUES(:name)
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'name': source.name
                                               })
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1
        if typeofSource == "MenuRate".lower():
            source: MenuRate
            sql = """
                    INSERT INTO "MenuRate" (menuId,uId,rate)
                    VALUES(:menuId,:uId, :rate)
                    RETURNING ID INTO :localvar
                    """
            try:
                db.session.execute(text(sql), {'menuId': source.menuId, 'uId': source.uId,
                                               'rate': source.rate
                                               })
                db.session.commit()
                source.id = localvar.getvalue()[0]
                return source.id

            except IntegrityError as e:
                db.session.rollback()
                return -1


