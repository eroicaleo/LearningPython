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
	- [Step 7: Storing Objects in a Database](#step-7-storing-objects-in-a-database)
- [Chapter 29 Class Coding Details](#chapter-29-class-coding-details)
	- [The Class Statement](#the-class-statement)
	- [Methods](#methods)
	- [Inheritance](#inheritance)
	- [Namespaces: The conclusion](#namespaces-the-conclusion)
	- [Namespace Dictionaries: Review](#namespace-dictionaries-review)
	- [Namespace links: A Tree Climber](#namespace-links-a-tree-climber)
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

Two problems with the above `__repr__` method.
1. `Manager` dose not print 'manager' title
2. If we have new attribute in the future, we have to modify the `__repr__` again.

Introspection tool:
* `__class__`: a link from instance to it's class
    * class has a attribute: `__name__`
* `__bases__`: provides access to its superclass
* `__dict__`: gives the attribute

To get the attribute from a class instance, we can do `getattr(instance, attribute_name)`.
Note that the `attribute_name` is a string.

**Instance Versus Class Attibutes**

Note that if you do `__dict__` on a instance, you only get the instance attributes.
If we want to show the class attribute, we need to first use `__class__`. If we
really want all the attributes, we could use `dir` function.

**Name Considerations in Tool Classes**

To prevent subclass accidentally define method with the same name, author usually
put an `_` in front of the method which they don't want others to use externally.

**Our Class's Final Form**

Now we make the `Person` class a subclass of `AttrDisplay`, and remove the `__repr__`
method defined in `Person`. It will give the correct title for `Manager`, like:
```python
class Person(AttrDisplay):
	  # blablabla

[Person: job=None, name=Bob Smith, pay=0]
[Person: job=dev, name=Sue Jones, pay=121000]
[Manager: job=mgr, name=Tom Jones, pay=720000]
```

## Step 7: Storing Objects in a Database

We can use three modules to make instance objects permanent: `pickle`, `dbm` and `shelve`.

`pickle`

Converts a python object in memory to a string of bytes.

`shelve`

Provides an extra layer of structure that allows you to store pickled objects by
key.

**Storing Objects on a Shelve Database**

Here is an example:

```python
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
```

**Exploring Shelve Interactively**

Here are some examples. Notice we don't have to `import Person` or `Manager` again.

```python
print(open('persondb.dir').read())
print(open('persondb.dat', 'rb').read())

db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))

bob = db['Bob Smith']
print(bob)

print(bob.last_name())

for key in db:
    print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])

```

* Cons: The classes and their module files must be importable when an instance
	is later loaded. More formally, pickleable classes must be coded at the top
	level of a module file accessible from a directory listed on the `sys.path`
	module search path.
* Pros: that changes in a class’s source code file are automatically picked up
	when instances of the class are loaded again.

# Chapter 29 Class Coding Details

## The Class Statement

The `class` statement is not a declaration, but is an object builder and implicit
assignment - when run, it generates a class object and stores a reference to it in
the name used in the header.

Within the `class` statement, any assignment generate class attributes.

Assignments of simple non-function objects to class attributes produce
data attributes, shared by all instances.

Assignments to instance attributes create or change the names in the instance, rather
than in the shared class. More generally, inheritance searches occur only on attribute
references, not on assignment: assigning to an object’s attribute always changes that
object, and no other. For example, `y.spam` is looked up in the class by inheritance, but
the assignment to `x.spam` attaches a name to x itself.

Consider the following code:

```python
class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)

x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()
 # The outut is like:
 # 1 spam
 # 2 spam
```

By using these techniques to store attributes in different objects, we determine their
scope of visibility. When attached to classes, names are shared; in instances, names
record per-instance data, not shared behavior or data. Although inheritance searches
look up names for us, we can always get to an attribute anywhere in a tree by accessing
the desired object directly.

## Methods

In other words, Python automatically maps instance method calls to a class’s method
functions as follows. Method calls made through an instance, like this:

```python
instance.method(args...)
```
are automatically translated to class method function calls of this form:

```python
class.method(instance, args...)
```

## Inheritance

**Class Interface Techniques**

* Super: Defines a method function and a delegate that expects an action in a subclass.
* Inheritor: Doesn’t provide any new names, so it gets everything defined in Super.
* Replacer: Overrides Super’s method with a version of its own.
* Extender: Customizes Super’s method by overriding and calling back to run the default.
* Provider: Implements the action method expected by Super’s delegate method.

The most crucial technique is `Provider`. Python first finds `delegate` method in
`Super` class. Then in the `delegate` method, `self.action` invokes a new, independent
inheritance search, the `action` located in the `Provider` subclass.

```python
class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

		def action(self):
        assert False, 'action must be defined!'

class Provider(Super):
    def action(self):
        print('in Provider.action')

x = Provider()
x.delegate()

X = Super()
X.delegate() # AssertionError: action must be defined!
```

With `function decorator` and `metaclass`, we can make a class not instantiable
if the any abstract methods are not defined.

## Namespaces: The conclusion

* Unqualified names (e.g. `X`) deal with scopes
* Qualified attribute names (e.g. `object.X`) use object namespaces.

Attribute Names: Object Namespaces.

*Assignment (`object.X = Value`)*: Creates or alters the attribute name `X` in the
namespace of the `object` being qualified,
and none other. Inheritance-tree climbing happens only on attribute reference,
not on attribute assignment.

*Reference (`object.X`)*: For class-based objects, searches for the attribute
name `X` in `object`, then in all
accessible classes above it, using the inheritance search procedure. For nonclass
objects such as modules, fetches `X` from `object` directly.

We can fetch the class attributes, e.g. `C.X`, but we can never fetch local variables
in functions or methods from outside their `def` statements.

Scopes are always determined by the position of assignments in your source code,
and are never influenced by what imports what or who imports whom.

**Nested Classes: The LEBT Scopes Rule Revisited**

The `LEBT` rule never search enclosing `class`, just `def`s, modules and built-ins.
It's `LEBT` not `CLEBT`. In the following example, the first `print` in `method1`
will print out 2, not 3. If we want to print 3, we have to use `self.X`.

```python
def nester():
    X = 2
    print(X)

    class C:
        X = 3
        print(X)

        def method1(self):
            print(X)
            print(self.X)
```

## Namespace Dictionaries: Review

Because attributes are actually dictionary keys inside Python, there are really
two ways to fetch and assign their values—by qualification, or by key indexing:

```python
print(X.data1, X.__dict__['data1'])
```

This equivalence applies only to attributes actually attached to the instance, though.
Because attribute fetch qualification also performs an inheritance search, it can access
inherited attributes that namespace dictionary indexing cannot. The inherited attribute
`X.hello`, for instance, cannot be accessed by `X.__dict__['hello']`.

## Namespace links: A Tree Climber

We use `__bases__` to get the base classes for a class.
```python
class A: pass
A.__bases__
```

# Chapter 30 Operator Overloading

## The basics

* Table 30.1 summarize the operators.
* All overloading methods start and end with '__'
* The mapping from special methods to expressions are predefined by python
  language

## Indexing and slicing

* `__getitem__` also works for slicing
* `__index__` is not indexing

## Index iteration

* In the absence of a specific iteration method, the `for` statement works by repeatedly
  indexing a sequence from 0 to higher index.
* Then __getitem__ is one way to overload iteration
* Then `in`, list comprehension, `map`/`filter`, list and tuple assignment all work in this case.

## Iterable objects

* Iteration context will first try __iter__, and then __getitem__
* iteration context pass an Iterable object to `iter()` which invokes the `__iter__` and expects to
  get an iterator object. If this succeed, the the context continues to call the `__next__` method,
  until `StopIteration` is raised.
* The `Square` example's `__iter__` just return itself because `__next__` is part of the class. But
  in more complex context, the iterator object maybe a separate class and object to support multiple
  active iterations.
* The design of it is to return itself, so it's one shot iteration. Once iterate over, it's empty.

### Multiple iterators on one object

* generator functions and expressions, as well as built-ins like map and zip are single iterator objects.
* The `range` and `list` support multiple iterations.
* To support multiple iteration, `__iter__` just need to define a new stateful object for the iterator, see `skipper.py`
* Another approach, combine `__iter__` with generator, i.e. in the `__iter__` return a generator object.
  This is because a generator is an iterator object, if you do `iter(G) == G`, the result is true
    * This approach also supports multiple active iterations, and code is more concise.
    * However, the regular version is more explicit and easy to understand.

## Membership: `__contains__`, `__getitem__`, `__iter__`

* priority: `__contains__` > `__getitem__` > `__iter__`

## Attribute Access:

* `__getattr__`: it's called when python cannot find the attribute name in the inheritance tree.
* `__setattr__`: if this function is defined or inherited, `self.attr = value` becomes `self.__setattr__('attr', value)`
    * Need to use like this: `self.__dict__['name'] = x`, otherwise will cause infinite loop
    * Another method is to route the assignment to a higher superclass: `object.__setattr__(self, attr, value + 10)`
    * We use this method to mimic the private attribute that cannot be changed outside a class. A better way will be
      presented in chapter 38.

## String represntation: `__repr__` and `__str__`

* `__str__` is first tried for `print` nad `str`. User friendly display.
* `__repr__` is used in other cases: interactive echos, `repr`, and etc. Detailed display for developers.
* They both must return strings
* `__str__` only applys when print top level object, if one object is nested in another larger object, need to use `__repr__`
* They are 2nd most commonly used methods, just behind `__init__`

## `__radd__` and `__iadd__`

* If truely symmetric operations, 3 ways to do `__radd__`
    * call `self.__add__` inside `__radd__`
    * switch the operands order inside `self.__radd__`
    * do: `__radd__ = __add__`
* inplace addition `+=`: `__iadd__`
* right side is advanced and fairly uncommon

## Call operations

* `__call__` becomes useful with API that expects functions, it allows us to code object
  that conforms an expected function call interface, and also retain state information.
* similar implementation:
    * closure
    * lambda functions
    * bound functions

## Boolean tests

* python prefer `__bool__` over `__len__` if both defined.
* if none of them defined, then boolean test is always true.

## Object deletion: `__del__`

* Destructors are not as commonly used as in other languages.
* Better to code termination code in some explicit function like `shutdown`

# Chapter 31 Designing with Classes

## Python and OOP

* Inheritance
* Polymorphism: attributes are resolved @ runtime, so objects with same interface are interchangable.
    * There can be only one definition of a method name in Python.
    * You should write the python code to expect an object interface, not a specific data type.
* Encapsulation

## OOP and Inheritance: is-a relation

## OOP and Composition: has-a relation

* Composition refers a collection of embedded objects.
* The processing code only cares that writers have a `write` method and a method named `convert` is defined.
* Inheritance and composition are often complementary and sometimes alternative techniques.

## OOP and delegation: "Wrapper" proxy objects

* sample code: `trace.py`
* delegation is a special form of composition, with a single embedded object managed by a wrapper (proxy)
  that retains most or all of the embedded object's interface.
* delegation is often implementated with the `__getattr__`.
* A wrapper class can use `__getattr__` to route arbitrary accesses to a wrapped object. 
* The net effect is to augment the interface of the wrapped object.
* See also ch.32 and ch39, function decorators.

## Pseudoprivate Class Attributes

* Python programmers code internal names with a single underscore `_X` to let you know a name should not
  be changed.
* `__X` will be expanded to `_spam__X`, assume the class is called `spam`.
* If care about privacy, should review `__getattr__` and `__setattr__` in last chapter or `Private` class
  decorator.

## Methods are objects: Bound or Unbound

* `class.function_attribute` returns an Unbound method object. Must provide instance as the explicitly
  as the 1st argument.
* `instance.function_attribute` is bound method object
* python supports 3 kinds of class level methods: instance, static and class
* Python 3 allows to call a method without an instance, as long as the method doesn't expect one.
  This doesn't work for python 2.x
    * Because of this, the `staticmethod` built-in function and decorator in not needed in 3.X if 
      a method doesn't have `self`
* bound methods have introspection of their own
    * `__self__` points to instance
    * `__func__` points to the function
* other callables:
    * functions: `lambda` and `def`
    * instance that inherites a `__call__`
    * bound method

## Classes are objects: generic object factories

* A factory might allow code to be insulated from the details of dynamically configured object construction.

## Multiple Inheritance: "Mix-in" classes

* Attribute search order: from left to right in the headline
* Resolve name conflict, (not very common)
    * `self.method()` choose the lowest and lefmost
    * `superclass.method()` Overrides the default
* `id` to find the address of an instance.
* See `testmixin.py` for the example
* `__dict__` to get instance attributes, `dir` to get all attributes.
* a little trick: s1 = '%%s'; res = 'lala'; s2 = s1 % res
* in `listtree.py`, the class object is used as key to the `__visited` directory. Since they are hashable objects.
* `collector` module combines them in a single namespace.

# Chapter 32 Advanced class topics

## Extending built-in types

### Extending by embedding

* `setwrapper.py`

### Extending by subclassing

* `setsubclass.py`, `typesubclass.py`

## The "New Style" Class Model

* Python 3.X, all classes are new style whether they inherited from `object`
* Python 2.X, classes must explicitly inherite from `object` or other built-in class to be considered as new style.

## New Style class changes

* Classes and types merged. `type(I)` returns a class and is normally same as `I.__class__`.
  classes are instances of the `type` class.
* All classes inherited from `object`
* Attribute search order: MRO and diamonds
* Inheritance algorithm is different.
* New class tools: slots, properties, descriptors, super and `__getattribute__`

### Attribute fetch for built-ins skip instance 

* In 2.X, for built-in operations, like `X[0]`, i.e. `__getitem__`, if the class of `X` doesn't define
  `__getitem__`, it will be routed to the instance's `__getattr__`. Why instance? Because a instance
  can define it's own `__getattr__` after its instantiation.
* In 3.X, `X.__add__` and `X.normal` will be routed to `X.__getattr__`, but `X + 1` won't
  and `type(X).__add__(X, 1)` also won't and will raise exception.

### Type Model Changes

* type object generate classes as its instances, classes generate instances of themselves.
* The type of a class instance is the class, the type of a user-defined class is the same as
  the type of a built-in object type.
    * `print(type(C), C.__class__, int.__class__, type(str))` are the same
* Generally, type checking is the wrong thing to do in Python, we code to the object interfaces,
  not object types. `isinstance` should be used for class type quering which is rare.

### All classes derive from `object`

* The following results are all `True`
    * `isinstance(type, object)`: All classes derive from `object`. 
    * `isinstance(object, type)`: `type` makes classes.

### Diamond inheritance change

* 2.X, DFLR (depth first left to right).
* 3.X, MRO (method resolution order), not just for method but also for all attributes
  looks in any super classes to the right of the one just searched before ascending to
  the common superclass at the top.
* Can use explicit conflict resolution: your code won't vary per Python version (portability technique).
* `object` class defines `__str__`, `__repr__`, so if we don't have MRO, multiple inheritence
  will probably go to this method first.
