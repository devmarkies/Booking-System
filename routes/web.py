from flask import Blueprint

'''
CONTROLLERS
'''
from controllers.AuthController import *
from controllers.DashboardController import *
from controllers.ContentController import *


'''
Blueprints
'''
auth = Blueprint('auth', __name__) #
dashboards = Blueprint('dashboards', __name__)#
contents = Blueprint('contents', __name__) #


'''
ROUTES
'''

#Auth
auth.route('login',  methods=['GET','POST'])(login)
auth.route('/logout')(logout)


#Dashboard
dashboards.route('/')(dashboad_index)

#home
contents.route('/home', methods=['GET'])(home_index)
contents.route('/home/update', methods=['POST'])(home_update)

#booked
contents.route('/booked_now', methods=['POST'])(book_now)
contents.route('/booked')(booked_index)
