import dataclasses
import json

from src.core.values import NotInitialized


@dataclasses.dataclass
class Tag:
    """
    A class representing a tag and its all children(direct and indirect).
    """

    name: str
    all_children: list[str]


_tags_data: dict[str, Tag] | NotInitialized = NotInitialized()
_data_path = "data/tags.json"


def get_tag_children(tag: str) -> list[str]:
    global _tags_data

    if isinstance(_tags_data, NotInitialized):
        _tags_data = _init_data()

    tag_data = _tags_data.get(tag)
    if tag_data is None:
        return []

    return tag_data.all_children


def _init_data() -> dict[str, Tag]:
    with open(_data_path) as file:
        data = json.load(file)

    result = {}
    for key in data.keys():
        result[key] = Tag(
            name=key,
            all_children=_get_all_children(data, key),
        )

    return result


def _get_all_children(data: dict[str, list[str]], name: str) -> list[str]:
    nodes = data.get(name)
    if nodes is None:
        return []

    result = []

    while nodes:
        node = nodes.pop()
        result.append(node)
        children = data.get(node)
        if children:
            nodes.extend(children)

    return result
