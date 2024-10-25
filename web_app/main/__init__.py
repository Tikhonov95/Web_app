from flask import Flask, render_template, request

from datetime import date

import json

import os 

from main import utils
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
ASDASD
articles = [] # Hell

def save_articles():
    file_obj = open('articles.json', 'w')       #   'w'- для записи
    
    json.dump(articles, file_obj, indent=4)
    
    file_obj.close() # Закрываем файл

def load_articles():
    if os.path.isfile('articles.json'):
        file_obj = open('articles.json', 'r')     #  'r' - для чтения 
        
        stored_articles = json.load(file_obj)
        articles.extend(stored_articles)
        
        file_obj.close()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    load_articles()
    
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return "<h1>Welcome to the about page</h1>"
    # Отлов нераспознанных маршутов
    @app.route("/<string:route>")
    def http_handler(route):
        return '404 - not found. Click <a href="/">here</a> to go home'
    
    @app.route("/result")
    def result():
        full_name = request.args.get('fullname')
        gender = request.args.get('gender')
        date_of_birth = request.args.get('date_of_birth')
       
       
        if not full_name or not date_of_birth:
            return '<h1>Некорректно заполнена форма</h1><a href="/">Вернуться домой</a>'
            
        # 1. Получить день, месяц и год
        day, month, year = utils.parse_date(date_of_birth)

        # 2. Проверить числа даты.
        if not utils.check_date(day, month, year):
            return f'<h1>Некорректно заполнена форма: Неправильная дата "{date_of_birth}" </h1><a href="/">Вернуться домой</a>'
            
        # 3. Вычислить возраст
        age = utils.get_age(day, month, year)

        return (f"<strong>{full_name}</strong> является "
                f"<em>{gender}</em> "
                f"<strong><em>{year}</em></strong> г. рождения. "
                f"Возраст: <u>{age}</u> лет.")
                
              
    @app.route("/articles", methods=["GET", "POST"])
    def articles_view():
        import random
        random_number = random.randint(1, 10)

        if request.method == "POST":
            article_title = request.values.get("article_title")
            article_body = request.values.get("article_body")
            if article_title and article_body:
                articles.append({
                    "title": article_title,
                    "body": article_body,
                })
                save_articles()

        second_article_text = "Это второй текст, созданный на сервере"
        return render_template(
            "articles.html", 
            argument_X = "This is text from named argument",
            random_number_arg = random_number, 
            articles = articles,
            second_article_text=second_article_text
        )
    
    return app

'''
    First approach
'''
# @app.route("/<string:route>")
# def http_handler(route):
#     if route == "home_1":
#         return "<h1>Welcome to the home page</h1>"
#     if route == "about":
#         return "<h1>About us</h1>"
#     if route == "login":
#         return "<h1>Login</h1>"
#     return '404 - not found. Click <a href="/home_1">here</a> to go home'

#    if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', date_of_birth);


  # if request.method == "POST":
        #     article_title = request.values.get("article_title")
        #     article_body = request.values.get("article_body")
        # else:
        #     article_title = "Временный заоголовок"
        #     article_body = "Временный параграф"