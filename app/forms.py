from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar")

class ToDoForm(FlaskForm):
    description = StringField("Descripción", validators=[DataRequired()])
    submit = SubmitField("Crear Tarea")

class DeleteTodoForm(FlaskForm):
    submit = SubmitField("Eliminar")

class UpdateTodoForm(FlaskForm):
    submit = SubmitField("Actualizar")