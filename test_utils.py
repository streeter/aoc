from utils import read_lines_as_matrix


def test_read_lines_as_matrix():
    lines = ["..X...", ".SAMX."]

    mat = read_lines_as_matrix(lines)

    assert mat == [[".", ".", "X", ".", ".", "."], [".", "S", "A", "M", "X", "."]]
