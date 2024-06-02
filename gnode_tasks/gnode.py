import abc


class IGNode(abc.ABC):

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_children(self) -> list["GNode"]:
        pass


class GNode(IGNode):

    def __init__(
        self,
        name: str,
        children: list["GNode"] | None = None,
    ) -> None:
        self._name = name
        self._children = children or []

    def get_name(self) -> str:
        return self._name

    def get_children(self) -> list["GNode"]:
        return self._children

    def __repr__(self) -> str:
        return f"GNode({self._name})"


def dict_to_gnode(
    data: dict[str, list[str]],
    root_name: str = "root",
) -> GNode:
    def _build_node(name: str) -> GNode:
        children = data.get(name, [])
        return GNode(
            name,
            children=[_build_node(child) for child in children],
        )

    return _build_node(root_name)
