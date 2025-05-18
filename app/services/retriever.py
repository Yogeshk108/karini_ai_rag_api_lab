from typing import List, Dict, Union

from app.database.mock_database import DATA
from app.exceptions.exceptions import RAGException
from app.logger import get_logger

logger = get_logger(__name__)


class Retriever:
    """
    This class is responsible for retrieving documents from the data source based on the query.
    """

    def __init__(self):
        """
        Initializes the Retriever class with a data source.
        """
        self.data_source = DATA

    def retrieve(self, query: str, top_k: int) -> List[Dict[str, Union[int, str]]]:
        """
        Retrieves documents from the data source based on the query and returns the top_k results.
        :param query: query string
        :param top_k: number to select top k parameters from data source
        :return: context with matched data
        """
        try:
            logger.info("Starting to retrieve data for query: %s", query)
            unique_query_words = set(query.lower().split())
            matched_docs = []

            for doc in self.data_source:
                unique_data_words = set(doc["data"].lower().split())
                overlapping_word_count = len(unique_query_words.intersection(unique_data_words))

                if overlapping_word_count:
                    matched_docs.append({
                        "doc_id": doc.get("id"),
                        "text": doc.get("data"),
                        "overlapping_word_count": overlapping_word_count
                    })

            logger.info("Total documents found for given query are: %s", len(matched_docs))
            matched_docs.sort(key=lambda x: x["overlapping_word_count"], reverse=True)

            logger.info("Returning top %s documents", min(top_k, len(matched_docs)))
            return matched_docs[:min(top_k, len(matched_docs))]
        except Exception as error:
            logger.error("Error in retrieving the data: %s", str(error))
            raise RAGException(
                message=[str(error)],
                status_code=500,
                error_code='internal_server_error'
            )
