from typing import NamedTuple

from gnode import GNode, dict_to_gnode


def paths(node: GNode) -> list[list[str]]:
    """
    Returns a list of all paths from the given node to each leaf node
    """
    result = []
    path = []

    def _dfs(current_node: GNode) -> None:
        path.append(current_node.get_name())

        if not current_node.get_children():
            result.append(path.copy())
        else:
            for child in current_node.get_children():
                _dfs(child)

        path.pop()

    _dfs(node)
    return result


################################################################################
# Testing Algorithm


class TestCaseData(NamedTuple):
    data: dict[str, list[str]]
    root_name: str
    expected: list[list[str]]


test_cases = [
    TestCaseData(  # Case from document
        data={
            "a": ["b", "c", "d"],
            "b": ["e", "f"],
            "c": ["g", "h", "i"],
            "d": ["j"],
        },
        root_name="a",
        expected=[
            ["a", "b", "e"],
            ["a", "b", "f"],
            ["a", "c", "g"],
            ["a", "c", "h"],
            ["a", "c", "i"],
            ["a", "d", "j"],
        ],
    ),
    TestCaseData(  # Case without children
        data={
            "a": [],
            "b": ["c", "d"],
        },
        root_name="a",
        expected=[["a"]],
    ),
    TestCaseData(  # Case with one child
        data={
            "a": ["b"],
            "b": [],
        },
        root_name="a",
        expected=[["a", "b"]],
    ),
    TestCaseData(  # Case with linear graph
        data={
            "a": ["b"],
            "b": ["c"],
            "c": ["d"],
        },
        root_name="a",
        expected=[["a", "b", "c", "d"]],
    ),
    TestCaseData(  # Case with duplicates
        data={
            "a": ["b", "c"],
            "b": ["c", "d"],
            "c": ["e"],
            "d": ["f"],
            "e": ["f"],
        },
        root_name="a",
        expected=[
            ["a", "b", "c", "e", "f"],
            ["a", "b", "d", "f"],
            ["a", "c", "e", "f"],
        ],
    ),
]


def test_solution() -> None:
    for i, test_case in enumerate(test_cases):
        node = dict_to_gnode(test_case.data, test_case.root_name)
        result = paths(node)
        if result != test_case.expected:
            message = (
                f"Test case {i} failed: expected {test_case.expected}, got {result}"
            )
            raise AssertionError(message)

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
