from flask import (
    Flask,
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config.update(
    DEBUG=False,
    ENV="development",
)
app.config["SECRET_KEY"] = "SUPER SECRETO"


todos = ["Jugar con el Michi", "Comprar comida del michi", "Amar al michi"]


class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html", error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session["user_ip"] = user_ip
    return response


@app.route("/hello", methods=["GET", "POST"])
def doxeando_ips():
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get("username")
    context = {
        "user_ip": user_ip,
        "todos": todos,
        "login_form": login_form,
        "username": username,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        return redirect(url_for("index"))
    return render_template("hello.html", **context)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
