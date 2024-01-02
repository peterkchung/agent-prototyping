from fastapi import FastAPI
from src.agents.agents import agent_basic

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/converse")
def converse(query: str):
    # Use the ConversationalAgent to process the query
    response = agent_basic.process(query)
    return {"response": response}