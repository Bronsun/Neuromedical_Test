from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from neuro.modules import User

class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Kontakt')
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Powtórz hasło', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Dodaj użytkownika')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).all()
        if user:
            raise ValidationError('Pacjent już został dodany.')

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

class AnswerForm(FlaskForm):
    answer = TextAreaField('Odpowiedz')
    submit = SubmitField('Wyślij odpowiedź')

class DeleteForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(),Length(min=2,max=20)])
    confirm_username = StringField('Powtórz nazwę', validators=[DataRequired(),EqualTo('username')])
    submit = SubmitField('Usuń użytkownika')

  