from minorproj import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    placeliked = db.Column(db.PickleType, nullable=True, unique=False)
    wishlist = db.Column(db.PickleType, unique=False, nullable=True)


    def __repr__(self):
        return f"User('{self.email}','{self.username}','{self.placeliked}','{self.wishlist}','{self.password}')"