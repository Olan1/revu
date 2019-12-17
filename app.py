import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
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

    flash('Invalid username/password')
    return render_template('signin.html')
 
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
            
        flash('An account already exists with that email address')

    return render_template('signup.html')
    
# Sign Out
@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect('home')
    
# Delete Account
@app.route('/delete_ac')
def delete_ac():
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
    the_revu =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if the_revu == None:
        flash("Unable to find that particular REVU")
        return redirect('home')
        
    return render_template('revu.html', review=the_revu)
    
#Form Values Validation
def form_validate():
    errors = 0
    # Rating Validation
    try:
        float(request.form['rating'])
    except:
        flash("Rating must be a number")
        errors += 1
    else:
        if float(request.form['rating']) > 5 or float(request.form['rating']) < 0:
            flash("Rating must be between 0 and 5")
            errors += 1
            
    # Run-Time Validation
    try:
        float(request.form['run-time'])
    except:
        flash("Run-Time must be a number")
        errors += 1
        
    # Budget Validation
    budget = request.form['budget']
    if "," in budget:
        budget = budget.replace(",", "")
    
    try:
        float(budget)
    except:
        flash("Budget must be a number")
        errors += 1
        
    # Run-Time Validation
    earned = request.form['earned']
    if "," in earned:
        earned = earned.replace(",", "")
    try:
        float(earned)
    except:
        flash("Earned must be a number")
        errors += 1
    if errors > 0:
        return False
    return True

# New REVU
@app.route('/new_revu', methods=['POST', 'GET'])
def new_revu():
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
    user = mongo.db.users.find_one({'email': session['user_email']})
    author = '{} {}'.format(user['first'], user['last'])
    the_reviews = mongo.db.reviews.find({'author': author})
    return render_template('myrevus.html', reviews=the_reviews)
    
# Edit REVU
@app.route('/edit_revu/<revu_id>')
def edit_revu(revu_id):
    return render_template('editrevu.html',
                            review=mongo.db.reviews.find_one(
                            {'_id': ObjectId(revu_id)}))

# Update REVU
@app.route('/update_revu/<revu_id>', methods=['POST'])
def update_revu(revu_id):
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
    mongo.db.reviews.remove({'_id': ObjectId(revu_id)})
    return redirect(url_for('my_revus'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
