# Chapter 01 The Python Data Model

* We implement special methods when we want our objects to support and interact with fundamental language constructs such as:
  * Collections
  * Attribute access
  * Iteration (including asynchronous iteration using async for)
  * Operator overloading
  * Function and method invocation
  * String representation and formatting
  * Asynchronous programming using await
  * Object creation and destruction
  * Managed contexts using the with or async with statements

* dunder methods: under-under-method-under-under

## A Pythonic Card Deck

* `frenchdeck.py`

```python
#!/usr/bin/env python

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])

    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
```

* `namedtuple` can be used to build class with attributes and no methods.
* 2 advantages using special methods and python data model:
    * The user doesn't have to memorize the arbitrary method names for standard
      operations, `.size()` or `.length()`?
    * benefit from rich python SL, avoid reinventing wheels
* doctest example
    * When the output is too long, Luciano used the `# doctest: +ELLIPSIS` directive to make the doctest pass.

```python
>>> from frenchdeck import FrenchDeck, Card
>>> deck = FrenchDeck()
>>> for card in reversed(deck):  # doctest: +ELLIPSIS
...   print(card)
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...
```

* Then in the command line, just type

```shell
python -m doctest -v frenchdeck.doctest
```

* Because we defined `__getitem__`, the `FrenchDeck` is an iterable, and we can have the following.
  * There are 4 ways to make an object iterable, see [here](https://stackoverflow.com/questions/19151/how-to-build-a-basic-iterator).


```python
>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beasts') in deck
False
```

* We can also sort it

```python
>>> suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
>>> def spades_high(card):
...     rank_value = FrenchDeck.ranks.index(card.rank)
...     return rank_value * len(suit_values) + suit_values[card.suit]

>>> spades_high(Card('2', 'clubs'))
0
>>> spades_high(Card('A', 'spades'))
51

>>> for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
...     print(card)
```

* Although `FrenchDeck` implicitly inherits from the object class, most of its functionality is not inherited, but comes from leveraging the data model and composition. By implementing the special methods `__len__` and `__getitem__`, our `FrenchDeck` behaves like a standard Python sequence, allowing it to benefit from core language features (e.g., iteration and slicing) and from the standard library, as shown by the examples using `random.choice`, reversed, and `sorted`. Thanks to composition, the `__len__` and `__getitem__` implementations can delegate all the work to a list object, `self._cards`.
* How About Shuffling?
  * a `FrenchDeck` cannot be shuffled because it is immutable: In Chapter 13, we will fix that by adding a one-line `__setitem__` method.

## How special methods are used

* User should not call special methods, E.g., user do not call `my_object.__len__()`.
  * User call `len(my_object)`
  * Then python call `__len__` method you implemented.

* Built-in objects like `list, str, bytearray` has short cuts because they are implemented in C which has `PyVarObject`, which has an `ob_size` to hold size.
* Usually special method call is implicit, like `for i in x`, in this case, `iter()` is called, then `__iter__()` is called if implemented. Otherwise `x.__getitem__()` gets called.
* In general, a user should not call special methods directly. The only exception is to call `__init__` to invoke the initializer of the superclass in your own `__init__` implementation.
* If you need to invoke a special method, use `len, iter, str` etc.

### Emulating Numeric Types

* Here our goal is to further illustrate the use of special methods through another simple example.
* We will implement a class to represent two-dimensional vectors—that is, Euclidean vectors like those used in math and physics.
* See `vector.py` and `vector.doctest`.

```python
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

* The string returned by `__repr__` should be unambiguous and if possible, match the source code necessary to recreate the object being represented.

### Boolean Value of a Custom Type

* By default, instances of user-defined classes are considered truthy, unless either `__bool__` or `__len__` is implemented.
  * `bool(x)` calls `x.__bool__()` and uses the result.
  * `__bool__` is not implemented, Python tries to invoke `x.__len__()`, and if that returns zero, `bool` returns `False`.
  * Otherwise `bool` returns `True`.
* So we add the following function and tests:

```python
class Vector:
    # ...
		def __bool__(self):
        return bool(self.x or self.y)
```

```
>>> bool(Vector(1, 1)) is True
True
>>> bool(Vector(0, 0)) is False
True
```

### Collection API

* All the classes in the diagram are ABCs—abstract base classes.

<img src="./images/0102CollectionAPI.png" style="zoom:50%;" />

* Each of the top ABCs has a single special method. The `Collection` ABC (new in Python 3.6) unifies the three essential interfaces that every collection should implement:
  * `Iterable` to support for, unpacking, and other forms of iteration
  * `Sized` to support the len built-in function
  * `Container` to support the in operator
* Three very important specializations of Collection are:
  * `Sequence`, formalizing the interface of built-ins like `list` and `str`
  * `Mapping`, implemented by `dict`, `collections.defaultdict`, etc.
  * `Set`, the interface of the `set` and `frozenset` built-in types
* All the special methods in the `Set` ABC implement infix operators.
  * `a & b` computes the intersection of sets a and b, and is implemented in the `__and__` special method.

## Overview of Special Methods

* Use 3 tables to list almost all special methods.

## Why len Is Not a Method

* “practicality beats purity.”: The `len(x)` on built-in type needs to run very fast, since it just reads a field.
* But for custom objects, `len` calls `__len__`, This is a fair compromise between the need for efficient built-in objects and the consistency of the language.
* You can think of `abs` and `len` as unary operators.

## Chapter Summary

* By implementing special methods, your objects can behave like the built-in types
* A basic requirement for a Python object is to provide usable string representations of itself, one used for debugging and logging.
* Emulating sequences, as shown with the `FrenchDeck` example, is one of the most common uses of the special methods.
* Thanks to operator overloading, Python offers a rich selection of numeric types, from the built-ins to `decimal.Decimal` and `fractions.Fraction`, all supporting infix arithmetic operators.

# Chapter 02 An array of sequences

* This chapter will cover:
  * List comprehensions and the basics of generator expressions
  * Using tuples as records versus using tuples as immutable lists
  * Sequence unpacking and sequence patterns
  * Reading from slices and writing to slices
  * Specialized sequence types, like arrays and queues

## Overview of built-in sequence

* Container sequences: e.g.`list`, `tuple`, `collections.deque` holds different types.
    * holds references to the objects it contains.
* Flat sequences: e.g. `str`, `bytes`, `bytearray`, `memoryview`, `array.array` holds one type.
    * stores the value of its contents in its own memory space.
    * More compact, but are limited to holding primitive machine values like `bytes`, `integers`, and `floats`.
* Every Python object in memory has a header with metadata.
* The simplest one, `float`, has a value field and two metadata fields:
    * `ob_refcnt`: the object’s reference count, 8-byte in 64-bit python build.
    * `ob_type`: a pointer to the object’s type, 8-byte in 64-bit python build.
    * `ob_fval`: a C double holding the value of the `float`, 8-byte in 64-bit python build.
* So, an array of `floats` is much more compact than a tuple of `floats`.
* From mutable point of view:
    * mutable: `list`, `collections.deque`, `bytearray`, `memoryview`, `array.array`
    * immutable: `tuple`, `str`, `bytes`
* UML diagram:
    * `class Sequence(Container, Iterable, Sized)`
    * `class MutableSequence(Sequence)`

<img src="./images/0202SequenceUML.png" style="zoom:50%;" />

```python
"""

    >>> from collections import abc
    >>> issubclass(tuple, abc.Sequence)
    True
    >>> issubclass(list, abc.MutableSequence)
    True

"""
```

* Keep in mind these common traits: mutable versus immutable; container versus flat. They are helpful to extrapolate what you know about one sequence type to others.

## List Comprehension (list comps) and generator expressions (genexps)

* A quick way to build a sequence is using a list comprehension (if the target is a list) or a generator expression (for other kinds of sequences).

  * faster and more readable.
  * If you are not doing something with the produced list, you should not use that syntax.
  * Also, try to keep it short. If the list comprehension spans more than two lines, it is probably best to break it apart or rewrite it as a plain old for loop.

  ```python
  """
  # listcomp.py
  >>> symbols = '$¢£¥€¤'
  >>> codes = [ord(code) for code in symbols]
  >>> codes
  [36, 162, 163, 165, 8364, 164]
  """
  ```

* In Python code, line breaks are ignored inside pairs of `[]`, {}, or `()`. So you can build multiline lists, listcomps, tuples, dictionaries, etc., without using the `\` line continuation escape, which doesn’t work if you accidentally type a space after it.
* Also, when those delimiter pairs are used to define a literal with a comma-separated series of items, a trailing comma will be ignored. So, for example, when coding a multiline list literal, it is thoughtful to put a comma after the last item, making it a little easier for the next coder to add one more item to that list, and reducing noise when reading diffs.
* `map` and `filter` lost some readablity
* code: `cartesian.py`
* listcomp builds list, genexp builds other sequences.
* genexp saves memory
* If genexp is the single argument in a func call, no need to use `()`. Otherwise, `()` is needed, like in `arrary.arrary()` constructor

## Tuples are not just immutable lists

* The position in tuple is also important
* tuple unpacking (`tupleunpacking.py`):
    * works for Iterable object 
    * parallel assignment, can do swapping value elegently, i.e. `a, b = b, a`
	* When don't care a variable, use `_`
    * prefix an argument with a star when calling a function.
    * `*` can be used to grab excess items
    * but in parallel assignment, it can appear only once, but can be anywhere
* assignment can have nested tuples.
* `namedtuple`
    * Accept 2 arguments, 1st is the class name, second can be a list of string or a string with single
      space delimit
    * The instantiation must take positional arguments not iterables.
    * The elements can be accessed by name or position
    * Most useful attribute: '\_fields'
    * Most useful methods: `_make(iterable)`, `_asdict()`: return `OrderedDict`

# Chapter -1 Other Notes

* [Github link](https://github.com/fluentpython/example-code-2e)

## How to run doctest

* Example 1:

```python
"""
vector2d.py: a simplistic class demonstrating some special methods
It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.
This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

"""

class Vector:
  	# ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

```shell
 python vector.py -v
```

* Example 2

```python
>>> from vector import Vector
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
>>> v = Vector(3, 4)
>>> abs(v)
5.0
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
```

```shell
python -m doctest -v vector.doctest
```


# Further Reading

## Chapter 1

* [Data model chapter](https://docs.python.org/3/reference/datamodel.html).
* [Python in a nutshell](https://www.oreilly.com/library/view/python-in-a/9781491913833/).
* Python Essential Reference
* Python Cook‐ book, 3rd ed.
* The Art of the Metaobject Protocol (Author's favorite)