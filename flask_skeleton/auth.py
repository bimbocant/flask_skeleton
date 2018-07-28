#Authentication example Blueprint
#Blueprint -> way to organize related views and code
# rather than registering the view in the application
# they are registered in a blueprint, which is later
# registered in the application

import functools

from flask import (
    Blueprint, flash, g,redirect,render_template,request,session,url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_skeleton.db import get_db

#Blueprint called Auth
#__name__ tells wheres its defined, like the application
#url_prefix will be prepended to all the url associated with the bp
bp=Blueprint('auth',__name__,url_prefix='/auth')

#To register the bp place the new code in the create app function
# from . import auth
# app.register_blueprint(auth.bp)
