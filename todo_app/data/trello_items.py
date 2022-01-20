from ast import Or
from flask import session
import requests
import os
import json

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status
        
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])


key = os.getenv('KEY')
token = os.getenv('TOKEN')
boardID = None
todo_listID = None
complete_listID = None
BOARD_NAME = 'todoapplication'
TODO_LIST_NAME = 'TO DO'
COMPLETE_LIST_NAME = 'COMPLETE'



_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

def get_items_trello():
    check_lists_exist() 
    json_cards = get_cards_json()
    json_lists = get_trello_lists()    
    for card in get_cards_json():
        Item.from_trello_card(card, json_lists)


def check_lists_exist():
    if boardID is None:
        create_trello_board()
    if complete_listID is None or todo_listID is None:
        create_trello_lists()

def get_cards_json():
    get_cards_params = {'key':key, 'token':token, 'filter':'open'}
    get_cards_uri = f'https://api.trello.com/1/boards/{boardID}/cards'
    get_cards_request = requests.get(get_cards_uri, params=get_cards_params)
    json_cards = get_cards_request.json()
    return json_cards

def get_trello_lists():
    get_lists_params = {'key':key, 'token':token}
    get_lists_uri = f'https://api.trello.com/1/boards/{boardID}/lists'    
    get_list_request = requests.get(get_lists_uri, get_lists_params)    
    json_lists = get_list_request.json()
    return json_lists

    print (json_lists)
    
    ##for card in json_cards:
    ##    Item.from_trello_card(card,list)

    return session.get('items', _DEFAULT_ITEMS.copy())

def check_board_exists():
    Create_boards()

def get_cards_json():
    get_cards_params = {'key':key, 'token':token, 'filter':'open'}
    get_cards_uri = f'https://api.trello.com/1/boards/{boardID}/cards'
    get_cards_request = requests.get(get_cards_uri, params=get_cards_params)
    json_cards = get_cards_request.json()
    return json_cards

def get_trello_lists():
    get_lists_params = {'key':key, 'token':token}
    get_lists_uri = f'https://api.trello.com/1/boards/{boardID}/lists'    
    get_list_request = requests.get(get_lists_uri, get_lists_params)    
    json_lists = get_list_request.json()
    return json_lists


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items_trello()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items_trello()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items_trello()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item
