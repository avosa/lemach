#General codebase
#templates should hold index, about, contact us pages
#index.py file

from flask import Blueprint, render_template

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates')

@general_bp.route('/')
@general_bp.route('/index.html')
def index():
    return render_template('index.html')

@general_bp.route('/about')
@general_bp.route('/about.html')
def about():

    return render_template('about.html')

@general_bp.route('/contact')
@general_bp.route('/contact.html')
def contact():

    return render_template('contact.html')

@general_bp.route('/services')
@general_bp.route('/services.html')
def list():

    return render_template('services.html')

# @general_bp.route('/')
# @general_bp.route('/')
# def ():

#     return render_template('')