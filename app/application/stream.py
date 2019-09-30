import os

from flask import (redirect, render_template, flash, Blueprint, request,
                   session, url_for, current_app, make_response)

from gripcontrol import GripPubControl

# Blueprint Configuration
stream_bp = Blueprint('stream_bp',
                    __name__,
                    template_folder='templates/stream',
                    static_folder='static',
                    url_prefix='/stream')

@stream_bp.route('/home')
def home():
    return render_template('home.html')


@stream_bp.route('/view')
def view():
    # not much code here as all magic happens on client side / JS
    return render_template('view.html')


@stream_bp.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # obtain sent message
        message = request.form.get('message')
        message = 'event: ranstr\ndata: ' + message + '\n\n'
        # send sent message to be published to a channel on pushpin
        pub = GripPubControl({
            'control_uri': 'http://pushpin:5561'
            })
        pub.publish_http_stream('test', message)
        return render_template('send.html')

    elif request.method == 'GET':
        return render_template('send.html')
    else:
        return redirect(url_for('stream_bp.home'))


@stream_bp.route('/message/sse', methods=['GET'])
def message_sse():
    # not much code here as all magic happens on client side / JS
    #return with right headers
    resp = make_response("SSE response sent")
    resp.headers['Content-Type'] = 'text/event-stream'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Grip-Hold'] = 'stream'
    resp.headers['Grip-Channel'] = 'test'
    return resp

# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     """User login page."""
#     # Bypass Login screen if user is logged in
#     if current_user.is_authenticated:
#         return redirect(url_for('auth_bp.status'))
#     login_form = LoginForm(request.form)
#     # POST: Create user and redirect them to the app
#     if request.method == 'POST':
#         if login_form.validate():
#             # Get Form Fields
#             email = request.form.get('email')
#             password = request.form.get('password')
#             # Validate Login Attempt
#             user = User.query.filter_by(email=email).first()
#             if user:
#                 if user.check_password(password=password):
#                     login_user(user)
#                     next = request.args.get('next')
#                     return redirect(next or url_for('auth_bp.status'))
#         flash('Invalid username/password combination')
#         return redirect(url_for('auth_bp.login'))
#     # GET: Serve Log-in page
#     return render_template('login.html', form=LoginForm())


# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     """User sign-up page."""
#     current_app.logger.debug("signup controller entered")
#     signup_form = SignupForm(request.form)
#     current_app.logger.debug("signup form var made")
            
#     # POST: Sign user in
#     if request.method == 'POST':
#         current_app.logger.debug("signup form post confirmed")
#         current_app.logger.debug(signup_form)
#         if signup_form.validate():
#             current_app.logger.debug("signup form validated")
#             # Get Form Fields
#             name = request.form.get('name')
#             email = request.form.get('email')
#             password = request.form.get('password')
#             website = request.form.get('website')
#             existing_user = User.query.filter_by(email=email).first()
#             if existing_user is None:
#                 user = User(name=name,
#                             email=email,
#                             password=generate_password_hash(password, method='sha256'),
#                             website=website)
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user)
#                 return redirect(url_for('auth_bp.status'))
#             flash('A user already exists with that email address.')
#             return redirect(url_for('auth_bp.signup'))
#         else:
#             return render_template('/signup.html',  form=signup_form)
#     # GET: Serve Sign-up page
#     return render_template('/signup.html', form=SignupForm())


# @auth_bp.route("/logout")
# @login_required
# def logout():
#     """User log-out logic."""
#     logout_user()
#     return redirect(url_for('auth_bp.status'))


# @auth_bp.route("/status")
# def status():
#     """User status"""
#     return render_template('/status.html')


# @auth_bp.route("/details")
# def details():
#     """User details"""
#     return render_template('/details.html')


# @login_manager.user_loader
# def load_user(user_id):
#     """Check if user is logged-in on every page load."""
#     if user_id is not None:
#         return User.query.get(user_id)
#     return None


# @login_manager.unauthorized_handler
# def unauthorized():
#     """Redirect unauthorized users to Login page."""
#     flash('You must be logged in to view that page.')
#     return redirect(url_for('auth_bp.login'))
