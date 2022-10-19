class Item:
    def __init__(self, id, name, status = 'To Do', date_modified = datetime.now()):
        self.id = id
        self.name = name
        self.status = status
        self.date_modified = date_modified

    @classmethod
    def from_database(cls, item, status = 'To Do'):
        return cls(str(item['_id']), item['name'], item['status'], item['date_modified'])