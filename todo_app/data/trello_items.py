from datetime import datetime, timedelta
from flask import session
import requests
import os
import json


class Item:
    def __init__(self, id, name, status = 'To Do', date_modified = datetime.now()):
        self.id = id
        self.name = name
        self.status = status
        self.date_modified = date_modified
        
    @classmethod
    def from_trello_card(cls, card, status = 'To Do'):
        return cls(card['id'], card['name'], status, card['dateLastActivity'])


api_key = os.getenv('KEY')
api_token = os.getenv('TOKEN')
trello_board_id = os.getenv('BOARD_ID')

def get_items():        
    open_cards = []    
    card_list = get_cards_from_trello()
    trello_lists = get_lists_from_trello()    
    for card in card_list:       
        card_status = (trello_lists[card['idList']]) 
        open_cards.append(Item.from_trello_card(card, card_status))           
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
        trello_lists.update ({list['id'] : list['name']}) 

    return trello_lists     

def add_item(title):        
    todo_list_id = get_lists_from_trello()['To Do']      
    post_new_card_uri = f'https://api.trello.com/1/cards'    
    post_new_card_params = {'key':api_key, 'token':api_token, 'idList':todo_list_id, 'name': title}
    post_new_card_request = requests.post(post_new_card_uri, post_new_card_params) 
    return post_new_card_request  

def complete_item(id):    
    open_cards = get_items()
    update_item = next((x for x in open_cards if x.id == id), None)
    if update_item == None:  # check required to resolve issue where multiple clicks on complete call hyperlink before page had updated caused error
        return "none"
    update_item.status = "Done"
    complete_list_id = get_lists_from_trello()['Done']       
    complete_card_uri = f'https://api.trello.com/1/cards/{id}'
    complete_card_params = {'key':api_key, 'token':api_token, 'idList':complete_list_id}
    complete_card_request = requests.put(complete_card_uri, complete_card_params) 
    return complete_card_request 
