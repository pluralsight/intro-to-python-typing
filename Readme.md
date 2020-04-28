# intro-to-python-typing
A practical introduction to Python's type annotation features (and the `typing` module), via simple, hackable examples.

(The examples currently use the typing syntax introduced in Python 3.6 - Backwards-compatible Python 2 examples may be added in a future update.)

These examples are intended to be self-explanatory to a Python developer, with minimal setup.

In addition to Python 3.6+, you'll also need the `mypy` type validator installed to experiment with the provided code:

```
pip install mypy
```

(optionally, inside a virtualenv or other environment wrapper, to keep this from affecting your local Python libraries!)

Once you've got all the requirements in place, you should be able to simply run

```
mypy examples/
```

In the base folder, and see a confirmation message like `Success: no issues found in 18 source files`.

You can now begin the tutorial track here.

(There are currently 16 examples, but only a few have detailed tutorials at the moment - I hope to improve this in the near future.)

---
If you have any feedback, questions, or Typing features you'd like to see covered, please let me know on Pluralsight Slack as @david.sturgis, or via GitHub Issues (or a PR) on this repo. Thanks!