from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_template(name=None):
    return render_template("hello.html", name=name)

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="foxpi.ico"))

@app.errorhandler(404)
def error_404(error):
    return render_template("errors/error404.html")

if __name__ == "__main__":
    app.debug = False
    app.run("0.0.0.0", 60000)

