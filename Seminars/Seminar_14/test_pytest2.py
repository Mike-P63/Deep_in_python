import pytest
from task_2_sem_14 import Rect


@pytest.fixture
def r1():
    return Rect(2,2)

@pytest.fixture
def r2():
    return Rect(2,2)

@pytest.fixture
def r3():
    return Rect(4,4)

def test_value_error():
    with pytest.raises(ValueError):
        Rect(-2,2)

def test_sum_result_is_rect(r1, r2):
    assert isinstance(r1+r2, Rect)

def test_perimetr(r3):
    assert r3.per() == 16


if __name__ == '__main__':
    pytest.main(["-vv"])