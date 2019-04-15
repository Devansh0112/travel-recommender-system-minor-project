from flask import render_template, url_for, flash, redirect, request
from minorproj import app, db, bcrypt
from minorproj.forms import RegistrationForm, LoginForm
from minorproj.models import User
from flask_login import login_user, current_user, logout_user
import pandas as pd

@app.route('/')
@app.route('/home')
def home():
    df = pd.read_csv('F:\\web development\\Minor Project\\cities.csv')
    df = df['name_of_city']
    return render_template('home.html', dataset=df)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        placelike = ['Delhi', 'Mumbai']
        wishlist = ['punjab','haryana']
        user = User(username = form.username.data, email = form.email.data, password = hashed_password, placeliked = placelike, wishlist = wishlist)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f'unsuccessfull! User not Found.','danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('home'))
