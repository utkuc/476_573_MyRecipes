from collections import namedtuple

from Scripts.Models import User, Menu, MenuRate, Ingredient, Recipe, Category
from flask import Flask, jsonify, make_response, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


# noinspection SqlResolve
class SqlUtils:

    def Insert(self, source: object):
        localvar = db.engine.raw_connection().cursor().var(
            int)  # Required for getting id after Insertion(Works only for cx_Oracle)

        if isinstance(source, User):
            source: User

            sql = """
                    INSERT INTO "USER" (email,username,password,fname,mname,lname,registerdate)
                    VALUES(:emailval,:usernameval, :passwordval,:fnameval,:mnameval,:lnameval,:registerdateval)
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'emailval': source.email, 'usernameval': source.username,
                                           'passwordval': source.password,
                                           'fnameval': source.fname, 'mnameval': source.mname,
                                           'lnameval': source.lname,
                                           'registerdateval': source.registerdate, 'localvar': localvar})
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source
        if isinstance(source, Recipe):
            source: Recipe
            sql = """
                    INSERT INTO "RECIPE" (direction,fat,"date",calories,description,protein,rating,title,ingredientList,ingredientDescription,sodium,categoryName)
                    VALUES(:direction,:fat, :"date",:calories,:description,:protein,:rating, :title,:ingredientList,:ingredientDescription,:sodium,:categoryName )
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'direction': source.direction, 'fat': source.fat,
                                           'date': source.date,
                                           'calories': source.calories, 'description': source.description,
                                           'protein': source.protein,
                                           'rating': source.rating, 'title': source.title,
                                           'ingredientList': source.ingredientList,
                                           'ingredientDescription': source.ingredientDescription,
                                           'sodium': source.sodium, 'categoryName': source.categoryName})
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source

        if isinstance(source, Menu):
            source: Menu
            sql = """
                    INSERT INTO "MENU" (uId,recipeList,name)
                    VALUES(:uId,:recipeList, :name)
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'uId': source.uId, 'recipeList': source.recipeList,
                                           'name': source.name
                                           })
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source
        if isinstance(source, Category):
            source: Category
            sql = """
                    INSERT INTO "Category" (name)
                    VALUES(:name)
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'name': source.name
                                           })
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source

        if isinstance(source, Ingredient):
            source: Ingredient
            sql = """
                    INSERT INTO "Ingredient" (name)
                    VALUES(:name)
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'name': source.name
                                           })
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source

        if isinstance(source, MenuRate):
            source: MenuRate
            sql = """
                    INSERT INTO "MenuRate" (menuId,uId,rate)
                    VALUES(:menuId,:uId, :rate)
                    RETURNING ID INTO :localvar
                    """
            db.session.execute(text(sql), {'menuId': source.menuId, 'uId': source.uId,
                                           'rate': source.rate
                                           })
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source

    def Delete(self, source: object) -> bool:
        typeofSource = source.__class__.__name__
        if isinstance(source, User):
            source: User

            sql = """
                            DELETE FROM :sourceType
                            WHERE  id = :sourceid
                            """

            db.session.execute(text(sql), {'sourceType': typeofSource, 'sourceid': source.id})
            db.session.commit()
            return True

    def GetModelWithID(self, tablename: str, id: int):
        if(tablename.lower() == "USER".lower()):
            sql = """
                            SELECT *
                            FROM "USER"
                            WHERE  id = :val
                            """
            result = User()
        elif (tablename.lower() == "MENU".lower()):
            sql = """
                            SELECT *
                            FROM "MENU"
                            WHERE  id = :val
                            """
            result = Menu()

        elif (tablename.lower() == "RECIPE".lower()):
            sql = """
                            SELECT *
                            FROM RECIPE
                            WHERE  id = :val
                            """
            result =Recipe()
        elif (tablename.lower() == "MENURATE".lower()):
            sql = """
                            SELECT *
                            FROM MENURATE
                            WHERE  id = :val
                            """
            result = MenuRate()
        else:
            return None
        resultProxy = db.session.execute(text(sql), {'val': id})
        db.session.commit()
        for r in resultProxy:
            r_dict = dict(r.items())
        for att in r_dict:
            result.__setattr__(att, r_dict[att])
        return result
    def GetModelWithName(self, tablename: str, name: str):
        if(tablename.lower() == "CATEGORY".lower()):
            sql = """
                            SELECT *
                            FROM CATEGORY
                            WHERE  name = :val
                            """
            result = Category()
        elif(tablename.lower() == "INGREDIENT".lower()):
            sql = """
                            SELECT *
                            FROM INGREDIENT
                            WHERE name = :val
                            """
            result = Ingredient()
        else:
            return None
        resultProxy = db.session.execute(text(sql), {'val': name})
        db.session.commit()
        for r in resultProxy:
            r_dict = dict(r.items())
        for att in r_dict:
            result.__setattr__(att, r_dict[att])
        return result
