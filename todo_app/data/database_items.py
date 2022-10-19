from datetime import datetime, timedelta
from time import monotonic
from flask import session
import os
from item import Item
import pymongo
from bson import ObjectId

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
    
