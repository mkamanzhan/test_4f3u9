from fastapi import APIRouter
from pydantic import BaseModel

from src.entities.documents import get_documents_by_tags
from src.entities.tags import get_tag_children

router = APIRouter()


class Document(BaseModel):
    title: str
    uri: str
    tags: list[str]


@router.get("/taggedContent")
async def tagged_content_endpoint(tag: str) -> list[Document]:
    child_tags = get_tag_children(tag)
    all_tags = [tag] + child_tags
    documents = get_documents_by_tags(all_tags)
    return [
        Document(
            title=document.title,
            uri=document.uri,
            tags=list(document.tags),
        )
        for document in documents
    ]
