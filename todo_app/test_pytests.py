from re import A
import pytest
from datetime import datetime
from todo_app.data.trello_items import Item
import todo_app.data.views

def generate_cards_for_test(list_to_use):
    cards = []
    for args in list_to_use:
        cards.append (Item(args[0], args[1], args[2]))
    return cards
    

cards_todo = (    
    (1, 'To Do Card 1', 'To Do'),
    (2, 'To Do Card 2', 'To Do'),
    (3, 'To Do Card 3', 'To Do'),
    (4, 'To Do Card 4', 'To Do'),
)

cards_done = (    
    (11, 'Done Card 1', 'Done'),
    (12, 'Done Card 2', 'Done'),
    (13, 'Done Card 3', 'Done'),
    (14, 'Done Card 4', 'Done'),
)

cards_doing = (    
    (21, 'Done Card 1', 'Doing'),
    (22, 'Done Card 2', 'Doing'),
    (23, 'Done Card 3', 'Doing'),
    (24, 'Done Card 4', 'Doing'),
)

cards_mixed = (    
    (1, 'To Do Card 5', 'To Do'),
    (2, 'To Do Card 6', 'To Do'),
    (3, 'Doing Card 5', 'Doing'),
    (4, 'Doing Card 6', 'Doing'),
    (5, 'Done Card 5', 'Done'),
    (6, 'Done Card 6', 'Done'),
)



def generate_test_cards():
    stub_card_data = ((1, 'To Do Card 1', 'To Do'),
                    ( ))
    
    
    

    

def stub_get_lists_json(url, params):
    return {"name": "ToDo"}

def stub_get_cards_json(url, params):
    return -1 

def stub_return_lists():
    pass
    



class CardsStubResponse():
    def json(self):
        return {}

def test_generated_data_todo_list():
    cards = generate_cards_for_test(cards_todo)
    assert len(cards) == 4
    for card in cards: 
        assert card.status == 'To Do'
    
def test_generated_data_done_list():
    cards = generate_cards_for_test(cards_done)
    assert len(cards) == 4
    for card in cards: 
        assert card.status == 'Done'
    
def test_generated_data_doing_list():
    cards = generate_cards_for_test(cards_doing)
    assert len(cards) == 4
    for card in cards: 
        assert card.status == 'Doing'

def test_generated_data_mixed_list():
    cards = generate_cards_for_test(cards_mixed)
    assert len(cards) == 6



def test_add_cards_to_items_class():
    assert -1

def test_create_one_item_card():
    assert -1

def test_multiple_item_cards():
    assert -1

def test_items_assigned_correct_status():
    assert -1 

def test_get_list_from_trello():    
    assert -1

def test_return_all_open_cards():
    assert -1 

def test_return_todo_cards():
    assert -1

def test_all_return_done_cards():
    assert -1

def test_return_doing_cards():
    assert -1

def test_return_completed_today():
    assert -1

def test_count_completed_today():
    assert -1

def test_return_completed_before_today():
    assert -1





