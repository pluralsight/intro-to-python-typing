"""
(Remember that Classes are all instances of "type")
"""
class Foo:
    pass

def make_instance(this_type: type):
    instance = this_type()
    return instance

my_foo = make_instance(Foo)

assert isinstance(my_foo, Foo)
