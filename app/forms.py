from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Agregar')

class DeletTodoForm(FlaskForm):
    submit = SubmitField('Delete')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')