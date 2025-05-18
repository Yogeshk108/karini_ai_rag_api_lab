import json
from typing import List, Dict, Union

from app.logger import get_logger

logger = get_logger(__name__)


class Generator:
    """
    A class to generate augmented data based on a query and context.
    """

    def generate(self, query: str, context: List[Dict[str, Union[int, str]]]) -> str:
        """
        Generate augmented data based on the provided query and context.
        :param query: query string
        :param context: matched data for given query string
        :return: serialised generated response from query and context
        """
        logger.info("Generating augmented data for query: %s", query)

        generated_data = {
            "query": query,
            "retrieved_data": [data.get("text") for data in context if data.get("text")]
        }

        logger.info("Final Generated Response: %s", generated_data)
        serialised_data = json.dumps(generated_data)

        logger.info("Yielding data in small chunks")
        for word in serialised_data.split(" "):
            yield word + " "
