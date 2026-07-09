from make_triangle import make_triangle


def test_make_triangle_returns_expected_triangle_for_three_rows():
    assert make_triangle(3) == "*\n**\n***\n"


def test_make_triangle_returns_empty_string_for_zero_rows():
    assert make_triangle(0) == ""
