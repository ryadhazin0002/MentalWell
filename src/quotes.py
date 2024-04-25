from connect_to_database import DatabaseManager


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
        
    def __init__(self) -> None:
        self.database = DatabaseManager()
        pass

    def getAll(self) -> list[Quote]:
        result = self.database.execute_query("Select * from quotes;")
        data = []
        for item in result:
            data.append(Quote(item[0], item[1], item[2]))
        return data
    