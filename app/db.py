from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_name = "database.db"

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    with app.app_context():
        db.create_all()