## 1: Basic Type Annotations

Python 3.6 added type annotation syntax, allowing you to mark the expected types of variables, callable (function and method) arguments, and their return values.

(The basic builtin types, `bool`, `int`, `float`, `str`, and `bytes` can be used directly as annotations, without any imports required.)

When defining a variable or argument, follow the name with a colon, and then the type, for example:
```
x = 0
```

Could be annotated as:

```
x: int = 0
```

This syntax works similarly for arguments:

```
def foo(x):
```

Could be annotated as:

```
def foo(x: int):
```

To annotate a return value, add an arrow `->` followed by the return type between the closing parenthesis and the ending colon:

```
def foo(x: int) -> int:
```

With that in mind, consider this example:

[examples/01_core_types.py](https://github.com/pluralsight/intro-to-python-typing/examples/01_core_types.py)

What do the type annotations imply?

Python does not inherently care about type annotations:

```
python examples/01_core_types.py
```

But MyPy will process them, and emit errors if any type annotations aren't being honored. (This example should validate successfully, without any changes):

```
mypy examples/01_core_types.py
```

Type Annotations can be more strict than Python itself allows! Try uncommenting the assertions on lines 13 and 14, and running the example again (with both Python and MyPy)...

These usages are allowed in Python, but since they're contrary to our annotations, MyPy will report errors.

The most basic "escape hatch" that MyPy provides is that (by default) it will only validate annotated code - If you now remove the `: int` and `-> int` annotations from the function, you'll find that MyPy no longer complains, even with the string and list use cases uncommented - there are no longer any annotations for it to validate.


## Up Next:

[Remember: type is a Type!](https://github.com/pluralsight/intro-to-python-typing/blob/master/tutorials/02_type_is_a_type.md)
