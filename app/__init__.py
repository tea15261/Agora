from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "2338724829301376494238947647623886783284y9"  # Set the secret key here
    app.config['DEBUG'] = True

    from app.db import init_db
    init_db(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app