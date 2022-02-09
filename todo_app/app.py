from flask import Flask, request,  render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, get_items, complete_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():   
    return render_template('index.html', items = get_items())

@app.route ('/additem', methods = ['POST'])
def add_todo():
    add_item(request.form["addtask"])
    return redirect('/')

@app.route ('/completeitem/<id>')
def make_complete(id):
    complete_item(id)
    return redirect('/')

