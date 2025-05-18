from typing import Dict, List, Any


class RAGException(Exception):
    """
    Custom exception class to raise custom errors
    """
    def __init__(self, message: List[str], status_code: int, error_code: str):
        """
        Initialises the parameters for error contains
        :param message: actual formatted error message
        :param status_code: HTTP status code
        :param error_code: error type
        """
        self.message = message
        self.status_code = status_code
        self.error_code = error_code

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the error message to a dictionary format
        :return: dictionary object
        """
        return {
            "error": {
                "message": self.message,
                "code": self.error_code
            }
        }
