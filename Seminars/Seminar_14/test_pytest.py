import pytest
from task_1_sem_14 import remove_char


def test_no_change():
        assert remove_char("qwer") == "qwer"

def test_result_is_str():
        isinstance(remove_char("qwer"), str)
        
def test_in():
        assert " " in remove_char("qw er")

def test_nonenon():
        assert remove_char("qwer") is not None


if __name__ == '__main__':
    pytest.main(["-vv"])

