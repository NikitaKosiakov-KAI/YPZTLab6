from src.string_utils import reverse_string, count_vowels, capitalize_words

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("CI/CD") == "DC/IC"
    assert reverse_string("") == ""

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("GitHub Actions") == 5
    assert count_vowels("bcdfgh") == 0

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"
    assert capitalize_words("") == ""