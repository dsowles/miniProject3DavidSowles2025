
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # The index route handler
    @app.route('/')
    def index():
        return '<h1>Index</h1>'

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/pics')
    def pics():
        return '<h1>This Is The Pictures Page</h1>'
    
    @app.route('/blogs')
    def blogs():
        return '<h1>This Is The Blogs Page</h1>'
    
    # Import the database.
    # See https://flask.palletsprojects.com/en/stable/tutorial/database/
    from . import db
    db.init_app(app)

    # Import the authorization blueprints.
    # See https://flask.palletsprojects.com/en/stable/tutorial/views/
    from . import auth
    app.register_blueprint(auth.bp)

    return app