from datetime import datetime, timedelta
import imp
from time import monotonic
from flask import session
import os
from .item import Item
import pymongo
from bson import ObjectId
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL'))


def get_items(): 
    client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = client[os.getenv('DATABASE')]
    collection = database[os.getenv('COLLECTION')]   
    items = []
    database_items = collection.find()
    for item in database_items:
        items.append(Item.from_database(item))   
    logger.debug(f"{len(items)} individual items collected from {collection.count_documents({})} total database records:## Item count and record count should match ##")    
    return items        

def add_item(title):    
    client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = client[os.getenv('DATABASE')]
    collection = database[os.getenv('COLLECTION')] 
    collection.insert_one({'name':title,'status':'To Do','date_modified':datetime.now()})        

def complete_item(_id):
    client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = client[os.getenv('DATABASE')]
    collection = database[os.getenv('COLLECTION')] 
    collection.update_one({'_id': ObjectId(_id)}, {"$set": {'status':'Done', 'date_modified':datetime.now()}})
    
