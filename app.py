# Main Application
import hashlib
import uuid

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api
from flask_restful.representations import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, func, bindparam

from config import DevConfig  # Import sequence matters!

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
api = Api(app)
auth = HTTPBasicAuth()
from Scripts.Models import *


def initDatabase():  # Delete All Tables, Create tables according to Model Imports
    #db.drop_all()
    db.create_all()
    db.session.commit()


initDatabase()


class SqlUtils:

    def Insert(self, source: object):

        localvar = db.engine.raw_connection().cursor().var(
            int)  # Required for getting id after Insertion(Works only for cx_Oracle)

        if isinstance(source, User):
            source: User
            if source.id is None:
                raise Exception("User Id can not be null")
            sql = """
                    INSERT INTO "USER" (id,email,username,password,fname,mname,lname,registerdate)
                    VALUES(:idval,:emailval,:usernameval, :passwordval,:fnameval,:mnameval,:lnameval,:registerdateval)
                    """

            db.session.execute(text(sql), {'emailval': source.email, 'usernameval': source.username,
                                           'passwordval': source.password,
                                           'fnameval': source.fname, 'mnameval': source.mname,
                                           'lnameval': source.lname,
                                           'idval': source.id,
                                           'registerdateval': source.registerdate})
            db.session.commit()
            return source
        if isinstance(source, Recipe):
            source: Recipe
            if source.id is None:
                raise Exception("Recipe Id can not be null")
            sql = """
                    INSERT INTO "RECIPE" (id,direction,fat,"date",calories,description,protein,rating,title,,ingredientDescription,sodium,categoryName)
                    VALUES(:id,:direction,:fat, :"date",:calories,:description,:protein,:rating, :title,:ingredientDescription,:sodium,:categoryName )
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'direction': source.direction, 'fat': source.fat,
                                           'date': source.date,
                                           'id': source.id,
                                           'calories': source.calories, 'description': source.description,
                                           'protein': source.protein,
                                           'rating': source.rating, 'title': source.title,
                                           'ingredientDescription': source.ingredientDescription,
                                           'sodium': source.sodium, 'categoryName': source.categoryName})
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source

        if isinstance(source, Menu):
            source: Menu
            if source.id is None:
                raise Exception("Menu Id can not be null")
            sql = """
                    INSERT INTO "MENU" (id,userId,recipeList,name)
                    VALUES(:id,:userId,:recipeList, :name)
                    RETURNING ID INTO :localvar
                    """

            db.session.execute(text(sql), {'userId': source.userId, 'recipeList': source.recipeList,
                                           'name': source.name,
                                           'id': source.id
                                           })
            db.session.commit()
            source.id = localvar.getvalue()[0]
            return source
        if isinstance(source, Category):
            source: Category
            if source.name is None:
                raise Exception("Category Name can not be null")
            sql = """
                    INSERT INTO "CATEGORY" (name)
                    VALUES(:name)
                    """

            db.session.execute(text(sql), {'name': source.name
                                           })
            db.session.commit()
            return source

        if isinstance(source, Ingredient):
            source: Ingredient
            if source.name is None:
                raise Exception("Ingredient Name can not be null")
            sql = """
                    INSERT INTO "INGREDIENT" (name)
                    VALUES(:name)
                    """

            db.session.execute(text(sql), {'name': source.name
                                           })
            db.session.commit()
            return source
        if isinstance(source, Review):
            source: Review
            if source.id is None:
                raise Exception("Review Id can not be null")
            sql = """
                    INSERT INTO "REVIEW" (ID,USERNAME,RATING,comments,recipeid)
                    VALUES(:idval,:username,:rating,:commentval,:recipeid)
                    """

            db.session.execute(text(sql), {'idval': source.id,
                                           'username': source.username,
                                           'rating': source.rating,
                                           'commentval': source.comments,
                                           'recipeid': source.recipeid
                                           })
            db.session.commit()
            return source
        if isinstance(source, MenuRate):
            source: MenuRate
            if source.id is None:
                raise Exception("MenuRate Id can not be null")
            sql = """
                    INSERT INTO "MENURATE" (menuId,uId,rate)
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
        if (tablename.lower() == "USER".lower()):
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
        elif (tablename.lower() == "REVIEW".lower()):
            sql = """
                            SELECT *
                            FROM "REVIEW"
                            WHERE  id = :val
                            """
            result = Review()

        elif (tablename.lower() == "RECIPE".lower()):
            sql = """
                            SELECT *
                            FROM "RECIPE"
                            WHERE  id = :val
                            """
            result = Recipe()
        elif (tablename.lower() == "MENURATE".lower()):
            sql = """
                            SELECT *
                            FROM "MENURATE"
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
    def GetAllRecipeReviewById(self,recipeId):
        sql = """
                        SELECT *
                        FROM "REVIEW"
                        WHERE  recipeid = :val
                        """
        resultProxy = db.session.execute(text(sql), {'val': recipeId})
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        return resultset


    def GetModelWithName(self, tablename: str, name: str):
        if (tablename.lower() == "CATEGORY".lower()):
            sql = """
                            SELECT *
                            FROM "CATEGORY"
                            WHERE  name = :val
                            """
            result = Category()
        elif (tablename.lower() == "INGREDIENT".lower()):
            sql = """
                            SELECT *
                            FROM "INGREDIENT"
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

    def GetUser(self, username):
        sql = """
                            SELECT *
                            FROM "USER"
                            WHERE  USERNAME = :val
                            """
        result = User()
        resultProxy = db.session.execute(text(sql), {'val': username})
        db.session.commit()
        for r in resultProxy:
            r_dict = dict(r.items())
        for att in r_dict:
            result.__setattr__(att, r_dict[att])
        return result

    def GetRecipeId(self, list):

        if list[0] is not None:
            sql = """
                                    SELECT "Recipe_id"
                                    FROM "Ingredient_List"
                                    WHERE "Ingredient_name" LIKE """ + "\'" + list[0] + "\'"
        for ing in list[1:]:
            sql = sql + """         
                                    UNION
                                    SELECT "Recipe_id"
                                    FROM "Ingredient_List"
                                    WHERE "Ingredient_name" LIKE """ + "\'" + ing + "\'"

        print(sql)
        resultProxy = db.session.execute(text(sql))
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        # print(resultset[0].get("Recipe_id"))
        return resultset

    def GetRecipeIdForCategory(self, list):
        if list[0] is not None:
            sql = """
                                    SELECT "Recipe_id"
                                    FROM "Category_List"
                                    WHERE "Category_name" LIKE """ + "\'" + list[0] + "\'"
        for ing in list[1:]:
            sql = sql + """         
                                    UNION
                                    SELECT "Recipe_id"
                                    FROM "Category_List"
                                    WHERE "Category_name" LIKE """ + "\'" + ing + "\'"

        print(sql)
        resultProxy = db.session.execute(text(sql))
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        return resultset
    def GetRecipeAverageRate(self,recipeId):
        sql = """
                                    SELECT AVG(rating)
                                    FROM "REVIEW"
                                    WHERE recipeid = :val
                """
        resultProxy = db.session.execute(text(sql), {'val': recipeId})
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        return resultset
    def UpdateRecipeAverateRate(self,recipeId,rate):
        sql = """
                                    UPDATE "RECIPE"
                                    SET RATING = :ratingval
                                    WHERE ID = :val
                """
        db.session.execute(text(sql), {'val': recipeId , 'ratingval': rate})
        db.session.commit()
        return True
    def GetRecipeIngList(self,recipeId):
        sql = """
                            SELECT "Ingredient_name"
                            FROM "Ingredient_List"
                            WHERE  "Recipe_id" = :val
                            """
        resultProxy = db.session.execute(text(sql), {'val': recipeId})
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        return resultset
    def GetRecipeCatList(self,recipeId):
        sql = """
                            SELECT "Category_name"
                            FROM "Category_List"
                            WHERE  "Recipe_id" = :val
                            """
        resultProxy = db.session.execute(text(sql), {'val': recipeId})
        db.session.commit()
        resultset = [dict(row) for row in resultProxy]
        return resultset

sqlUtil = SqlUtils()


@app.route('/get_search_result_recipes', methods=['GET', 'POST'])
def get_search_result():
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content["password"]
        keywords = content["keywords"]
        categories = content["categories"]
        if str(username).strip():  # Check for Login
            try:
                user = sqlUtil.GetUser(username)
                if user.password == password:
                    pass
                else:
                    return "False"
            except:
                return "False"
        else:
            return "False"

        arr = []
        if (categories):
            catListForSql = []
            for val in keywords:
                catListForSql.append("%" + val + "%")
            recipeList = sqlUtil.GetRecipeIdForCategory(catListForSql)
            for recipeId2 in recipeList:
                recipe = sqlUtil.GetModelWithID("Recipe", recipeId2.get("Recipe_id"))
                arr.append(recipe.to_json())
        else:
            ingListForSql = []
            for val in keywords:
                ingListForSql.append("%" + val + "%")
            recipeList = sqlUtil.GetRecipeId(ingListForSql)
            for recipeId in recipeList:
                recipe = sqlUtil.GetModelWithID("Recipe", recipeId.get("Recipe_id"))

                arr.append(recipe.to_json(sqlUtil.GetRecipeIngList(recipe.id), sqlUtil.GetRecipeCatList(recipe.id)))

        print(arr)
    return json.dumps(arr)  # verilen keywordlere bağlı recipeler dönülecek
    # sorgu dışında 2 tane daha dönülecek bunlar en populer


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content["password"]
        email = content["email"]
        fname = content["fname"]
        mname = content["mname"]
        lname = content["lname"]
        id = hashlib.md5(str(email).encode('utf-8'))
        registerdate = datetime.utcnow()
        idHashed = int(id.hexdigest(), base=16) % 10000
        try:
            user: User = User(email=email, username=username, password=password,
                              fname=fname, mname=mname, lname=lname,
                              registerdate=registerdate, id=idHashed)
            sqlUtil.Insert(user)
            return "True"
        except:
            return "False"
    return "False"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content["password"]

    if str(username).strip():
        try:
            user = sqlUtil.GetUser(username)
            if user.password == password:
                return "True"
            else:
                return "False"
        except:
            return "False"
    else:
        return "False"


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        content = request.get_json()
        direction = content["direction"]
        fat = content["fat"]
        date = datetime.utcnow()
        calories = content["calories"]
        description = content["description"]
        protein = content["protein"]
        rating = content["rating"]
        title = content["title"]
        ingredientList = content["ingredientList"]
        ingredientDescription = content["ingredientDescription"]
        sodium = content["sodium"]
        categoryName = content["categoryName"]
        id = hashlib.md5(str(title).encode('utf-8'))
        idHashed = int(id.hexdigest(), base=16)

        recipe: Recipe = Recipe()
        recipe.direction = direction
        recipe.fat = fat
        recipe.date = date
        recipe.calories = calories
        recipe.description = description
        recipe.protein = protein
        recipe.rating = rating
        recipe.title = title
        recipe.id = idHashed % 100000
        for ing in ingredientList:
            try:
                # ingredient=sqlUtil.GetModelWithName("ingredient",ing["name"])
                ingredient = Ingredient.query.filter_by(name=str(ing["name"])).one()
                recipe.ingredientList.append(ingredient)
            except Exception as e:
                ingredient: Ingredient = Ingredient(name=str(ing["name"]))
                recipe.ingredientList.append(ingredient)
        for cat in categoryName:
            try:
                # category = sqlUtil.GetModelWithName("category",cat["name"])
                category = Category.query.filter_by(name=cat["name"]).one()
                recipe.categoryList.append(category)
            except Exception as e:
                category: Category = Category(name=str(cat["name"]))
                recipe.categoryList.append(category)
        print(recipe.categoryList)
        print(recipe.ingredientList)
        recipe.ingredientDescription = ingredientDescription
        recipe.sodium = sodium

        try:
            db.session.add(recipe)
            db.session.commit()
        except Exception as e:
            print("FAULT: " + str(e))
            return "False"
        return "True"


@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        content = request.get_json()
        name = content["name"]
        try:
            result = sqlUtil.GetModelWithName("ingredient", name)
            return "False"
        except:
            newIngredient = Ingredient()
            newIngredient.name = name
            sqlUtil.Insert(newIngredient)
            return "True"


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        content = request.get_json()
        name = content["name"]
        try:
            result = sqlUtil.GetModelWithName("category", name)
            return "False"
        except:
            newCategory = Category()
            newCategory.name = name
            sqlUtil.Insert(newCategory)
            return "True"


@app.route('/get_recipe_reviews_with_id', methods=['GET', 'POST'])
def get_recipe_reviews_with_id():
    if request.method == 'POST':
        content = request.get_json()
        recipe_id = content["recipe_id"]
        try:
            result = sqlUtil.GetAllRecipeReviewById(recipe_id)
        except:
            return "False"
    return json.dumps(result)  # all recipe info as json


@app.route('/add_recipe_reviews_with_id', methods=['GET', 'POST'])
def addrecipe_reviews_with_id():
    if request.method == 'POST':
        content = request.get_json()
        recipe_id = content["recipe_id"]
        username = content["username"]
        comment = content["comments"]
        rating = content["rating"]
        id = uuid.uuid4().int & (1 << 64) - 1
        review : Review = Review(id=id,username=username,comments=comment,rating=rating,recipeid=recipe_id)
        try:
            sqlUtil.Insert(review)
            avgrate = sqlUtil.GetRecipeAverageRate(review.recipeid)
            sqlUtil.UpdateRecipeAverateRate(review.recipeid,int(avgrate[0].get("AVG(RATING)")))
            return "True"
        except Exception as e:
            print(str(e))
            return "False "

    return "False"


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        pass


if __name__ == '__main__':
    app.run()
