from app import app
from app.models import db
from flask_uploads import configure_uploads, IMAGES, UploadSet

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

if __name__ == "__main__":
    app.init_db()
    app.run()