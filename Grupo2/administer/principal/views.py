from flask import render_template, Blueprint, url_for, flash, redirect

principal = Blueprint('principal',__name__)

@principal.route('/')
def index():
    return render_template('home.html')
