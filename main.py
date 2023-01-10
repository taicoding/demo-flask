from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ["Todo 1", "Todo 2", "Todo 3"]


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response


@app.route("/hello")
def doxeando_ips():
    user_ip = request.cookies.get("user_ip")
    context = {"user_ip": user_ip, "todos": todos}
    return render_template("hello.html", **context)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
