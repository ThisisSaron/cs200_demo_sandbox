import main
import pytest

@pytest.mark.parametrize(
        ('input_x','input_y','expected'),
        (
            (0, 0, 1),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 2)
        )
)
def test_foo(input_x,input_y,expected):
    assert main.foo(input_x, input_y) == expected


@pytest.mark.parametrize(
        ('input_z','expected'),
        (
            (0, True),
            (1, False),
            (6, True),
            (7, False)
        )
)
def test_bar(input_z,expected):
    assert main.bar(input_z) == expected