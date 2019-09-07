from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_o_four(error):
    '''
    This is a function that renders the 404 error page
    '''
    return render_template('fourofour.html'),404
