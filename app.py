import os
from flask import (
    Flask, request, render_template,
    redirect, flash, session, url_for, app)
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = 'mongodb'
mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    writings = list(mongo.db.stories.find({'$text': {'$search': query}}))
    return render_template('get_stories.html', writings=writings)


@app.errorhandler(404)
def not_found(er):
    flash("A Fool's Errand!")
    return render_template('404.html')


@app.route('/get_stories/')
def get_stories():
    writings = list(mongo.db.stories.find().sort('title', 1))
    return render_template('get_stories.html', writings=writings)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash("Someone else has already registered this username.")
            return redirect(url_for('register'))
        if request.form.get('password') != request.form.get(
                'confirm_password'):
            flash("Password and Confirm Password MUST match")
            return redirect(url_for('register'))
        register = {
            'username': request.form.get('username').lower(),
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'password': generate_password_hash(request.form.get('password')),
            'date_joined': datetime.now()
        }

        mongo.db.users.insert_one(register)
        # Put new user into a session cookie
        session['user'] = request.form.get('username').lower()
        flash("You did it! Successful registration as a new user. Hurrah!")
        return redirect(url_for('profile', username=session['user']))
    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            if check_password_hash(
                    existing_user['password'],
                    request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash("Hey {}!".format(
                    request.form.get('username').capitalize()))
                return redirect(url_for('profile', username=session['user']))
            else:
                flash("Hmm...that's not your Username and/or Password.")
                return redirect(url_for('login'))
        else:
            flash("Hmm...that's not your Username and/or Password.")
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route("/logout")
def logout():
    flash("You have been logged out.")
    session.pop('user')
    return redirect(url_for("login"))


@app.route("/profile/<username>/", methods=['GET', 'POST'])
def profile(username):

    username = mongo.db.users.find_one(
        {"username": session['user']})['username']
    userstories = list(mongo.db.stories.find({'author': session['user']}))
    if session["user"]:
        return render_template('profile.html',
                               username=username,
                               userstories=userstories)
    return redirect(url_for("login"))


@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if request.method == 'POST':
        submit = {
            "title": request.form.get('title'),
            "author": session['user'],
            "date": request.form.get('date'),
            "category_name": request.form.get('category_name'),
            "composition": request.form.get('composition')
        }
        mongo.db.stories.insert_one(submit)
        flash("Your story has been added.")
        return redirect(url_for('get_stories'))

    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('new_story.html', categories=categories)


@app.route('/edit_story/<story_id>/', methods=['GET', 'POST'])
def edit_story(story_id):
    if request.method == 'POST':
        submit = {
                'title': request.form.get('title'),
                'author': session['user'],
                'date': request.form.get('date'),
                'category_name': request.form.get('category_name'),
                'composition': request.form.get('composition')
        }
        mongo.db.stories.update({'_id': ObjectId(story_id)}, submit)
        flash("Alright then, you've successsfully edited this story.")
        return redirect(url_for('get_stories'))
    story = mongo.db.stories.find_one(
            {'_id': ObjectId(story_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('edit_story.html',
                           story=story,
                           categories=categories)


@app.route('/delete_story/<story_id>')
def delete_story(story_id):
    mongo.db.essays.remove({'_id': ObjectId(story_id)})
    flash('You have deleted a story')
    return redirect(url_for('get_stories'))


@app.route('/user/')
def user():
    users = mongo.db.users.find().sort('username', 1)
    writings = list(mongo.db.stories.find().sort('title', 1))
    return render_template('user.html', users=users, writings=writings)


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    flash('You have deleted a user')
    return redirect(url_for('user'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
