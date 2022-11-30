import ssl
from sys import dont_write_bytecode
import datetime
import logging
import os

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL'))

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
        logger.debug(f'{len(todo_items)} TODO items returned from total {len(self._items)} records')
        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == 'Doing':
                doing_items.append(item)
        logger.debug(f'{len(doing_items)} Doing  items returned from total {len(self._items)} records')
        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == 'Done':
                done_items.append(item)
        logger.debug(f'{len(done_items)} Completed items returned from total {len(self._items)} records')
        return done_items

    @property
    def recently_done_items(self):       
        recently_done_items = []
        starting_date = datetime.datetime.today() - datetime.timedelta(days=7)        
        for item in self._items:
            if item.status == 'Done' and item.date_modified > starting_date:
                recently_done_items.append(item)
        logger.debug(f'Filtered:  {len(recently_done_items)} items recently completed in week period from date :  {starting_date}')
        return recently_done_items


