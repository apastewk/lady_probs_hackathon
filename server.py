"""Server file for Task Manager."""

#######################
#### Configuration ####
#######################

#Access local env variables
import os

from jinja2 import StrictUndefined

# Flask: A class that we import. An instance of this class will be the
# WSGI application.

from flask import Flask, render_template, request, flash, redirect, session

#Use toolbar for debugging
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db


# Instantiates Flask and "__name__" informs Flask where to find files.
# Instantiates Flask. "__name__" is a special Python variable for the name of
# the current module. This is needed so that Flask knows where to look for
# templates, static files, and so on.
app = Flask(__name__, static_url_path='/static')

#Set a secret key to enable the flask session cookies and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "seKriTz")

# Prevents the need to restart server when HTML/CSS is changed.
app.jinja_env.auto_reload = True

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined

@app.route()

# Listening or requests
if __name__ == "__main__":

    connect_to_db(app)

    #Create tables from models.py
    db.create_all(app=app)

    #Set debug=True in order to invoke the DebugToolbarExtension
    app.debug = True

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True
    # app.config['Testing'] = True
    #Use of debug toolbar
    DebugToolbarExtension(app)

    connect_to_db(app)

    #Create tables from models.py
    db.create_all(app=app)

    #Run app locally (full)
    #Points to port to use and turns on debugger
    app.run(port=5050, debug=True, host='0.0.0.0')

    #Run app via Heroku
    # PORT = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=PORT)
