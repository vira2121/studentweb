import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def studentadd():
    return flask.render_template("student.html")

@app.route("/search")
def search():
    return flask.render_template("search.html")

@app.route("/delete")
def delete():
    return flask.render_template("delete.html")

if(__name__) == "__main__":
    app.run()