from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ajdbnaifdanjeijafdno adpoiwjoi1481y50419n 019481 sdfh2 8f928h198 18ahd8h918y42jkafdalkxzbc'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app