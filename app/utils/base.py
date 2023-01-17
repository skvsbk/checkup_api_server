from databases import Database


class BaseUtil:
    def __init__(self, database: Database):
        self.database = database
