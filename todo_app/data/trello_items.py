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
    def from_trello_card(cls, card, status):
        return cls(card['id'], card['name'], status)


api_key = os.getenv('KEY')
api_token = os.getenv('TOKEN')
trello_board_id = os.getenv('BOARD_ID')

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

def get_items_trello():        
    open_cards = []    
    card_list = get_cards_from_trello()
    list_dictionary = get_lists_from_trello() 
    for card in card_list:
        status_of_card = list_dictionary.get(card['idList'])
        open_cards.append(Item.from_trello_card(card, status_of_card))       
    return session.get('items', _DEFAULT_ITEMS.copy())
 
def get_cards_from_trello():
    open_cards = []
    get_cards_params = {'key':api_key, 'token':api_token, 'filter':'open'}
    get_cards_uri = f'https://api.trello.com/1/boards/{trello_board_id}/cards'
    get_cards_request = requests.get(get_cards_uri, params=get_cards_params)
    json_cards = get_cards_request.json()   
    return open_cards

def get_lists_from_trello():
    list_dict = {}
    get_board_lists_params = {'key':api_key, 'token':api_token}
    get_board_lists_uri = f'https://api.trello.com/1/boards/{trello_board_id}/lists'    
    get_board_lists_request = requests.get(get_board_lists_uri, get_board_lists_params)    
    json_lists = get_board_lists_request.json()
    for list in json_lists:
        list_dict.update ({list['id'] : list['name']})
    return list_dict 
    


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
