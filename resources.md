## Python Typing Resources

MyPy is the most featureful and "official" type validator for Python, and tends to support all the latest cool features:
https://mypy.readthedocs.io/

MyPy has a handy Typing Cheat Sheet which inspired this project - However, it's fairly terse, not a in very intuitive order (and some of the example code doesn't work anymore?)
https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

PyType is Google's entry into the Static Type Validation space - while it's not as up to date / on spec as MyPy, and is much more lenient by design, it can infer types when they aren't available(!) and has other features to help incrementally type legacy codebases:
https://google.github.io/pytype/

PyRight is Microsoft's own Static Type checker, and is optimized for performance in large code bases, includes a "watch" mode to auto-check files after edits, and integrates with VSCode:
https://github.com/microsoft/pyright

Pyre is Facebook's in-house Static Type checker: Like Microsoft's PyRight, it seems to focus on speed and scalability for large codebases, but I found it very opinioned and hard to set up, if you aren't working on a Facebook-shaped codebase:
https://pyre-check.org/

FastAPI is a powerful web framework that makes use of lots of modern Python features, not the least of which are type annotations - Use them to validate requests, auto-document your APIs, and more:
https://fastapi.tiangolo.com/

PyDantic uses type annotations for data validation and settings management, and is how FastAPI does some of its type-based magic:
https://pydantic-docs.helpmanual.io/

Typer helps you build smart command line tools with a minimum of repetition using type annotations!
https://typer.tiangolo.com/

Typical is another library for runtime usage of typing, including inference, validation, and enforcement of types with better performance than similar libraries:
https://python-typical.org/