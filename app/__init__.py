from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    '''
    This is a method for creating the app instance
    '''
    app = Flask(__name__)

    #Create the app configurations
    app.config.from_object(config_options[config_name])

    #Initialise the flask extenstions
    bootstrap.init_app(app)

    #Registration of the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Setting up config
    from .requests import configure_request
    configure_request(app)

    return app

