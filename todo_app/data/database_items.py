from datetime import datetime, timedelta
from time import monotonic
from flask import session
#import requests
import os
#import json
from pymongo import MongoClient
from bson import ObjectId


class Item:
    def __init__(self, id, name, status = 'To Do', date_modified = datetime.now()):
        self.id = id
        self.name = name
        self.status = status
        self.date_modified = date_modified

    @classmethod
    def from_database(cls, item, status = 'To Do'):
        return cls(str(item['_id']), item['name'], item['status'], item['date_modified'])

collection = MongoClient(os.getenv('CONNECTION_STRING')).todo_app.items

def get_items():    
    items = []
    database_items = collection.find()
    for item in database_items:
        items.append(Item.from_database(item))        
    return items
        

def add_item(title):    
    collection.insert_one({'name':title,'status':'To Do','date_modified':datetime.now()})
        

def complete_item(_id):
    collection.update_one({'_id': ObjectId(_id)}, {"$set": {"status":"Done"}})
    
