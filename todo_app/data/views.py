from sys import dont_write_bytecode
import todo_app.data.trello_items

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
    def recent_done_items():  
        
        recent_done_items = []
        return recent_done_items

    @property
    def older_done_items(self):
        older_done_items = ()

        
        
        return older_done_items
    
    @property
    def should_show_all_done(self):
        if len(self.done_items) > 5:
            return False
        else:  
            return True


    

    

