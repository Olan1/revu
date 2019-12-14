import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('secret_key')

mongo = PyMongo(app)


# Home / index
@app.route('/')
@app.route('/home')
def home():
    if 'user_email' in session:
        return render_template('index.html', reviews=mongo.db.reviews.find())
    return render_template('signin.html')
    
    
# Sign in
@app.route('/sign_in', methods=['POST'])
def sign_in():
    users = mongo.db.users
    login_user = users.find_one({ 'email': request.form['email']})
    
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['user_email'] = request.form['email']
            return redirect(url_for('home'))
    
    return 'Invalid username/password'

 
# Sign up
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        users = mongo.db.users
        existing_email = users.find_one({'email': request.form['email']})
        
        if existing_email is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'first': request.form['first_name'],
                            'last': request.form['last_name'],
                            'email': request.form['email'],
                            'password': hashpass})
            session['user_email'] = request.form['email']
            return redirect(url_for('home'))
        return "That email is already registered to an account"

    return render_template('signup.html')
    
    
# Sign Out
@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect('home')


# User agreement
@app.route('/user_agreement')
def user_agreement():
    return render_template('terms.html')
    
    
# View REVU
@app.route('/view_revu/<review_id>')
def view_revu(review_id):
    the_revu =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('revu.html', review=the_revu)    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)