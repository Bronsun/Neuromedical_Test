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
        answer = Answer(day1="Dzień 1, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day1.html',form=form,message=message)

@app.route('/day2',methods=['POST','GET'])
@login_required
def day2():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 2, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day2.html',form=form,message=message)

@app.route('/day3',methods=['POST','GET'])
@login_required
def day3():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 3, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day3.html',form=form,message=message)

@app.route('/day4',methods=['POST','GET'])
@login_required
def day4():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 4, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day4.html',form=form,message=message)

@app.route('/day5',methods=['POST','GET'])
@login_required
def day5():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 5, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day5.html',form=form,message=message)

@app.route('/day6',methods=['POST','GET'])
@login_required
def day6():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 6, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day6.html',form=form,message=message)

@app.route('/day7',methods=['POST','GET'])
@login_required
def day7():
    message=None
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(day1="Dzień 7, "+form.answer.data, author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day7.html',form=form,message=message)



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


@app.route('/users',methods =["GET"])
def users():
    users = User.query.all()
    
    for user in users:
        x = user.answers
        for answer in x:
            useranswer=(answer.day1)
            answer_arry=useranswer.split(",")
            
            if (answer_arry[0]=="Dzień 1"):
                correctDay1 = [" xdd","ziemniak","polonez","gitara","samochód","melanz"]    
                a = set(answer_arry)
                b = set(correctDay1)
                result1=len(a&b)
                
            elif (answer_arry[0]=="Dzień 2"):
                a = set(answer_arry)
                b = set(correctDay1)
                result2 = len(a&b)
                
    

    return render_template('users.html',users=users,result1=result1)


######## LOGOUT ###########
@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')