
from flask import Flask, render_template, redirect, url_for, request
import time
import json
import datetime
from Scripts.Models import add_User, add_Ingredient
app = Flask(__name__)




@app.route('/get_search_result_recipes', methods=['GET', 'POST'])
def get_search_result():
    error = None
    if request.method == 'POST':


        content = request.get_json()
        username = content["username"]
        password = content["password"]
        keywords = content["keywords"]
        categories = content["categories"]
        order = content[""] #viewCount ,


        if(categories):
            a = 1
            #categorye göre sorgu

        otp = request.form['username']

    return "" # verilen keywordlere bağlı recipeler dönülecek
    # sorgu dışında 2 tane daha dönülecek bunlar en populer, 



@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    error = None
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



@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    error = None
    if request.method == 'POST':
        content = request.get_json()
        name = content["ingredient_name"]
        add_Ingredient(name)
    return "1" # tek usera ait menuler 

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    error = None
    if request.method == 'POST':
        content = request.get_json()
        name = content["category_name"]
        add_category(name)
    return "1" # tek usera ait menuler 




@app.route('/get_user_menus', methods=['GET', 'POST'])
def get_user_menus():
    error = None
    if request.method == 'POST':

        content = request.get_json()
        username = content["username"]
        


    return "" # tek usera ait menuler 


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':


        content = request.get_json()
        username = ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545,debug=True)

