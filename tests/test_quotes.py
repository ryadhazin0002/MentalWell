import unittest
from unittest.mock import MagicMock
from src import Quote, QuoteFunctions

class TestQuoteFunctions(unittest.TestCase):
    def setUp(self):
        self.mock_database = MagicMock()
        self.quote_functions = QuoteFunctions()
        self.quote_functions.database = self.mock_database

    def test_getAll(self):
        # Mocka och testa the execute_query method of the database to returnera samma data
        self.mock_database.execute_query.return_value = [(1, "Don’t let what you cannot do interfere with what you can do.", "John Wooden"), (2, "A person who never made a mistake never tried anything new.", "Albert Einstein")]
        
        quotes = self.quote_functions.getAll()

        self.assertEqual(len(quotes), 2)
        self.assertEqual(quotes[0].id, 1)
        self.assertEqual(quotes[0].text, "Don’t let what you cannot do interfere with what you can do.")
        self.assertEqual(quotes[0].author, "John Wooden")
        self.assertEqual(quotes[1].id, 2)
        self.assertEqual(quotes[1].text, "A person who never made a mistake never tried anything new.")
        self.assertEqual(quotes[1].author, "Albert Einstein")

    def test_set_current_quote(self):
        # Test setting a current quote by index
        quote = self.quote_functions.set_current_quote(0)
        self.assertEqual(quote.id, 1)
        self.assertEqual(quote.text, "Don’t let what you cannot do interfere with what you can do.")
        self.assertEqual(quote.author, "John Wooden")

    def test_next_quote(self):
        # Test moving next quote
        self.quote_functions.set_current_quote(0)
        next_quote = self.quote_functions.next_quote()
        self.assertEqual(next_quote.id, 2)
        self.assertEqual(next_quote.text, "A person who never made a mistake never tried anything new.")
        self.assertEqual(next_quote.author, "Albert Einstein")

    def test_previous_quote(self):
        # Test moving previous quote
        self.quote_functions.set_current_quote(1)
        prev_quote = self.quote_functions.previous_quote()
        self.assertEqual(prev_quote.id, 1)
        self.assertEqual(prev_quote.text, "Don’t let what you cannot do interfere with what you can do.")
        self.assertEqual(prev_quote.author, "John Wooden")

    def test_current_quote(self):
        # Testa getting the current quote
        self.quote_functions.set_current_quote(0)
        current_quote = self.quote_functions.current_quote()
        self.assertEqual(current_quote.id, 1)
        self.assertEqual(current_quote.text, "Don’t let what you cannot do interfere with what you can do.")
        self.assertEqual(current_quote.author, "John Wooden")

if __name__ == '__main__':
    unittest.main()
