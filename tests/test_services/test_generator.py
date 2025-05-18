import unittest
from app.services.generator import Generator


class TestGenerator(unittest.TestCase):
    """
    Test cases for the Generator class.
    """
    def setUp(self):
        """
        Set up the test case by creating an instance of the Generator class.
        """
        self.generator = Generator()

    def test_empty_query_and_context(self):
        """
        Test the generator with an empty query and context.
        """
        result = ''.join(self.generator.generate('', []))
        self.assertEqual('{"query": "", "retrieved_data": []} ', result)

    def test_context_with_missing_text(self):
        """
        Test the generator with context that has missing 'text' keys.
        """
        context = [{'id': 1}, {'text': 'kafka'}, {}, {'text': None}]
        result = ''.join(self.generator.generate('test', context))
        self.assertIn('"retrieved_data": ["kafka"]', result)

    def test_query_with_special_characters(self):
        """
        Test the generator with a query that contains special characters.
        """
        query = 'docker "kubernetes"\n'
        context = [{'text': 'bar'}]
        result = ''.join(self.generator.generate(query, context))
        self.assertIn('docker \\"kubernetes\\"\\n', result)

    def test_context_with_multiple_texts(self):
        """
        Test the generator with context that has multiple 'text' keys.
        """
        context = [{'text': 'fastapi'}, {'text': 'kafka'}, {'text': 'kubernetes'}]
        result = ''.join(self.generator.generate('q', context))
        self.assertIn('"retrieved_data": ["fastapi", "kafka", "kubernetes"]', result)

    def test_yielding_chunks(self):
        """
        Test the generator to ensure it yields chunks of text.
        """
        context = [{'text': 'foo bar'}]
        gen = self.generator.generate('q', context)
        chunks = list(gen)
        self.assertTrue(all(chunk.endswith(' ') for chunk in chunks))
        self.assertGreater(len(chunks), 1)
