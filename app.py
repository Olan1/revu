import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


# Home / index
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', reviews=mongo.db.reviews.find())


# User agreement
@app.route('/user_agreement')
def user_agreement():
    return render_template('terms.html')


# Sign in
@app.route('/sign_in')
def sign_in():
    return render_template('signin.html')

 
# Sign up
@app.route('/sign_up')
def sign_up():
    return render_template('signup.html')
    
    
# View REVU
@app.route('/view_revu/<review_id>')
def view_revu(review_id):
    the_revu =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('revu.html', review=the_revu)    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)