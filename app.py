import os
from flask import (
    Flask, request, render_template,
    redirect, flash, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/board/")
def board():
    writings = mongo.db.essays.find()
    return render_template('board.html', writings=writings)


@app.route("/register/")
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("So much for originality! Someone else has already regsistered this username.")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get('username').lower(),
            "first_name": request.form.get('first_name').lower(),
            "last_name": request.form.get('last_name').lower(),
            "password": generate_password_hash(request.form.get('password'))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You did it! Successful registration as a new user. Hurrah!")
        return redirect(url_for('profile', username=session["user"]))
    return render_template('register.html')


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hey {}!".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                #invalid password match
                flash("Hmm...that's not your Username and/or Password.")
                return redirect(url_for('login'))

        else:
            #username doesn't exist 
            flash("Hmm...that's not your Username and/or Password.")
            return redirect(url_for('login'))
        
        return render_template('login.html')



@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    #grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template('profile.html', username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
