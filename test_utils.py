from utils import read_lines_as_matrix, middle_of_list


def test_read_lines_as_matrix():
    lines = ["..X...", ".SAMX."]

    mat = read_lines_as_matrix(lines)

    assert mat == [[".", ".", "X", ".", ".", "."], [".", "S", "A", "M", "X", "."]]


def test_middle_of_list():
    assert middle_of_list([1, 2, 3]) == 2
    assert middle_of_list([1, 2, 3, 4, 5]) == 3
    assert middle_of_list([1, 2, 3, 4]) == 3

    assert middle_of_list(["1", "2", "3", "4", "5"]) == "3"
