<!-- TOC depth:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Chapter 27 Class Coding Basics](#chapter-27-class-coding-basics)
	- [The Simple Python Class](#the-simple-python-class)
- [Chapter 28 A More Realistic Example](#chapter-28-a-more-realistic-example)
	- [Step 1: Making Instances](#step-1-making-instances)
	- [Step 2: Adding Behavior Methods](#step-2-adding-behavior-methods)
	- [Step 3: Operator Overloading](#step-3-operator-overloading)
	- [Step 4: Customizing Behavior by Subclassing](#step-4-customizing-behavior-by-subclassing)
	- [Step 5: Customizing Constructors](#step-5-customizing-constructors)
	- [Step 6: Using Introspection Tools](#step-6-using-introspection-tools)
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

## Step 1: Making Instances

`bob`'s name is not `sue`'s name. Technically, `bob` and `sue` are both namespace
objects like all
class instances, they each have their own independent copy of the state information
created by the class. Because each instance of a class has its own set of `self` attributes,
classes are a natural for recording information for multiple objects this way; just like
built-in types such as lists and dictionaries, classes serve as a sort of object factory.

To do unit test, we would do:

```python
if __name__ == '__main__':
	# blablabla
```

## Step 2: Adding Behavior Methods

The preceding code works as planned, but if you show it to a veteran software developer
he or she will probably tell you that its general approach is not a great idea in practice.
Hardcoding operations like these outside of the class can lead to maintenance problems
in the future.

We want to code operations on objects in a class's methods. *factoring* code to
remove *redundancy* and thus optimizing maintainability.

## Step 3: Operator Overloading

**Providing Print Display**

`__str__` is preferred by `print` and `str`. `__repr__` is used as fallback.

the `__repr__` method is often used to provide an as-code low-level display of an
object when present, and `__str__` is reserved for more user-friendly
informational displays like ours here. Sometimes classes provide both a
`__str__` for user-friendly displays and a `__repr__` with extra details for
developers to view. Because printing runs `__str__` and the interactive prompt
echoes results with `__repr__`, this can provide both target audiences with an
appropriate display.

## Step 4: Customizing Behavior by Subclassing

We can call the method in the superclass like:

```python
class Manager(Person):
    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent+bonus)
```

Note that `instance.method(args...)` is same as `class.method(instance, args...)`

Note: Python's `super` is like a box of chocolates - you never know what you're
going to get!

## Step 5: Customizing Constructors

It's similar as customizing other member functions:

```python
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
```

**Other ways to combine classes**

```python
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=0.1):
        self.person.give_raise(percent+bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)
```

The more important point here is that this Manager alternative is representative
of a general coding pattern usually known as *delegation*—a composite-based
structure that manages a wrapped object and propagates method calls to it.

Note that in python 3.X, we have to define `__repr__`. In 3.X’s new-style classes, built-in
operations like these do not route their implicit attribute fetches through generic attribute
managers: neither `__getattr__` (run for undefined attributes) nor its cousin
`__getattribute__` (run for all attributes) is invoked. This is why we have to redefine
`__repr__` redundantly in the alternative Manager, in order to ensure that printing is
routed to the embedded Person object in 3.X.

## Step 6: Using Introspection Tools
