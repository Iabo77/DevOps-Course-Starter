from re import A
import pytest
from datetime import datetime, timedelta
from todo_app.data.trello_items import Item
import todo_app.data.views


def generate_cards_for_test(list_to_use):
    cards = []
    for args in list_to_use:
        cards.append (Item(args[0], args[1], args[2]))
    return cards

#hardcoded date time values to test datetime logic consistently
date_today = datetime(2022,6,15)
date_yesterday = datetime(2022,6,14)
date_last_week = datetime(2022,6,8)
date_way_back = datetime(2000,1,1)    

cards_todo = (    
    (1, 'To Do Card 1', 'To Do', date_today),
    (2, 'To Do Card 2', 'To Do', date_yesterday),
    (3, 'To Do Card 3', 'To Do', date_last_week),
    (4, 'To Do Card 4', 'To Do', date_way_back)    
)

cards_done = (    
    (11, 'Done Card 1', 'Done', date_today),
    (12, 'Done Card 2', 'Done', date_yesterday),
    (13, 'Done Card 3', 'Done', date_last_week),
    (14, 'Done Card 4', 'Done', date_way_back),
)

cards_doing = (    
    (21, 'Done Card 1', 'Doing', date_today),
    (22, 'Done Card 2', 'Doing', date_yesterday),
    (23, 'Done Card 3', 'Doing', date_last_week),
    (24, 'Done Card 4', 'Doing', date_way_back),
)

cards_mixed = (    
    (51, 'To Do Card 51', 'To Do', date_today),
    (52, 'To Do Card 52', 'To Do', date_yesterday),
    (53, 'To Do Card 53', 'To Do', date_last_week),
    (54, 'Doing Card 54', 'Doing', date_today),
    (55, 'Doing Card 55', 'Doing', date_yesterday),
    (56, 'Doing Card 56', 'Doing', date_last_week),
    (57, 'Done Card 57', 'Done', date_today),
    (58, 'Done Card 58', 'Done', date_yesterday),
    (59, 'Done Card 59', 'Done', date_last_week),
    (60, 'Done Card 60', 'Done', date_today),
    (61, 'Done Card 61', 'Done', date_yesterday),
    (62, 'Done Card 62', 'Done', date_last_week),
)

## test the generated test data is correct
def test_generated_data_todo_list():
    cards = generate_cards_for_test(cards_todo)
    assert len(cards) == 4
    for card in cards: 
        assert card.status == 'To Do'
    
def test_generated_data_done_list():
    cards = generate_cards_for_test(cards_done)
    assert len(cards) == len(cards_done)
    for card in cards: 
        assert card.status == 'Done'
    
def test_generated_data_doing_list():
    cards = generate_cards_for_test(cards_doing)
    assert len(cards) == len(cards_doing)
    for card in cards: 
        assert card.status == 'Doing'

def test_generated_data_mixed_list():
    cards = generate_cards_for_test(cards_mixed)
    assert len(cards) == len(cards_mixed)



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





