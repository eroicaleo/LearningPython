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
