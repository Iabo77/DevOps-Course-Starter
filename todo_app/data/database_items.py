from datetime import datetime, timedelta
import imp
from time import monotonic
from flask import session
import os
from .item import Item
import pymongo
from bson import ObjectId
import logging
from logging import Formatter
from loggly.handlers import HTTPSHandler

client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
database = client['todo_app']
collection = database['items']

logger = logging.getLogger(__name__)
if os.getenv('LOGGLY_TOKEN') is not None: 
    handler = HTTPSHandler(f"https://logs-01.loggly.com/inputs/{os.getenv('LOGGLY_TOKEN')}/tag/todo-app") 
    handler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")) 
    logger.addHandler(handler)

def get_items(): 
    logger.debug(f'database name : {database}') 
    items = []
    database_items = collection.find()
    for item in database_items:
        items.append(Item.from_database(item))   
    logger.debug(f"{len(items)} individual items collected from {collection.count_documents({})} total database records:## Item count and record count should match ##")    
    return items        

def add_item(title):    
    collection.insert_one({'name':title,'status':'To Do','date_modified':datetime.now()})        

def complete_item(_id):
    collection.update_one({'_id': ObjectId(_id)}, {"$set": {'status':'Done', 'date_modified':datetime.now()}})
    