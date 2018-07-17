# Chapter 01 The Python Data Model

* dunder methods: under-under-method-under-under

## A Pythonic Card Deck

* `namedtuple` can be used to build class with attributes and no methods.
* 2 advantages using special methods and python data model:
    * The user doesn't have to memorize the arbitrary method names for standard
      operations, `.size()` or `.length()`?
    * benefit from rich python SL, avoid reinventing wheels

## How special methods are used

* The string returned by `__repr__` should be unambiguous and, 
  if possible, match the source code necessary to recreate the object being represented.

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

* more readable
* line breaks are ignored inside `[], {}, ()`
* `map` and `filter` lost some readablity
