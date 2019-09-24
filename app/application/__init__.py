import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from logging.config import dictConfig


# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
#r = FlaskRedis()


def create_app(test_config=None):
    """Initialize the core application."""

    # Create config for logging
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter': 'default'
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })

    # Create app
    app = Flask(__name__, instance_relative_config=False)

    # Create logs in various modes
    app.logger.debug('Logging working...')
    app.logger.info('Logging working...')
    app.logger.warning('Logging working...')
    app.logger.error('Logging working...')
    app.logger.critical('Logging working...')
    
    # Configure app
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        # Include routes
        from . import routes
        from . import auth
        from . import home

        # Register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(home.home_bp)
        
        db.create_all()

        return app
