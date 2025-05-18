# Karini.ai RAG API Lab Test


## Overview: 
Lightweight Streaming Retrieval-Augmented Generation (RAG) API
service using FastAPI and Pydantic. 

## Hot To Set up:

- Clone the repository
- Create a virtual environment using following command
```bash 
Python3 -m venv venv
```
- Activate the virtual environment using following command
- for MacOS/Linux
```bash
source venv/bin/activate
```
  - for windows
```bash
venv\Scripts\activate
```
- Install the dependencies using following command
```bash
pip install -r requirements.txt
```
- Run the FastAPI server using following command
```bash
uvicorn app.main:rag_app --port 5001
```
- To Test the API open swagger documentation on any browser using following url
  - http://localhost:5001/docs
- To open API redoc documentation on any browser using following url
  - http://localhost:5001/redoc
- To run unit test run following command
```bash
pytest -v
```
