
import unittest
from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    flash,
    url_for
)

from app import create_app
from app.forms import ToDoForm, DeleteTodoForm, UpdateTodoForm
from app.firestore_services import get_users,get_todos, put_todos, delete_todo, update_todo
from flask_login import login_required, current_user

app = create_app()


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


@app.route("/hello", methods=["GET", "POST"])
@login_required
def doxeando_ips():
    user_ip = session.get("user_ip")
    username = current_user.id
    todo_form = ToDoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    
    context = {
        "user_ip": user_ip,
        "todos": get_todos(user_id = username),
        "username": username,
        "todo_form" :todo_form,
        "delete_form":delete_form,
        "update_form":update_form
    }
    
    if todo_form.validate_on_submit():
        put_todos(user_id = username, descripcion = todo_form.description.data)
        flash("Tu tarea se creo con exito!")
        return redirect(url_for("doxeando_ips"))
    return render_template("hello.html", **context)

@app.route("/todos/delete/<todo_id>", methods=["POST"])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)
    return redirect(url_for("doxeando_ips"))

@app.route("/todos/update/<todo_id>/<int:done>", methods=["POST"])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id, todo_id, done)
    return redirect(url_for("doxeando_ips"))

if __name__ == "__main__":
    app.run(port=8080, debug=True)
