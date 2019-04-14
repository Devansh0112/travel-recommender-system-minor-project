from flask import render_template, url_for, flash, redirect
from minorproj import app, db, bcrypt
from minorproj.forms import RegistrationForm, LoginForm
from minorproj.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        placelike = list()
        wishlist = list()
        user = User(username = form.username.data, email = form.email.data, password = hashed_password, placeliked = placelike, wishlist = wishlist)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Successfully logged In!','success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
