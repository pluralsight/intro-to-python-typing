"""
The Tuple type is useful for describing return values
"""
from typing import Tuple

def first_word_length(text: str) -> Tuple[str, int]:
    word, *_ =  text.split(' ')
    return word, len(word)

word, length = first_word_length("Hello world!")

assert (word, length) == "Hello", 5
