from langchain.agents import create_agent
from .llms import get_openai_model
from ai.tools import document_tools

def get_document_agent():
    model = get_openai_model()
    agent = create_agent(
        model=model,
        tools=document_tools,
        system_prompt="You are helpful assistant in managing a user's documents within this app"
    )
    return agent
