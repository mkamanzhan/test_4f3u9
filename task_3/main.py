from typing import NamedTuple


def word_counts_in_file(file_path: str) -> dict[str, int]:
    with open(file_path, "r") as file:
        text = (
            file.read().lower().replace(",", " ").replace(".", " ").replace("\n", " ")
        )
        words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


################################################################################
# Testing Algorithm


class TestCaseData(NamedTuple):
    file_path: str
    expected: dict[str, int]


test_cases = [
    TestCaseData(  # Common Case
        file_path="task_3/test_cases/1.txt",
        expected={
            "a": 3,
            "the": 1,
            "of": 5,
            "in": 1,
            "com": 1,
            "you": 1,
            "that": 1,
            "energy": 1,
            "to": 1,
        },
    ),
    TestCaseData(  # Case without words
        file_path="task_3/test_cases/2.txt",
        expected={},
    ),
    TestCaseData(  # Case with one word
        file_path="task_3/test_cases/3.txt",
        expected={"a": 1},
    ),
]


def test_solution() -> None:
    for i, test_case in enumerate(test_cases):
        result = word_counts_in_file(test_case.file_path)
        if result != test_case.expected:
            message = (
                f"Test case {i} failed: expected {test_case.expected}, got {result}"
            )
            raise AssertionError(message)

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
