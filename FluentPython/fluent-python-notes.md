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

* `vector.py`
* The string returned by `__repr__` should be unambiguous and if possible, match the source code necessary to recreate the object being represented.

# Chapter 02 An array of sequences

## Overview of built-in sequence

* `list`, `tuple`, `collections.deque` holds different types
* `str`, `bytes`, `bytearray`, `memoryview`, `array.array` holds one type

* From mutable point of view:
    * mutable: `list`, `collections.deque`, `bytearray`, `memoryview`, `array.array`
    * immutable: `tuple`, `str`, `bytes`

* UML diagram:
    * `class Sequence(Container, Iterable, Sized)`
    * `class MutableSequence(Sequence)`

## List Comprehension (list comps) and generator expressions (genexps)

* code: `listcomp.py`
* more readable
* line breaks are ignored inside `[], {}, ()`
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
