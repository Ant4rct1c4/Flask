from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='development'):

    app = Flask(__name__)

    app.config.from_object(
        config.get(config_name, config['default'])
    )

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views import main_bp
    from app.users.views import users
    from app.products.views import products
    from app.posts import post_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(post_bp)

    @app.errorhandler(404)
    def not_found(error):
        return render_template(
            '404.html',
            title='Page not found',
            theme='light'
        ), 404

    return app