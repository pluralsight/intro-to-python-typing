"""
Lists can have typed contents; Dicts can type [Keys: Values]
"""
from typing import List, Dict

LetterList = List[str]

LetterIndexMap = Dict[str, int]

def map_strings_by_index(my_list: LetterList) -> LetterIndexMap:
    return {letter: index for index, letter in enumerate(my_list)}

letter_list = ['A', 'B', 'C', 'D', 'E']
indexed_strings = map_strings_by_index(letter_list)

assert indexed_strings['C'] == 2
