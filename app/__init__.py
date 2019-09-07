from flask import Flask
from bootsrap import Bootstrap
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

    return app

