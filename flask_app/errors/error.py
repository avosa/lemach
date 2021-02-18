from flask import Blueprint, render_template

error_bp = Blueprint('error_bp', __name__,
    template_folder='templates')

@error_bp.errorhandler(404)
def page_not_found():

    return render_template('404.html'), 404



@error_bp.errorhandler(500)
def bad_request():
    return render_template('500.html'), 500