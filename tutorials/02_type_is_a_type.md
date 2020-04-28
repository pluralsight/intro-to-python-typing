## 2: Remember: "type" is a Type!

There's one more basic Type that is sometimes overlooked, but can be critical to proper annotations around Classes: the `type` Type.

While we refer to our classes as such, the `class` keyword in Python is used to create them - and instances of a class have that parent class as their type. But what type does a class have?

...Yeah, it's `type`. (And while were on it, what is the type of `type`? Well, I don't want to ruin your day, but it's also `type`, which might seem like a bizarre self-reference, but helps maintain the pattern of all python types having a type they can refer to.)

But don't worry about that too much for now: Let's try annotating a function that specifically accepts classes, by using `type`:

[examples/02_type_is_a_type.py](https://github.com/pluralsight/intro-to-python-typing/blob/master/examples/02_type_is_a_type.py)

As long as you can get over the weirdness of remembering `type` as the base of the type system, and the superclass of all classes, this works pretty well. Give it a try!

```
python examples/02_type_is_a_type.py
```

As usual, Python doesn't have a problem with it...

```
mypy examples/01_core_types.py
```

And MyPy accepts it as well.

You might be wondering if we could make this more specific, say, only allowing the `Foo` class specifically, simply by replacing `type` with `Foo` on line 7 - Unfortunately, it's not quite that simple, but we will dig into that later.

For now, let's get into the annotation of data structures, starting with Tuple:

## Up Next:

[Tuple Types (and return values)](https://github.com/pluralsight/intro-to-python-typing/blob/master/tutorials/03_tuple_types.md)
