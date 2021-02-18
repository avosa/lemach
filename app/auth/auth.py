#All code related to authentication and authorization of routes
#Login
#Registration
#Forgot Password


from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates')

@auth_bp.route('/login')
@auth_bp.route('/login.html')
def login():

    return render_template('login.html')


@auth_bp.route('/register')
@auth_bp.route('/register.html')
def register():

    return render_template('register.html')


@auth_bp.route('/forgot-password')
@auth_bp.route('/forgot-password.html')
def forgort_password():

    return render_template('forgot-password.html')



@auth_bp.route('/rest-password')
@auth_bp.route('/rest-password.html')
def reset_password():

    return render_template('reset-password.html')