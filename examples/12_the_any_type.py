"""
The Any type will match anything (skipping Type analysis)
"""
from typing import Dict, List, Any

# Mapping of str to whatever
StrObjectMap = Dict[str, Any]

# These are equivalent (but AnyList is more explicit)
GenericList = List
AnyList = List[Any]

my_map: StrObjectMap = {'A': 1, 'B': (), 'C': 'Hello'}

my_list: GenericList = ['Foo', 3.14]
any_list: AnyList = [1, 'A']
