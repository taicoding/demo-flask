from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response


@app.route("/hello")
def doxeando_ips():
    user_ip = request.cookies.get("user_ip")
    return "Hola :D the hemos doxeado y esta es tu IP: {}".format(user_ip)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
