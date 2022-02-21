import todo_app.data.trello_items

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):        
        return self._items

    @property
    def doing_items(self):
        return self._items

    @property
    def done_items(self):
        return self._items

    @property
    def recent_done_items(self):
        return self._items

    @property
    def older_done_items(self):
        return self._items
    
    @property
    def should_show_all_done(self):
         return False


    

    

