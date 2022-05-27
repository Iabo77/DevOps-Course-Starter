from flask import Flask, request,  render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, get_items, complete_item
from todo_app.data.views import ViewModel



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():   
        item_view_model = ViewModel(get_items())
        return render_template('index.html', view_model = item_view_model)
        

    @app.route ('/additem', methods = ['POST'])
    def add_todo():
        add_item(request.form["addtask"])
        return redirect('/')

    @app.route ('/completeitem/<id>')
    def make_complete(id):
        complete_item(id)
        return redirect('/')
    
    return app


app = create_app()
