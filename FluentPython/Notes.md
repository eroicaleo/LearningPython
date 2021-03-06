# Chapter 01 The Python Data Model

* dunder methods: under-under-method-under-under

## A Pythonic Card Deck

* `frenchdeck.py`
* `namedtuple` can be used to build class with attributes and no methods.
* 2 advantages using special methods and python data model:
    * The user doesn't have to memorize the arbitrary method names for standard
      operations, `.size()` or `.length()`?
    * benefit from rich python SL, avoid reinventing wheels

## How special methods are used

* `vector.py`
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
