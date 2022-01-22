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

def get_items():        
    open_cards = []    
    card_list = get_cards_from_trello()
    trello_lists = get_lists_from_trello() 
    for card in card_list:
        status_of_card = trello_lists.get(card['idList'])
        open_cards.append(Item.from_trello_card(card, status_of_card))     
    return open_cards
 
def get_cards_from_trello():   
    get_cards_uri = f'https://api.trello.com/1/boards/{trello_board_id}/cards'
    get_cards_params = {'key':api_key, 'token':api_token, 'filter':'open'}
    get_cards_request = requests.get(get_cards_uri, params=get_cards_params)
    return get_cards_request.json()

def get_lists_from_trello():
    trello_lists = {}
    get_board_lists_params = {'key':api_key, 'token':api_token}
    get_board_lists_uri = f'https://api.trello.com/1/boards/{trello_board_id}/lists'    
    get_board_lists_request = requests.get(get_board_lists_uri, get_board_lists_params)    
    for list in get_board_lists_request.json():
        trello_lists.update ({list['name'] : list['id']})
    return trello_lists     

def add_item(title):        
    todo_list_id = get_lists_from_trello()['To Do']      
    post_new_card_uri = f'https://api.trello.com/1/cards'    
    post_new_card_params = {'key':api_key, 'token':api_token, 'idList':todo_list_id, 'name': title}
    print(post_new_card_params)
    post_new_card_request = requests.post(post_new_card_uri, post_new_card_params) 
    return post_new_card_request  


"""
def save_item(item):
    
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item
"""

"""
def get_item(id):
    
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)
"""

