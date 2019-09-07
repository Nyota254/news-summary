from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
from ..models import News_article,News_source 

@main.route('/')
def index():
    '''
    Home page function returns news sources
    '''

    news_sources = get_sources()


    title = "Welcome to news Summary a collection of all the news sources"
    return render_template('index.html',title = title, sources = news_sources)