from datetime import datetime
from neuro import db, login_manager#, admin
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60),unique=True,nullable=True)    
    password = db.Column(db.String(60), nullable=False)
    answers = db.relationship('Answer', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    day1 = db.Column(db.Text, nullable=True)
    score = db.Column(db.Text,nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Post( '{self.date_posted}')"

