
# Chaptre 2

## 2.1 Assertion

* `assert` is for internal debugging, not for catching
  runtime errors.
* We can have a second expression to print out some messages.
* Caveat 1: Don't use `assert` for data validation, since it can be disabled
    * Do the data validation just uses the regular `if-else`
* Caveat 2: Asserts never fails
    * like these: `assert (1==2, 'This should fail')`
    * But now seems the python3 will just give an warning
    * To avoid such kind of problem, needs to use unit test to make
      it fail

## 2.2 comma

* If we define a list in one line. It's hard to track the changes
  through the version control system. So if we list each item in one line,
  it's easier to track the changes.
* But if we miss a comma, we will run into string literal concatenation problem.
* In python, you are allowed to a comma after every item in a list, dict, set. 

## 2.3 `with` statement

* `with` statement can get rid of resource handling logic.
* context manager: a protocol your objects need follow
    * add `__enter__` and `__exit__` methods
    * The signature of `__exit__` must be `def __exit__(self, exc_type, exc_val, exc_tb):`
* it can also be implemented as `contextmanager` inside `contextlib`
* The resource doesn't have to be file or lock
    * it can be indentation level, when enter increase the indentation, when exist, reduce the indentation.
    * it can be timer, when enter start the timer, when exist, stop the timer
* Key Takeaways:
    * simplifies exception handling.
    * resource acquisition and release.

## 2.4 Underscore, Dunders and More

* `_var`: single leading underscore.
    * convention only: the variable or function is internal use only.
    * But if such variable or function exists in a module, and you use
      wildcard to import, then it will ignore such variable and function.
    * Regular import is not affected, and wildcard import is not recommended.

* `var_`: single trailing underscore.
    * This is to avoid naming conflict with keyword

* `__var`: double leading underscore.
    * Python will rename this variable to `_Classname__var`, called name mangling
    * Inside the class, the programmer can just use the `__var`, it's transparent to programmer.
    * And the name mangling is not tied to class attribute, it can happen to any name
      start with `__` in class context.

* `__var__`
    * Name mangling doesn't impact these variables
    * We should avoid use the dunder variable for your own attribute.
      so won't conflict with future Python language

* `_`
    * means ignore
    * Can also use as the last variable in terminal
    * Can also use for constructing objects online 

## 2.5 

* old style
    * We can pass a mapping to `%` operator, easier to maintain and modify, no need to match the number
    * requires more typing.
* new style, python3 and 2.7, [link](https://docs.python.org/3/library/string.html#string-formatting)
    * Use `''.format(arg1=arg1, arg2=arg2)`, the order can change
* Literal String Interpolation, in python3.6, [link](https://www.python.org/dev/peps/pep-0498/)
    * `str_ = f'Hey {name}, there is a {errno:#x} error!'`
* Template Strings:
    * not core language feature
    * doesn't allow format specifier
    * Use it when you are handling format string form user input, so no security issue
* Dan's Rule of Thumb
    * User supply format string: `Template` to reduce security issue
    * 3.6+, Literal String Interpolation
    * New style

## 2.6

* `import this` to get the "Then Zen of Python".

# Chapter 3 Functions

## 3.1 Python's Functions Are First-Class

* Functions are objects
    * You can assign the function to a different variables
    * Delete the original name
    * Find the function name: `func.__name__`
* Functions can be store in data structure
* Functions can be passed to other functions
    * powerful feature: abstract away, pass around behaviour
    * functions accept other functions are called higher-order functions
    * classical example: `map`
* Functions can be nested
    * you cannot directly access the inner function: `whisper`
    * Nor you can access like this `speak.whisper`
    * You have to reture function,
    * which means python function only can accept behaviour but can also 
      return behaviour, which is cool
* Functions can capture local state
    * The inner function can still access the variables defined in parent functions
    * A (lexical) closure remembers the values from its enclosing lexical scope
      even when the program flow is no longer in that scope.
    * Functions not only returns behaviour, but also pre-configure those behaviours.
    * `make_adder` serves as the factory to create and configure "add" functions.
* Objects can Behave like functions
    * Objects can be made callable
    * Define the `__call__` method
    * use `callable` to see if an object is callable or not

## 3.2 Lambdas Are Single-Expression Functions

* Didn't have to bind function objects to a name before using it.
* Lambda functions are restricted to a single expression, cannot use statements, nor annotations, nor even `return`
* Lambda also works with lexicon closure.
* Caveat:
    * Sometimes it's much cleaner to go with a list comprehension or generator expression
    * If doing something complex with Lambda expression, then should define standalone functions.

## 3.3 The power of decorators 

* Decorators can modify the behaviour of a callable (functions, methods and classes)
* Use case for decorators: logging/enforcing access control and anthentication/ instrumentation and timing functions / rate-limiting / caching and more.
* Understanding decorators is a milestone for any serious Python programmer.
* What is a decorators or wrappers: allows you to execute code before and after the wrapped functions.
    * You don't need to change wrapper function itself
    * Function behaviour only changes when it is decorated
* We can put `@null_decorator` in front of a function, it's a syntax short cut.
    * We can put multiple decorators in front of the function
    * The order is from bottom to top, like stacking
* To decorate functions that take argument, `*args` and `**kwargs` comes in handy

```python
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

* To copy over lost metadata, e.g. `__name__`, `__doc__` to the decorated closure,
  Use `functools.wraps`

## 3.4 FUNC with `*args` and `**kwargs`

* `args` collects all positional argument
* `kwargs` collects all keyword argument
* They can be used to forwarding argument, modify them before passing to another function
    * Good for subclassing and writing wrapper function
    * Like the `AlwaysBlueCar` class in the example, the parent constructor
      might change, but the color the for `AlwaysBlueCar` is still blue.
    * Scenario potentially more helpful: writing wrapper functions. There you typically 
      also want to accept arbitrary arguments to be passed.

## 3.5 Function Argument Unpacking

* really cool feature: unpacking argument from sequence and dict with `*` and `**` .
* putting a `*` before an iterable in a function call will unpack it and pass its
  elements as separate positional arguments to the called function.
* This technique works for any iterable, including generator expressions.
* `**` will pass key argument to the function, so if there is a key not present in
  the function's argument list, it will give an error.
* We can also use `*` to unpack dictionary, then it will pass the key to the function.

## 3.6 Nothing to Return Here

* If we don't add any `return` statements, then
  the function will return `None` or you can just do `return`
* When is good to use this?
    * For function like `print`
* This is a core Python feature but your code might communicate
its intent more clearly with an explicit return None statement.

# Chapter 4 Classes and OOP

## 4.1 Object Comparisons: “is” vs “==”

* `==` compares by checking for equality
* `is` compares identity
* When in doubt, think about the twin cats

## 4.2 String Conversion (Every Class Needs a `__repr__`)

* For a user defined class, if we print it, it just shows the memory address and very
  little info.
* With `__str__` method, `str` and `'{}'.format()` will call it.
* Inspecting an object in interative session will call `__repr__`
* Convert a container like str and dict will call `__repr__`
* Manually call with `str` and `repr`
* Difference, check out the `datetime.date` object:
    * `str` returns something readable
    * `repr` returns something not ambiguious, for debugging purpose
* My rule of thumb is to make my __repr__ strings unambiguous
  and helpful for developers, but I don’t expect them to be able to restore
  an object’s complete state.
* if `__str__`  is missing, it will always call `__repr__`

## 4.3 Defining your own exception classes

* Defining your own error types can be of great value:
    * Make potential error cases stand out clearly
    * functions and modules more maintainable
* Generally, you want to derive your custom exceptions from the root `Exception`
  or `ValueError` or `TypeError`
* We can use the `try ... except ... as ...`
* easier to ask for forgiveness than permission (EAFP)

## 4.4 Cloning Objects for fun and profit

* Assignment only binds name to an object.
* Copy python built-in collections, using `list, dict, set` factory functions
    * `new_list = list(original_list)`
    * `new_dict = dict(original_dict)`
    * `new_set  = set(original_set)`
* This method won't work for custom object
* Shallow copy:
    * Create a collection, then child objects are reference
* Deep copy:
    * Create a collection, recursively copy child objects
* Use `copy.deepcopy` for deep copy
* Use `copy.copy` to create shallow copy
    * But for built-in collections, using factory functions is more pythonic and more simple
* Arbitrary object:
    * `Point` object only has built-in type, so shallow and deep are the same
    * `Rectangle` object needs to use `copy.deepcopy`
* Further reading: python `copy` module [here](https://docs.python.org/3/library/copy.html)

## 4.5 Abstract Base Class Keeps Inheritance in Check

* ABC ensure the derived classes implement particular methods from the base class.
* Scenario:
    * `BaseService`
    * Several concrete implementations: `MockService`, `RealService`
* Target
    * instantiating the base class is impossible
    * forgetting to implement interface raises and error as early as possible
* Downsides of 1st implementation
    * Not satisfy the first
    * second is not early enough
* With `abc` module and `ABCMeta` and `abstractmethod`
    * The above 2 are all satisfied
    * More robust / maitainable / communicative
* Further reading: python `abc` module [here](https://docs.python.org/3/library/abc.html)

## 4.6 What Namedtuples Are Good For

* Namedtuples can be a great alternative to defining a class manually
* plain tuple data can only be accessed through integer indexing, impact readability.
* `namedtuple` are immutable containers
    * object can be accessed through `identifer`
* Initialization, first parameter needs to be type.
    * Value can be accessed through name: `my_car.color`
    * Value can be accessed through index: `my_car.color`
* Memory is more efficient than `class`
* We can add method to `namedtuple` by subclassing
* If we want to add new field, the trick is to use `_fields` in `namedtuple`:
    * `ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))`
* Build-in helper methods
    * `_asdict`: `my_car._asdict()`
    * `_replace`: `my_car._replace(color="blue")`
    * `_make`
* When to use?
    * clean up your code / more readable
    * Dictionary with fixed format -> `namedtuple`
    * Unstructured `tuple` and `dict` -> `namedtuple` self-documenting
    * Don't use it if doesn't make your code cleaner
