

# Chapter 27 Class Coding Basics

## Simple Python Class

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

We could use following:
* `x.__dict__.keys()` to check the attributes of an instance or a class.
* `x.__class__` to find out the class of an instance.
* `x.__bases__` to find out the base classes of a class.

We could even define methods outside the class.
