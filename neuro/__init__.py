from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_admin import Admin,AdminIndexView
#from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SECRET_KEY']='adsadsd3123kjhg32131iplksa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#admin = Admin(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from neuro import routes
#from neuro.modules import User,Answer
#admin.add_view(ModelView(User,db.session))
#admin.add_view(ModelView(Answer,db.session))

