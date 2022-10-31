from flask import Flask, request,  render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.database_items import add_item, get_items, complete_item
from todo_app.data.views import ViewModel
from flask_login import LoginManager, UserMixin, login_required, login_user
import requests
import os

github_oauth_uri = os.getenv('GITHUB_OAUTH_URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
token_url = 'https://github.com/login/oauth/access_token'


class User(UserMixin): 
    def __init__(self, id):
        self.id = id

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    login_manager = LoginManager()

    @login_manager.unauthorized_handler 
    def unauthenticated():
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
        return render_template('index.html', view_model = item_view_model)
        
    
    @app.route ('/additem', methods = ['POST'])
    @login_required
    def add_todo():
        add_item(request.form["addtask"])
        return redirect('/')

    
    @app.route ('/completeitem/<id>')
    @login_required
    def make_complete(id):
        complete_item(id)
        return redirect('/')
            
    @app.route ('/login/callback', methods = ['GET'] )
    def complete_authentication():
        code = request.args.get("code")  
        params = {'client_secret':client_secret, 'client_id':client_id, 'code':code}
        response = requests.get(token_url, params=params, headers={"Accept": "application/json"}) 
        access_token = response.json().get('access_token')
        userinfo_response = requests.get("https://api.github.com/user",headers={"Authorization": f"Bearer {access_token}"})
        user = User(userinfo_response.json().get('id'))
        login_user(user)
        return redirect('/')
    
               
    return app

app = create_app()

