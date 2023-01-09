from flask import render_template, request, flash, session, url_for, redirect
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from app import app


@app.route('/', methods=['GET'])
def root():
  if current_user.is_authenticated:
     return render_template("home.html")
  return render_template("login.html")


@app.route("/protected",)
@login_required
def protected():
    return render_template("protected.html")


@app.errorhandler(404)
def invalid_route(e):
  return render_template("404.html")
