import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from email_validator import validate_email
from django.core.validators import URLValidator
import re

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('secret_key')

mongo = PyMongo(app)

# Home / index
@app.route('/')
@app.route('/home')
def home():
    """
    If user is logged in, render homepage
    
    Else render sign in page
    """
    if 'user_email' in session:
        return render_template('index.html', reviews=mongo.db.reviews.find())
    return render_template('signin.html')
    
# Sign in
@app.route('/sign_in', methods=['POST'])
def sign_in():
    """
    If user email and password match database, initialize user session and
    render homepage
    
    Else flash error message and return to sign in page
    """
    login_user = mongo.db.users.find_one({ 'email': request.form['email']})
    
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                        login_user['password']) == login_user['password']:
            session['user_email'] = request.form['email']
            return redirect(url_for('home'))

    flash('Invalid username/password')
    return render_template('signin.html')
 
# Sign up
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    """
    If request method is POST and form contents are valid, check if email is in
    database
    
    If email does not already exist in the database, encrypt the password,
    insert form data into database, initialise user session and render homepage
    
    If email already in database flash error message and return to sign up page
    
    If request method is not POST, return sign up page
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if form fields are empty
        if (not first_name.strip() or not last_name.strip() or
                not email.strip() or not password.strip()):
            flash("Form fields cannot be empty")
            return redirect(url_for('sign_up'))
            
        # Check if password secure
        # Source: https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions
        if (len(password) < 8 or re.search(r"\d", password) is None or
                re.search(r"[A-Z]", password) is None or
                re.search(r"[a-z]", password) is None or
                re.search(r"[ @!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None):
            flash("Password must contain minimum 8 characters,\
                    1 uppercase and 1 lowercase letter, 1 digit,\
                    and 1 special character")
            return redirect(url_for('sign_up'))
        
        # Check for valid email address
        # Source: https://pypi.org/project/email-validator/
        try:
            validate_email(email)
        except:
            flash("Please enter a valid email address")
            return redirect(url_for('sign_up'))
        
        users = mongo.db.users
        existing_email = users.find_one({'email': email})
        
        if existing_email is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users.insert({'first': first_name,
                            'last': last_name,
                            'email': email,
                            'password': hashpass})
            session['user_email'] = email
            return redirect(url_for('home'))
            
        flash('An account already exists with that email address')
    return render_template('signup.html')
    
# Sign Out
@app.route('/sign_out')
def sign_out():
    """
    Clear current session and redirect to the home method (which will render
    the Sign in page)
    """
    session.clear()
    return redirect('home')
    
# Delete Account
@app.route('/delete_ac')
def delete_ac():
    """
    Remove current session user from the database
    
    Clear current session
    
    Render Sign in page
    """
    mongo.db.users.remove({'email': session['user_email']})
    session.clear()
    return redirect('home')

# User agreement
@app.route('/user_agreement')
def user_agreement():
    return render_template('terms.html')
    
# View REVU
@app.route('/view_revu/<review_id>')
def view_revu(review_id):
    """
    Find review in database based on review_id parameter
    
    If review doesn't exist, flash error message and redirect to home
    
    If review exists, render REVU page
    """
    the_revu =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if the_revu == None:
        flash("Unable to find that particular REVU")
        return redirect('home')
        
    return render_template('revu.html', review=the_revu)
    
#Form Values Validation
def form_validate():
    """
    If a form field throws an error, flash error message and increment error
    counter
    """
    errors = 0
    title = request.form['title']
    rating = request.form['rating']
    img_url = request.form['img-url']
    plot = request.form['plot']
    review = request.form['review']
    released = request.form['released']
    director = request.form['director']
    writers = request.form['writers']
    producer = request.form['producer']
    starring = request.form['starring']
    run_time = request.form['run-time']
    genre = request.form['genre']
    budget = request.form['budget']
    earned = request.form['earned']
    
    # Empty Form Fields Validation
    if (not title.strip() or not rating.strip() or
            not img_url.strip() or not plot.strip() or
            not review.strip() or not released.strip() or
            not director.strip() or not writers.strip() or
            not producer.strip() or not starring.strip() or
            not run_time.strip() or not genre.strip() or
            not budget.strip() or not earned):
        flash("Form fields cannot be empty")
        errors += 1
        
    # URL Validation
    # Source: https://stackoverflow.com/questions/3170231/how-can-i-check-if-a-url-exists-with-django-s-validators
    val = URLValidator()
    try:
        val(img_url)
    except:
        flash("Please enter a valid URL")
        errors += 1
    
    # Rating Validation
    # Must be a number between 0 - 5
    try:
        float(rating)
    except:
        flash("Rating must be a number")
        errors += 1
    else:
        if float(rating) > 5 or float(rating) < 0:
            flash("Rating must be between 0 and 5")
            errors += 1
            
    # Run-Time Validation
    # Must be a number
    try:
        float(run_time)
    except:
        flash("Run-Time must be a number")
        errors += 1
        
    # Budget Validation
    # Remove all comas and check if number
    if "," in budget:
        budget = budget.replace(",", "")
    try:
        float(budget)
    except:
        flash("Budget must be a number")
        errors += 1
        
    # Run-Time Validation
    # Remove all comas and check if number
    if "," in earned:
        earned = earned.replace(",", "")
    try:
        float(earned)
    except:
        flash("Earned must be a number")
        errors += 1
    
    # If an error exists, return False
    # Else return True
    if errors > 0:
        return False
    return True

# New REVU
@app.route('/new_revu', methods=['POST', 'GET'])
def new_revu():
    """
    If request method is POST, query session users full name from database
    
    If form validation method returns no errors, insert form data into reviews
    collection in database and render My REVUs page
    
    If form validation returns errors, flash error messages and render New REVU
    page
    
    If request method is not POST, render New REVU page
    """
    if request.method == 'POST':
        user = mongo.db.users.find_one({'email': session['user_email']})
        author = '{} {}'.format(user['first'], user['last'])
        reviews = mongo.db.reviews
        
        if form_validate():
            reviews.insert({'title': request.form['title'],
                            'rating': request.form['rating'],
                            'img_url': request.form['img-url'],
                            'plot': request.form['plot'],
                            'review': request.form['review'],
                            'released': request.form['released'],
                            'director': request.form['director'],
                            'writers': request.form['writers'],
                            'producer': request.form['producer'],
                            'starring': request.form['starring'],
                            'run_time': request.form['run-time'],
                            'genre': request.form['genre'],
                            'budget': request.form['budget'],
                            'earnings': request.form['earned'],
                            'author': author})
            return redirect(url_for('my_revus'))
            
    return render_template('newrevu.html')

# My REVUs
@app.route('/my_revus')
def my_revus():
    """
    Get current session users full name from database from database
    
    Get all reviews in database where the author field matches the users full
    name
    
    Render My REVUs page and provide the users reviews as parameter
    """
    user = mongo.db.users.find_one({'email': session['user_email']})
    author = '{} {}'.format(user['first'], user['last'])
    user_reviews = mongo.db.reviews.find({'author': author})
    return render_template('myrevus.html', reviews=user_reviews)
    
# Edit REVU
@app.route('/edit_revu/<revu_id>')
def edit_revu(revu_id):
    """
    Render Edit REVU page and get specified review from database and feed as
    parameter
    """
    return render_template('editrevu.html',
                            review=mongo.db.reviews.find_one(
                            {'_id': ObjectId(revu_id)}))

# Update REVU
@app.route('/update_revu/<revu_id>', methods=['POST'])
def update_revu(revu_id):
    """
    If form validation method returns no errors, update review in database with
    form data
    
    If form validation returns errors, render Edit REVU page
    """
    user = mongo.db.users.find_one({'email': session['user_email']})
    author = '{} {}'.format(user['first'], user['last'])
    if form_validate():
        mongo.db.reviews.update(
                                {'_id': ObjectId(revu_id)},
                                {'title': request.form['title'],
                                'rating': request.form['rating'],
                                'img_url': request.form['img-url'],
                                'plot': request.form['plot'],
                                'review': request.form['review'],
                                'released': request.form['released'],
                                'director': request.form['director'],
                                'writers': request.form['writers'],
                                'producer': request.form['producer'],
                                'starring': request.form['starring'],
                                'run_time': request.form['run-time'],
                                'genre': request.form['genre'],
                                'budget': request.form['budget'],
                                'earnings': request.form['earned'],
                                'author': author})
        return redirect(url_for('my_revus'))
        
    return redirect(url_for('edit_revu', revu_id=revu_id))

# Delete REVU
@app.route('/delete_revu/<revu_id>')
def delete_revu(revu_id):
    """
    Delete specified review from database
    
    Render My REVUs page
    """
    mongo.db.reviews.remove({'_id': ObjectId(revu_id)})
    return redirect(url_for('my_revus'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
