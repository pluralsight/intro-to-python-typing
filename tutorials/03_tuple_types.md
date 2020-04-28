## 3: Tuple Types (and return values)

You may have noticed that the built-in types we've used for annotations so far don't include more interesting data structures like Lists or Dictionaries - Those are a more complicated case, since we'll want to be able to specify the type of the container, _and_ the contents...

Let's start as simply as possible, by importing the `Tuple` type from the `typing` module:

[examples/03_tuple_types.py](https://github.com/pluralsight/intro-to-python-typing/examples/03_tuple_types.py)

The `Tuple` type is a `Generic`, a special class that allows us to describe a type that has parameters - in the case of a Tuple, we can specify the types we expect it to contain.

The syntax for this can be a little confusing at first - When adding parameters to a Generic Type, we use square brackets, essentially following list syntax. For example, to describe a Tuple that contains three integers, we would phrase it as:

```
Tuple[int, int, int]
```

What is the Tuple in this example expected to contain?

Tuples are important for annotating Python code - While Tuple may not be the first data type you reach for when writing code, it is a type that you often use implicitly: When a callable (function or method) returns multiple values, it is returning them as a Tuple!

Therefore, if we want to annotate the return type of a function that returns multiple values, we need to describe it as a Tuple. Let's give the example a try:

```
python examples/03_tuple_types.py
```

It works, and demonstrates that we can store the returned data as a tuple, or unpack it directly into two variables, as usual.

```
mypy examples/03_tuple_types.py
```

And MyPy considers it valid as well.

While we can specify the number and types of the values we expect to be in the Tuple, we don't have to! Try removing the `[str, int]` parameters from the annotation, leaving only the word `Tuple`, and test it again.

It still works! But it's a lot less specific than before. (But this represents another "escape valve" for typing - You can make your annotations less specific, rather than dropping them entirely.)

However, without the parameters, MyPy is also less sure about how this function can be used...

Let's add another use case: A variable that we assert to be typed as a two-Tuple of `str`, `int` (the annotation we had been using for our function) and try to use it to store the result of `first_word_length`:

```
t: Tuple[str, int] = first_word_length("Hello world!")
```

And run it through MyPy again...

MyPy does not approve! It knows that our `t` variable has very specific annotations, but our function doesn't guarantee anything about the Tuple it returns! Thus it reports that our annotations don't agree.

We could fix this by making `t` less specific, but let's try restoring the type parameters to our function's return value: Add `[str, int]` back to the end of `Tuple` on line 6, and try running MyPy again...

It works again - Now the detailed annotations we have on our variable are compatible with the (equally detaildd) annotations on our function's return value - MyPy can now "prove" that our annotations make sense, and our code will work.

Now that we've configured and used a Generic Type, let's also look at an easier way to make it more readable, and to avoid repeating ourselves...

## Up Next:

[Type Aliases](https://github.com/pluralsight/intro-to-python-typing/blob/master/tutorials/04_type_aliases.md)
