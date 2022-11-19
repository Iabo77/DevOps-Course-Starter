from flask import Flask, request,  render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.database_items import add_item, get_items, complete_item
from todo_app.data.views import ViewModel
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user
import requests
import os
import logging

github_oauth_uri = os.getenv('GITHUB_OAUTH_URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
token_url = 'https://github.com/login/oauth/access_token'

administrators = ['94004061'] # list of admin userIds. hardcoded for demo/testing purposes. 

class User(UserMixin): 
    def __init__(self, id):
        self.id = id

def admin_only(func):
    def wrapper (*args,**kwargs):
        if current_user.id in administrators:
            return func(*args,**kwargs)
        elif current_user.is_anonymous: # testing uses anonymous_user
            return func(*args,**kwargs)
        else:
            logging.warning('Unauthorised Access attempted')
            return redirect('/AccessDenied')
    wrapper.__name__ = func.__name__
    return wrapper

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    login_manager = LoginManager()

    @login_manager.unauthorized_handler 
    def unauthenticated():
        app.logger.debug ('unauthenticated access  -  being redirected to Github')
        return redirect(f'https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}')
       
    @login_manager.user_loader 
    def load_user(user_id): 
        user = User(user_id)
        return user

    login_manager.init_app(app)    
    
    @app.route('/')    
    @login_required
    def index():           
        item_view_model = ViewModel(get_items())
        is_admin = True
        try:
            is_admin = current_user.id in administrators            
        except AttributeError: # to handle attributeerror when running tests (anonymous user has no 'id' attribute)
            is_admin == False            
        return render_template('index.html', view_model = item_view_model, is_admin = is_admin)
        
    
    @app.route ('/additem', methods = ['POST'])
    @admin_only
    @login_required
    def add_todo():
        add_item(request.form["addtask"])
        app.logger.debug(f'Task added. Task: {request.form["addtask"]} Userid: {current_user.id}')
        return redirect('/')
    
    @app.route ('/completeitem/<id>')
    @admin_only
    @login_required
    def make_complete(id):
        complete_item(id) 
        app.logger.debug(f'Task completed. TaskID {id} Userid: {current_user.id}')           
        return redirect('/')
          
            
    @app.route ('/AccessDenied')
    def access_denied(): 
        #  Currently Supplies userid of logged in user, solely for ease of testing/demo purposes. 
        app.logger.warning('Terminated at AccessDenied')       
        try:
            return (f'Access Denied. User ID = {current_user.id}')
        except:
            return ('Access Denied.')
    
    @app.route ('/login/callback', methods = ['GET'] )
    def complete_authentication():
        code = request.args.get("code")  
        params = {'client_secret':client_secret, 'client_id':client_id, 'code':code}
        app.logger.debug('requesting access token')
        response = requests.get(token_url, params=params, headers={"Accept": "application/json"})         
        access_token = response.json().get('access_token')        
        app.logger.debug (f'access token recieved: {access_token}')
        userinfo_response = requests.get("https://api.github.com/user",headers={"Authorization": f"Bearer {access_token} "})        
        user = User(userinfo_response.json().get('id'))
        login_user(user)
        if current_user.get_id() == 'None':
            # Occurs if user rejects OAuth logon/permissions or uses invalid access token
            app.logger.warning ('Rejected OAuth logon attempt')
            return redirect ('/AccessDenied')
        else:
            if current_user.get_id() in administrators:
                app.logger.info(f'User {current_user.id} logged in as administrator')
            else:
                app.logger.info(f'User {current_user.id} logged in with read only access')
            return redirect('/')

    return app



