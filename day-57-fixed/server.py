from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

GENDERIZE_ENDPOINT = 'https://api.genderize.io?'
AGEIFY_ENDPOINT = 'https://api.agify.io'


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    today = date.today()
    current_year = today.year
    # or| current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    genderize_params = {
        "name": name
    }
    response = requests.get(url=GENDERIZE_ENDPOINT, params=genderize_params)
    genderize_response = response.json()
    gender = genderize_response['gender']
    response = requests.get(url=AGEIFY_ENDPOINT, params=genderize_params)
    age_response = response.json()
    age = age_response['age']
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



