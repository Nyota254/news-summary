from flask import render_template,request,redirect,url_for
from . import main
#from ..requests import
#from ..models import 

@main.route('/')
def index():
    '''
    Home page function returns news sources
    '''

    title = "Welcome to news Summary a collection of all the news sources"
    return render_template('index.html',title = title)