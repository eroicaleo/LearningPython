<!-- TOC depth:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Chapter 27 Class Coding Basics](#chapter-27-class-coding-basics)
	- [The Simple Python Class](#the-simple-python-class)
- [Chapter 28 A More Realistic Example](#chapter-28-a-more-realistic-example)
<!-- /TOC -->

# Chapter 27 Class Coding Basics

## The Simple Python Class

We could attach attributes outside the class definition. Like:
```python
class rec:
    pass

rec.name = "Bob"
rec.age = 40

x = rec()
y = rec()
```

We could do it even without an instance.

```python
x.name = 'Sue'
print(list(rec.__dict__.keys()))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))
```

In the above example, the first outputs `['age', 'name']`, the second outputs
`['name']` and the last outputs `['name']`.

We could use following:
* `x.__dict__.keys()` to check the attributes of an instance or a class.
* `x.__class__` to find out the class of an instance.
* `x.__bases__` to find out the base classes of a class.

Classes and instances are just namespace objects, with attributes created on the
fly by assignment. Those assignments usually happen within the class
statements you code, but they can occur anywhere you have a reference to one of
the objects in the tree.

We could even define methods outside the class.

# Chapter 28 A More Realistic Example
