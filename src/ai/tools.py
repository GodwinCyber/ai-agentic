from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from documents.models import Document

@tool
def list_documents(config: RunnableConfig):
    '''Get document for the current user'''
    print(config)
    metadata = config.get('metadata') or config.get('configurable') # depending on langchain version
    user_id = metadata.get('user_id') # extract user id from config metadata
    qs = Document.objects.filter(owner_id=user_id, active=True) # Only active documents
    # serialize django data to python dicts
    response_data = []
    for obj in qs:
        response_data.append(
            {
                "id": obj.id,
                "title": obj.title,
            }
        )
    return response_data

@tool
def get_document(document_id:int, config: RunnableConfig):
    '''Get details of a document for a current user'''
    metadata = config.get('metadata') or config.get('configurable') # depending on langchain version
    user_id = metadata.get('user_id')
    if user_id is None:
        raise Exception("Invalid user details, try again")
    
    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found")
    except Exception as e:
        raise Exception("Invalid request details for a document details, try again")
    response_data = {
        "id": obj.id,
        "title": obj.title,
    }
    return response_data

