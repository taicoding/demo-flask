import unittest
from flask import (
    Flask,
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
    flash,
)

from app import create_app
from app.forms import LoginForm
from app.firestore_services import get_users,get_todos


app = create_app()





todos = ["Jugar con el Michi", "Comprar comida del michi", "Amar al michi"]




@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


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


@app.route("/hello", methods=["GET"])
def doxeando_ips():
    user_ip = session.get("user_ip")
    username = session.get("username")
    context = {
        "user_ip": user_ip,
        "todos": get_todos(user_id = username),
        "username": username,
    }
    return render_template("hello.html", **context)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
