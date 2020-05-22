from flask import render_template, url_for, flash, redirect,request
from neuro import app,db
from neuro.forms import LoginForm, RegistrationForm, DeleteForm, AnswerForm
from neuro.modules import User,Answer
from flask_login import login_user, current_user, logout_user,login_required

############### LOGIN PAGE #############################
@app.route("/")
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form1=LoginForm()
    error=None
    if request.method =='POST':
        if form1.validate_on_submit():
            adminLogin = "fXZubFtF"
            adminPassword = "kAhJwYeX"
            user = User.query.filter_by(username=form1.username.data,password=form1.password.data).first()
            if user:
                login_user(user)
                return redirect(url_for('main'))
            elif form1.username.data == adminLogin and form1.password.data == adminPassword:
                return redirect(url_for('admin'))
            else:
                error='Niepoprawna nazwa użytkownika lub hasło'
    return render_template('login.html',form1=form1,error=error)


################## MAIN PAGE AND TEST DAYS ##################
@app.route('/main',methods=['GET'])
@login_required
def main():
    currentUser = current_user.username
    return render_template('main.html',currentUser=currentUser)

@app.route('/day1',methods=['POST','GET'])
@login_required
def day1():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day=form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana !"
    return render_template('day1.html',form=form,message=message)





















############## ADMIN PAGE ########################

@app.route('/admin',methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route('/add',methods=['GET','POST'])
def add():
    error="Pomyślnie dodano uzytkownika"
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return render_template('add.html',form=form,error=error)
    return render_template('add.html',form=form)

@app.route('/delete', methods=['GET','POST'])
def delete():
    form = DeleteForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            error="Nie ma takiego uzytkownia"
        else:
            db.session.delete(user)
            db.session.commit()
            error="Uzytkownik został usunięty"
    return render_template('delete.html',form=form,error=error)
        
    return render_template('delete.html',form=form)


@app.route('/users')
def users():
    users = User.query.all()
    
    return render_template('users.html',users=users)


######## LOGOUT ###########
@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')