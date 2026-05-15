from src.main import add_numbers, multiply_numbers, is_even

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(0, 10) == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False