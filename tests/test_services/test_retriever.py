import unittest

from app.exceptions.exceptions import RAGException
from app.services.retriever import Retriever


class TestRetriever(unittest.TestCase):
    """
    Test class for the Retriever class.
    """
    def setUp(self):
        """
        Set up the test case by creating an instance of the Retriever class
        """
        self.retriever = Retriever()
        self.retriever.data_source = [
            {"id": 1, "data": "FastAPI is a fastest python web framework"},
            {"id": 2, "data": "Kafka is based on pub sub architecture"},
            {"id": 3, "data": "Kubernetes is container orchestration tool"},
        ]

    def test_empty_query(self):
        """
        Test the retrieve method with an empty query string.
        """
        result = self.retriever.retrieve("", 2)
        self.assertEqual(result, [])

    def test_no_match(self):
        """
        Test the retrieve method with a query string that does not match any data.
        """
        result = self.retriever.retrieve("no_match_word", 2)
        self.assertEqual(result, [])

    def test_all_match(self):
        """
        Test the retrieve method with a query string that matches all data.
        """
        result = self.retriever.retrieve(
            "fastapi KAFKA Kubernetes", 10)
        self.assertEqual(len(result), 3)

    def test_top_k_greater_than_matches(self):
        """
        Test the retrieve method with a query string that matches fewer items than the top_k parameter.
        """
        result = self.retriever.retrieve("is", 10)
        self.assertLessEqual(len(result), 3)

    def test_top_k_less_than_matches(self):
        """
        Test the retrieve method with a query string that matches more items than the top_k parameter.
        """
        result = self.retriever.retrieve("is", 1)
        self.assertEqual(len(result), 1)

    def test_top_k_zero(self):
        """
        Test the retrieve method with a top_k parameter of zero.
        """
        result = self.retriever.retrieve("the", 0)
        self.assertEqual(result, [])

    def test_exception_handling(self):
        """
        Test the retrieve method when the data source is None.
        """
        self.retriever.data_source = None
        with self.assertRaises(RAGException):
            self.retriever.retrieve("the", 1)
