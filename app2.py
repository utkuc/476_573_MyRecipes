
from flask import Flask, render_template, redirect, url_for, request
import time
import json
import datetime
#from Scripts.Models import *
#from Scripts.SqlUtils2 import SqlUtils

app = Flask(__name__)




@app.route('/get_search_result_recipes', methods=['GET', 'POST'])
def get_search_result():
    
    if request.method == 'POST':
        content = request.get_json()
        keywords = content["keywords"]
        categories = content["categories"]
        # önce order sabit olsun sonra 3 farklı order yapmaya çalışırız.  order = content["order"] #viewCount , rating , name
        recipe = {"recipe_id":"132321","title":"qwewqr", "calories":"13","ingredients":"d , a, v ,c,d"}
        recipes = []
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        recipes.append(recipe)
        

        recipe_list = {}
        recipe_list["recipes"] = recipes
        return json.dumps(recipe_list)

        
        return "{""}"
        if(categories):
            a = 1
            #categorye göre sorgu
    arr = []
    for i in range(3):
        result = {}
        result["recipe_id"]
        result["title"] = ""
        result["calories"] = ""
        result["ingredients"] = ["a","b","c"]
        arr.append(result)
    recipe_list = {}
    recipe_list["recipe"]
    return json.dumps(arr)  # verilen keywordlere bağlı recipeler dönülecek
    # sorgu dışında 2 tane daha dönülecek bunlar en populer 



@app.route('/get_recipe_with_id', methods=['GET', 'POST'])
def get_recipe_with_id():
    
    if request.method == 'POST':
        content = request.get_json()
        recipe_id = content["recipe_id"]
        recipe_info = {}
        
        recipe_info["recipe_info"] ="adsadsadsadsadsadsasadsa"
        recipe_info["recipe_id"] = recipe_id
    return json.dumps(recipe_info) # all recipe info as json 


@app.route('/get_recipe_reviews_with_id', methods=['GET', 'POST'])
def get_recipe_reviews_with_id():
    
    if request.method == 'POST':
        content = request.get_json()
        recipe_id = content["recipe_id"]
        recipe_info = {}
        review = {"username":"mustafa","rating":"4.5","comment":"ewewqewqaadsasadas dsdwqwqdwdqdwq"}
        reviews = []
        
        reviews.append(review)
        reviews.append(review)
        reviews.append(review)
        reviews.append(review)
        reviews.append(review)
        reviews.append(review)
        
        recipe_info["reviews"] =reviews
        recipe_info["recipe_id"] = recipe_id
    return json.dumps(recipe_info) # all recipe info as json 


@app.route('/add_recipe_reviews_with_id', methods=['GET', 'POST'])
def addrecipe_reviews_with_id():
    
    if request.method == 'POST':
        content = request.get_json()
        recipe_id = content["recipe_id"]
        username = content["username"]
        comment = content["comment"]
        rating = content["rating"]
        print(content)
    return "True"
    

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content["password"]
        email = content["email"]
        fname = content["name"]
        mname = "mname"
        lname = "lname"
        registerdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(email,username,password,fname,mname,lname,registerdate)
        #add_User(email,username,password,fname,mname,lname,registerdate)
        #add_User("email","username","password","fname","mname","lname","registerdate")
    return "True" 
    return "False"



@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content["password"]

    #check username password 
    result = {}
    result["result"] = "True"
    return json.dumps(result)
    return "True" # doğru parola ise 
    return "False" # yanlış ise 

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    
    if request.method == 'POST':
        content = request.get_json()
        direction = content["direction"]
        fat = content["fat"]
        date = datetime.datetime.now()#content["date"]
        calories = content["calories"]
        description = content["description"]
        protein = content["protein"]
        rating = content["rating"]
        title =content["title"]
        ingredientList = content["ingredientList"]## TODO connect with ingredients
        ingredientDescription = content["ingredientDescription"]
        sodium = content["sodium"]
        categoryName = content["categoryName"]
        add_Recipe(direction,fat,date,calories,description,protein,rating,title,ingredientList,ingredientDescription,sodium,categoryName)
    return "1" 




#TODO ayrı method olmamalı add recipe yapıldığında ingredient yaratılmalı
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    
    if request.method == 'POST':
        content = request.get_json()
        name = content["ingredient_name"]
        add_Ingredient(name)
    return "1" # tek usera ait menuler 

#TODO ayrı method olmamalı add recipe yapıldığında category yaratılmalı
@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    
    if request.method == 'POST':
        content = request.get_json()
        name = content["category_name"]
        add_category(name)
    return "1" # tek usera ait menuler 




@app.route('/get_user_menus', methods=['GET', 'POST'])
def get_user_menus():
    
    if request.method == 'POST':

        content = request.get_json()
        username = content["username"]
        


    return "" # tek usera ait menuler 

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':


        content = request.get_json()
        username = content["username"]
        password = content["password"]
        check_result = check_password(username,password)
        result = {}
        result["result"] = check_result
        return json.dumps(result)"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545,debug=True)

