import ssl
from sys import dont_write_bytecode
import datetime
import logging

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self): 
        todo_items = []
        for item in self._items:
            if item.status == 'To Do':
                todo_items.append(item)
        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == 'Doing':
                doing_items.append(item)
        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == 'Done':
                done_items.append(item)
        return done_items

    @property
    def recently_done_items(self):       
        recently_done_items = []
        starting_date = datetime.datetime.today() - datetime.timedelta(days=7)        
        for item in self._items:
            if item.status == 'Done' and item.date_modified > datetime.datetime.today() - datetime.timedelta(days=7):
                recently_done_items.append(item)
        logging.debug(f'Filtered:  {len(recently_done_items)} items completed in week period from date :  {starting_date}')
        return recently_done_items


