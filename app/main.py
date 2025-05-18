import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import RAGException
from app.logger import get_logger
from app.routers import query

logger = get_logger(__name__)

rag_app = FastAPI(
    title="Streaming RAG API Service",
    description="A lightweight Retrieval Augmented Generation API",
    version="1.0.0",
)
rag_app.include_router(query.router)


@rag_app.exception_handler(RAGException)
def custom_exception_handler(request: Request, exc: RAGException):
    """
    Custom exception handler for RAGException.
    :param request: Request Object
    :param exc: Exception Object
    :return: HTTP JSON response with error details
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict()
    )


if __name__ == "__main__":
    logger.info("Starting RAG API Server on 5001 port")
    config = uvicorn.Config("main:rag_app", port=5001, log_level="info")
    server = uvicorn.Server(config)
    server.run()
