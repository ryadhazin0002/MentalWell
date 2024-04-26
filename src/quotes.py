
from src.connect_to_database import DatabaseManager


class Quote:

    def __init__(self, id, text, author) -> None:
        self.id = id
        self.text = text
        self.author = author
        pass

    
    id: int
    text: str
    author: str

    
class QuoteFunctions:

    quotes: list[Quote]
    current_quote_index = None
        
    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.quotes = self.getAll()
        self.set_current_quote(0)
        pass

    def set_current_quote(self, index)-> Quote:
        if index < len(self.quotes):
            self.current_quote_index = index
            return self.quotes[index]
        

    def getAll(self) -> list[Quote]:
        result = self.database.execute_query("Select * from quotes;")
        if result != None:
            data = []
            for item in result:
                data.append(Quote(item[0], item[1], item[2]))
            return data
        return []
    
    def next_quote(self)-> Quote:
        if self.current_quote_index != len(self.quotes)-1:
           return self.set_current_quote(self.current_quote_index+1)
    
    def previous_quote(self)-> Quote:
        if self.current_quote_index != 0:
           return self.set_current_quote(self.current_quote_index-1)
    

    def current_quote(self):
        if self.current_quote_index is None:
            return None
        return self.quotes[self.current_quote_index]