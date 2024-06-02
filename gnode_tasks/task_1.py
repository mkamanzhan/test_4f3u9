from typing import NamedTuple

from gnode import GNode, dict_to_gnode


def walt_graph(node: GNode) -> list[str]:
    """
    Returns a list containing every GNode in the graph starting with the given node.
    Each node appears in the list exactly once, meaning there are no duplicates.
    """
    result = []
    visited = set()
    queue = [node]

    while queue:
        current_node = queue.pop(0)

        if current_node.get_name() in visited:
            continue

        visited.add(current_node.get_name())
        result.append(current_node.get_name())

        queue.extend(current_node.get_children())

    return result


################################################################################
# Testing Algorithm


class TestCaseData(NamedTuple):
    data: dict[str, list[str]]
    root_name: str
    expected: list[str]


test_cases = [
    TestCaseData(  # Common Case with duplicates
        data={
            "a": ["b", "c"],
            "b": ["c", "d"],
            "c": ["e"],
            "d": ["f"],
            "e": ["f"],
        },
        root_name="a",
        expected=["a", "b", "c", "d", "e", "f"],
    ),
    TestCaseData(  # Case without children
        data={
            "a": [],
            "b": ["c", "d"],
        },
        root_name="a",
        expected=["a"],
    ),
    TestCaseData(  # Case with one child
        data={
            "a": ["b"],
            "b": [],
        },
        root_name="a",
        expected=["a", "b"],
    ),
    TestCaseData(  # Case with linear graph
        data={
            "a": ["b"],
            "b": ["c"],
            "c": ["d"],
        },
        root_name="a",
        expected=["a", "b", "c", "d"],
    ),
]


def test_solution() -> None:
    for i, test_case in enumerate(test_cases):
        node = dict_to_gnode(test_case.data, test_case.root_name)
        result = walt_graph(node)
        if result != test_case.expected:
            message = (
                f"Test case {i} failed: expected {test_case.expected}, got {result}"
            )
            raise AssertionError(message)

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
