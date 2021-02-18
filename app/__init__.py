import os

from flask            import Flask
from flask_login      import LoginManager
#from flask_bcrypt     import Bcrypt
from flask_mail import Mail

from app.general.general import general_bp
from app.auth.auth import auth_bp
from app.errors.error import error_bp


# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.DevConfig')


#register blueprints
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(error_bp)



