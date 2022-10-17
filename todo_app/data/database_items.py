from datetime import datetime, timedelta
from time import monotonic
from flask import session
#import requests
import os
#import json
import pymongo
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

connectionstring = os.getenv('CONNECTION_STRING')
client = pymongo.MongoClient(connectionstring)
database = client[os.getenv('DATABASE')]
collection = database[os.getenv('COLLECTION')]

def get_items():    
    items = []
    database_items = collection.find()
    for item in database_items:
        items.append(Item.from_database(item))        
    return items
        

def add_item(title):    
    collection.insert_one({'name':title,'status':'To Do','date_modified':datetime.now()})
        

def complete_item(_id):
    collection.update_one({'_id': ObjectId(_id)}, {"$set": {'status':'Done', 'date_modified':datetime.now()}})
    
