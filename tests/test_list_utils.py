import pytest

from we_are_venom.utils.lists import flat


@pytest.mark.parametrize(
    'test_value, expected_result', [
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2, 3]], [1, 2, 3]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[]], []),
    ],
)
def test_flat(test_value, expected_result):
    assert flat(test_value) == expected_result
