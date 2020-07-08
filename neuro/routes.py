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
    correctDay1 = ["AGREST","BIGOS","FASOLA","FURIA","BOMBA","KRAWAT","JAROSZ","TRZCINA","CIASTO","KACZKA","CHMURA","SZYSZKA","NARTY","MATA","GŁOWA"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay1)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 1: "+form.answer.data,score="Dzień 1: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day1.html',form=form,message=message)

@app.route('/day2',methods=['POST','GET'])
@login_required
def day2():
    message=None
    form = AnswerForm()
    correctDay2 = ["PIŁKA","OWOC","LÓD","FUTRO","KOZA","ŁUK","NOGA","OPERA","POLE","TAJFUN","SIEĆ","WILK","ZĄB","SOK","KUCHARZ"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay2)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 2: "+form.answer.data,score="Dzień 2: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day2.html',form=form,message=message)

@app.route('/day3',methods=['POST','GET'])
@login_required
def day3():
    message=None
    form = AnswerForm()
    correctDay3 = ["MOTYL","LALKA","BĘBEN","KACZKA","TWARZ","PCHŁA","PIANA","FUTRO","SERCE","KOPYTO","SŁOIK","LAMPA","ŚNIEG","RYŚ","MAG"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay3)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 3: "+form.answer.data,score="Dzień 3: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day3.html',form=form,message=message)

@app.route('/day4',methods=['POST','GET'])
@login_required
def day4():
    message=None
    form = AnswerForm()
    correctDay4 = ["SERCE","OWCA","BAROK","REJS","PARK","TRAWA","KOT","WITRAŻ","PIANA","LAS","IGLOO","DZBAN","GLINA","ŁZA","KAPSEL"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay4)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 4: "+form.answer.data,score="Dzień 4: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day4.html',form=form,message=message)

@app.route('/day5',methods=['POST','GET'])
@login_required
def day5():
    message=None
    form = AnswerForm()
    correctDay5 = ["ASTER","CHŁOPIEC","DRZEWO","REJS","GUMA","KACZKA","HERB","MALINA","KAPSEL","ŁAWKA","KURA","MYSZ","MAKLER","ŁZA","PIANA"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay5)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 5: "+form.answer.data,score="Dzień 5: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day5.html',form=form,message=message)

@app.route('/day6',methods=['POST','GET'])
@login_required
def day6():
    message=None
    form = AnswerForm()
    correctDay6=["OPONA","RAJ","NOBEL","PALMA","TŁOK","SSAK","MGŁA","WAPŃ","ZUPA","URAN","TYGRYS","SĄD","REWIA","ZOO","SCENA"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay6)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 6: "+form.answer.data,score="Dzień 6: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day6.html',form=form,message=message)

@app.route('/day7',methods=['POST','GET'])
@login_required
def day7():
    message=None
    form = AnswerForm()
    correctDay7 = ["USTA","WIATRAK","ROBAK","OBUWIE","LUKIER","NAFTA","KSIĄŻE","LARWA","MAPA","IDEA","HALKA","JAWOR","BAK","HENNA","ANYŻ"]
    if form.validate_on_submit():
        answers=form.answer.data.upper()
        answer_arry=answers.split(",")
        a = set(correctDay7)
        b = set(answer_arry)
        score=str(len(a&b))
        answer = Answer(day1="Dzień 7: "+form.answer.data,score="Dzień 7: "+score+"/15", author=current_user)
        db.session.add(answer)
        db.session.commit()
        message = "Odpowiedz została wysłana!"
    return render_template('day7.html',form=form,message=message)



############## ADMIN PAGE ########################

@app.route('/admin2551',methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route('/add2551',methods=['GET','POST'])
def add():
    error="Pomyślnie dodano użytkownika"
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,password=form.password.data,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return render_template('add.html',form=form,error=error)
    return render_template('add.html',form=form)

@app.route('/delete2551', methods=['GET','POST'])
def delete():
    form = DeleteForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            error="Nie ma takiego użytkownika"
        else:
            db.session.delete(user)
            db.session.commit()
            error="Użytkownik został usunięty"
        return render_template('delete.html',form=form,error=error)
    return render_template('delete.html',form=form)


@app.route('/users2551',methods =["GET"])
def users():
    users = User.query.all()
    return render_template('users.html',users=users)#result1=result1)


######## LOGOUT ###########
@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')