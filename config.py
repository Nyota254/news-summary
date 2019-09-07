import os

class Config:
    '''
    Class for configurations to be added during run-time
    '''
    
    NEWS_API_BASE_URL = https://newsapi.org/v2/sources?apiKey={}
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Class for configuarion to be added during production
    '''
    pass

class DevConfig(Config):
    '''
    Class for configuration to be run during development configuration
    '''
    DEBUG = True

#Dictionary for configurations
config_options = {
'development':DevConfig,
'production':ProdConfig
}




