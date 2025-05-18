from fastapi import APIRouter
from fastapi import status
from fastapi.responses import StreamingResponse

from app.exceptions.exceptions import RAGException
from app.logger import get_logger
from app.schema_model.schema import RequestModel
from app.services.generator import Generator
from app.services.retriever import Retriever

logger = get_logger(__name__)
router = APIRouter(prefix="/api/v1.0", tags=["query"])

rag_retriever = Retriever()
rag_generator = Generator()


@router.post("/query")
def query_augmented_data(request: RequestModel):
    """
    Endpoint method to retrieve and generate data based on query
    :param request: Pydantic validated request body
    :return: streaming response contains retrieved data for given query
    """
    logger.info("Processing for query: %s", request.query)
    contexts = rag_retriever.retrieve(request.query, request.top_k)

    if not contexts:
        raise RAGException(
            message=[f"No context found for given query: {request.query}"],
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="resource_not_found"
        )

    def streaming_res_generator():
        logger.info("Starting to stream response for query: %s", request.query)
        for chunk in rag_generator.generate(request.query, contexts):
            yield chunk

    return StreamingResponse(streaming_res_generator(), media_type="application/json")
