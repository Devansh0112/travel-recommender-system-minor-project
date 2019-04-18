from flask import render_template, url_for, flash, redirect, request
from minorproj import app, db, bcrypt
from minorproj.forms import RegistrationForm, LoginForm, dropdown
from minorproj.models import User
from flask_login import login_user, current_user, logout_user
import pandas as pd

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    form = dropdown()
    if request.method == 'POST':
        a = form.select.data
        b = list(current_user.placeliked)
        if a not in b:
            b.append(a)
            current_user.placeliked = b
            db.session.commit()

        flash('Successfully Added!', 'success')

    return render_template('home.html', forms=form)

@app.route('/delete_places')
def delete_places():
    current_user.placeliked = []
    db.session.commit()
    flash('Deleted Successfully','danger')

    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
