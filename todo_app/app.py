from flask import Flask, request,  render_template, redirect
from todo_app.data.session_items import  get_items, add_item
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items_trello

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():   
    return render_template('index.html', items = get_items_trello())

@app.route ('/additem', methods = ['POST'])
def add_todo():
    add_item(request.form["addtask"])
    return redirect('/')

@app.route ('/completeitem', methods = ['POST'])
def make_complete():
    add_item(request.form["addtask"])
    return redirect('/')

