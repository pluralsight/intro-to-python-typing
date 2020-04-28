"""
Optional indicates that a type could be None
"""
from typing import Optional

OptionalStr = Optional[str]

def clean_text(text: OptionalStr):
    if text is None:
        return text
    return text.lower().strip()

assert clean_text(' Hello World! ') == 'hello world!'

# Try commenting out lines 9 and 10 - MyPy will catch your mistake!
