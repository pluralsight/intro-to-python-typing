"""
Annotating with core types: No imports required!
bool, int, float, str, bytes
"""
def triple(value: int) -> int:
    return value * 3

assert triple(3) == 9

"""
These both "work"... but don't match our annotations!
"""
# assert triple_annotated('?') == '???'
# assert triple_annotated(['*']) == ['*', '*', '*']
