import os
import sys

def reverse_string( s ):
    return s[::-1]

def count_vowels(text):
    """Рахує кількість голосних літер у тексті."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
      if char in vowels:
        count += 1
    return count

def capitalize_words(text):
    """Робить першу літеру кожного слова великою."""
    if not text:
        return text
    return " ".join([word.capitalize() for word in text.split()])