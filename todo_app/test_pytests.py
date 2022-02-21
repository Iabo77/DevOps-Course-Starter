from re import A
import pytest
from datetime import date, datetime, timedelta
from todo_app.data.trello_items import Item
from todo_app.data.views import ViewModel


#hardcoded date time values to test datetime logic consistently
date_today = datetime(2022,6,15)
date_yesterday = datetime(2022,6,14)
date_last_week = datetime(2022,6,8)
date_way_back = datetime(2000,1,1)    

cards_todo = (    
    Item(1, 'To Do Card 1', 'To Do', date_today),
    Item(2, 'To Do Card 2', 'To Do', date_yesterday),
    Item(3, 'To Do Card 3', 'To Do', date_last_week),
    Item(4, 'To Do Card 4', 'To Do', date_way_back)    
)

cards_done = (    
    Item(11, 'Done Card 1', 'Done', date_today),
    Item(12, 'Done Card 2', 'Done', date_yesterday),
    Item(13, 'Done Card 3', 'Done', date_last_week),
    Item(14, 'Done Card 4', 'Done', date_way_back),
)

cards_doing = (    
    Item(21, 'Done Card 1', 'Doing', date_today),
    Item(22, 'Done Card 2', 'Doing', date_yesterday),
    Item(23, 'Done Card 3', 'Doing', date_last_week),
    Item(24, 'Done Card 4', 'Doing', date_way_back),
)

cards_mixed = (    
    Item(51, 'To Do Card 51', 'To Do', date_today),
    Item(52, 'To Do Card 52', 'To Do', date_yesterday),
    Item(53, 'To Do Card 53', 'To Do', date_last_week),
    Item(54, 'Doing Card 54', 'Doing', date_today),
    Item(55, 'Doing Card 55', 'Doing', date_yesterday),
    Item(56, 'Doing Card 56', 'Doing', date_last_week),
    Item(57, 'Done Card 57', 'Done', date_today),
    Item(58, 'Done Card 58', 'Done', date_yesterday),
    Item(59, 'Done Card 59', 'Done', date_last_week),
    Item(60, 'Done Card 60', 'Done', date_today),
    Item(61, 'Done Card 61', 'Done', date_yesterday),
    Item(62, 'Done Card 62', 'Done', date_last_week),
)

cards_empty = ()


@pytest.mark.parametrize("card_list, expected", [(cards_todo, 4),(cards_doing,4), (cards_done,4), (cards_empty,0), (cards_mixed,12)])
def test_viewmodel_return_all_open_cards(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.items
    assert len(returned_items) == expected  
        
    
@pytest.mark.parametrize("card_list, expected", [(cards_todo, 4),(cards_doing,0), (cards_done,0), (cards_empty,0), (cards_mixed,3)])
def test_viewmodel_return_todo_cards(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.todo_items
    assert len(returned_items) == expected
    for item in returned_items:
        assert item.status == 'To Do'
    

@pytest.mark.parametrize("card_list, expected", [(cards_todo, 0),(cards_doing,0), (cards_done,4), (cards_empty,0), (cards_mixed,6)])
def test_viewmodel_all_return_done_cards(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.done_items
    assert len(returned_items) == expected
    for item in returned_items:
        assert item.status == 'Done'

@pytest.mark.parametrize("card_list, expected", [(cards_todo, 0),(cards_doing,4), (cards_done,0), (cards_empty,0), (cards_mixed,3)])
def test_viewmodel_return_doing_cards(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.doing_items
    assert len(returned_items) == expected
    for item in returned_items:
        assert item.status == 'Doing'


@pytest.mark.parametrize("card_list, expected", [(cards_todo, 0),(cards_doing,0), (cards_done,1), (cards_empty,0), (cards_mixed,2)])
def test_viewmodel_return_completed_today(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.doing_items
    assert len(returned_items) == expected
    for item in returned_items:
        assert item.status == 'Done'
        assert item.date_modified.date() == datetime.now.date()


@pytest.mark.parametrize("card_list, expected", [(cards_todo, 0),(cards_doing,0), (cards_done,3), (cards_empty,0), (cards_mixed,4)])
def test_viewmodel_return_completed_before_today(card_list, expected):
    test_view = ViewModel(card_list)
    returned_items = test_view.older_done_items
    assert len(returned_items) == expected
    for item in returned_items:
        assert item.status == 'Done' 
        assert item.date_modified.date() == datetime.now.date()       


@pytest.mark.parametrize("card_list, expected", [(cards_todo, True),(cards_doing, True), (cards_done, True), (cards_empty, True), (cards_mixed,False)])
def test_should_show_all_done_items(card_list, expected):
    test_view = ViewModel(card_list)
    for item in test_view:
        assert item.should_show_all_done == expected
        





