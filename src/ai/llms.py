from langchain_openai import ChatOpenAI
from django.conf import settings

def get_openai_api_key():
    return settings.OPENAI_API_KEY

def get_openai_model(model="gpt-4o-mini"):
    '''Instantiate model object to generate chat completions.'''

    return ChatOpenAI(
        model=model,
        temperature=0,
        timeout=None,
        max_retries=2,
        api_key=get_openai_api_key(),
    )
