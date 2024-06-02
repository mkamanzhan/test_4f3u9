import dataclasses
import json

from src.core.values import NotInitialized


@dataclasses.dataclass
class Document:
    title: str
    uri: str
    tags: set[str]


_documents_data: dict[str, Document] | NotInitialized = NotInitialized()
_data_path = "data/documents.json"


def get_documents_by_tags(tags: list[str]) -> list[Document]:
    global _documents_data

    if isinstance(_documents_data, NotInitialized):
        _documents_data = _init_data()

    result = []
    for document in _documents_data.values():
        if any(tag in document.tags for tag in tags):
            result.append(document)

    return result


def _init_data() -> dict[str, Document]:
    with open(_data_path) as file:
        data = json.load(file)

    result = {}
    for key, value in data.items():
        result[key] = Document(
            title=key,
            uri=value["uri"],
            tags=set(value["tags"]),
        )

    return result
