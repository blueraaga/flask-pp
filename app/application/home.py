from flask import render_template, Blueprint, current_app

# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates/home',
                    static_folder='static')

@home_bp.route('/')
def index():
    """Home page."""
    current_app.logger.debug("Logging from app home page in debug mode.")
    return render_template('index.html')