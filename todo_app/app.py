from flask import Flask, request,  render_template, redirect
from  todo_app.data.session_items import  get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET'])
def index():   
    return render_template('index.html', items = get_items())

@app.route ('/additem', methods = ['POST'])
def add_todo():
    add_item(request.form["addtask"])
    return redirect('/')