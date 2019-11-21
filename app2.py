
from flask import Flask, render_template, redirect, url_for, request
import time
import json
import datetime
from Scripts.Models import *
app = Flask(__name__)




@app.route('/get_search_result_recipes', methods=['GET', 'POST'])
def get_search_result():
    
    if request.method == 'POST':


        content = request.get_json()
        username = content["username"]
        password = content["password"]
        keywords = content["keywords"]
        categories = content["categories"]
        order = content["order"] #viewCount ,


        if(categories):
            a = 1
            #categorye göre sorgu

        a = get_users()
        arr = []
        for i in a:
            arr.append(i.password)
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
        registerdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(email,username,password,fname,mname,lname,registerdate)
        add_User(email,username,password,fname,mname,lname,registerdate)
        add_User("email","username","password","fname","mname","lname","registerdate")
    return "1" # tek usera ait menuler 


   

#TODO ayrı method olmamlı add recipe yapıldığında ingredient yaratılmalı
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    
    if request.method == 'POST':
        content = request.get_json()
        name = content["ingredient_name"]
        add_Ingredient(name)
    return "1" # tek usera ait menuler 



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


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':


        content = request.get_json()
        username = content["username"]
        password = content["password"]
        check_result = check_password(username,password)
        result = {}
        result["result"] = check_result
        return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545,debug=True)

