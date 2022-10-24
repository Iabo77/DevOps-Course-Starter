from flask import Flask, request,  render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.database_items import add_item, get_items, complete_item
from todo_app.data.views import ViewModel
from flask_login import LoginManager, login_required
import requests
import os

github_oauth_uri = os.getenv('GITHUB_OAUTH_URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('CALLBACK_URI')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    login_manager = LoginManager()

    @login_manager.unauthorized_handler 
    def unauthenticated():
        return redirect(f'https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}')
       
    @login_manager.user_loader 
    def load_user(user_id): 
        pass # We will return to this later 
    login_manager.init_app(app)
    
    
    @app.route('/')
    @login_required
    def index():   
        item_view_model = ViewModel(get_items())
        return render_template('index.html', view_model = item_view_model)
        
    @login_required
    @app.route ('/additem', methods = ['POST'])
    def add_todo():
        add_item(request.form["addtask"])
        return redirect('/')

    @login_required
    @app.route ('/completeitem/<id>')
    def make_complete(id):
        complete_item(id)
        return redirect('/')
  
    
    return app


app = create_app()

