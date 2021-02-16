# Preface

Deviating from the path set by the framework’s developers will give you lots of headaches.

With Flask you can choose the components of your application, or even write
your own if that’s what you want.

Flask comes with a robust core. And expect all rest are provided by 3rd party.

[github source code](https://github.com/miguelgrinberg/flasky)

* Useful git command for this book

```shell
git clone https://github.com/miguelgrinberg/flasky.git
git checkout 1a
git reset --hard
git fetch --all
git fetch --tags
git reset --hard origin/master
git diff 2a 2b
```

# chapter 01 installation

Flask has three main dependencies.

1. The routing, debugging, and Web Server Gateway
Interface (WSGI) subsystems come from `Werkzeug`;
2. the template support is provided by `Jinja2`;
3. and the command-line integration comes from `Click`.

These dependencies are all authored by Armin Ronacher, the author of Flask.

```shell
conda create --name flasky python=3.8.5
conda activate flasky
conda deactivate
python --version
conda list
conda install flask
```

* Checkout a tag in Source tree, in the left panel, there is a "tag", double click the one you want

# Chapter 02 Basic Application Structure

## Initialization

```python
from flask import Flask
app = Flask(__name__)
```

## Routes and View Functions

* The Flask application instance needs to know
what code it needs to run for each URL requested, so it keeps a mapping of URLs to
Python functions.
* The association between a URL and the function that handles it is called a route.

* The most convenient way to define a route in a Flask application is through the
`app.route` decorator

```python
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

* `app.add_url_rule()` do the same thing
    * three arguments: the URL, the endpoint name, and the view function.

```python
def index():
    return '<h1>Hello World!</h1>'
app.add_url_rule('/', 'index', index)
```

* Functions like `index()` that handle application URLs are called *view functions*.

* a route that has a dynamic component
    * The dynamic components in routes are strings by default but can also be of different types.
    * Flask supports the types `string`, `int`, `float`, and `path` for routes.

```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```

## Development Web Server

```shell
export FLASK_APP=hello.py
flask run
```

* older way, but useful for unit test

```python
if __name__ == '__main__':
    app.run()
```

## Debug Mode

* `reloader`
    * watches all the source code files of your project
      and automatically restarts the server
* `debugger`
    * The web browser window transforms into an interactive stack trace that
      allows you to inspect source code
    * add `100/0.0` to `index` function.

```shell
export FLASK_APP=hello.py
export FLASK_DEBUG=1
flask run
```

* Older way

```python
app.run(debug=True)
```

## Command-Line Options

```shell
flask --help
flask run --help
flask run --host 0.0.0.0
```

## The Request-Response Cycle

### Application and Request Contexts

When Flask receives a request from a client, it needs to make a few objects available
to the view function that will handle it. A good example is the request object, which
encapsulates the HTTP request sent by the client.

Don't clutter view function with many arguments, Flask uses contexts to
temporarily make certain objects globally accessible.

Contexts enable Flask to make certain
variables globally accessible to a thread without interfering with the other
threads.

```python
from flask import request

@app.route('/')
def index():
  user_agent = request.headers.get('User-Agent')
  return '<p>Your browser is {}</p>'.format(user_agent)
```

* There are two contexts in Flask: (pg 40, table 2-1)
    * the application context:
        * `current_app`: The application instance for the active application.
        * `g`: An object that the application can use for temporary storage
          during the handling of a request. This variable is reset with each request.
    * the request context:
        * `request`: The request object, which encapsulates the contents of an
          HTTP request sent by the client.
        * `session`: The user session, a dictionary that the application can use
          to store values that are “remembered” between requests.

* Flask activates (or pushes) the application and request contexts before dispatching a
request to the application
* removes them after the request is handled.
* When the application context is pushed, the `current_app` and `g` variables
  become available to the thread.
* Likewise, when the request context is pushed, request and session
  become available as well.

```python
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
...
RuntimeError: working outside of application context
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```

### Request Dispatching

* When the application receives a request from a client, it needs to find out what view
function to invoke to service it.
* For this task, Flask looks up the URL given in the request in the
  application’s URL map, which contains a mapping of URLs to the view
  functions that handle them.

```python
(venv) $ python
>>> from hello import app
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
<Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
```

* The `/static/<filename>` route is a special route added by Flask to give
access to static files.

* The `(HEAD, OPTIONS, GET)` elements shown in the URL map are the request methods
that are handled by the routes.
* The `HEAD` and `OPTIONS` methods are managed automatically by Flask.
* In this chapter, we only have `GET`. Other method will be in Chapter 4.

### The Request Object

* Table 2-2, pg 40-41

| Attribute Name | Description    |
| :------------- | :------------- |
| form       | A dictionary with all the form fields submitted with the request.       |
| args | A dictionary with all the arguments passed in the query string of the URL. |
| values | A dictionary that combines the values in form and args. |
| cookies | A dictionary with all the cookies included in the request. |
| headers | A dictionary with all the HTTP headers included in the request. |
| files | A dictionary with all the file uploads included with the request. |
| get_data() | Returns the buffered data from the request body. |
| get_json() | Returns a Python dictionary with the parsed JSON included in the body of the request. |
| blueprint | The name of the Flask blueprint that is handling the request. Blueprints are introduced in Chapter 7. |
| endpoint | The name of the Flask endpoint that is handling the request. Flask uses the name of the view function
as the endpoint name for a route. |
| method | The HTTP request method, such as GET or POST. |
| scheme | The URL scheme (http or https). |
| is_secure | Returns True if the request came through a secure (HTTPS) connection. |
| host | The host defined in the request, including the port number if given by the client. |
| path | The path portion of the URL. |
| query_string | The query string portion of the URL, as a raw binary value. |
| full_path | The path and query string portions of the URL. |
| url | The complete URL requested by the client. |
| base_url | Same as url, but without the query string component. |
| remote_addr | The IP address of the client. |
| environ | The raw WSGI environment dictionary for the request. |

### Request Hooks

* Sometimes it is useful to execute code before or after each request is processed.
  * at the start of each request it may be necessary to create a database connection
  * or authenticate the user making the request.

* Request hooks are implemented as decorators.

```python
# Registers a function to run before each request.
before_request
# Registers a function to run only before the first request is handled. This can be a
# convenient way to add server initialization tasks.
before_first_request
# Registers a function to run after each request, but only if no unhandled exceptions occurred.
after_request
# Registers a function to run after each request, even if unhandled exceptions occurred.
teardown_request
```

* A common pattern to share data between request hook functions and view functions
is to use the `g` context global as storage. For example, a `before_request` handler can
load the logged-in user from the database and store it in `g.user`. Later, when the view
function is invoked, it can retrieve the user from there.
* More in later chapters.

### Responses

* HTTP protocol requires more than a string as a response to a request.
    * A very important part of the HTTP response is the status code
    * which Flask by default sets to 200, the code that indicates that the
      request was carried out successfully.

```python
@app.route('/')
def index():
  return '<h1>Bad Request</h1>', 400
```

* Can return `response object.` with `make_response`.

```python
from flask import make_response
@app.route('/')
def index():
  response = make_response('<h1>This document carries a cookie!</h1>')
  response.set_cookie('answer', '42')
  return response
```

* Table 2-3 pg 44

| Header One     | Header Two     |
| :------------- | :------------- |
| Item One       | Item Two       |
| status_code    | The numeric HTTP status code |
| headers        | A dictionary-like object with all the headers that will be sent with the response |
| set_cookie()   | Adds a cookie to the response |
| delete_cookie()| Removes a cookie |
| content_length | The length of the response body |
| content_type   | The media type of the response body |
| set_data()     | Sets the response body as a string or bytes value |
| get_data()     | Gets the response body |

* `redirect` response

```python
from flask import redirect
@app.route('/')
def index():
  return redirect('http://www.example.com')
```

* `abort` response

```python
from flask import abort
@app.route('/user/<id>')
def get_user(id):
  user = load_user(id)
  if not user:
    abort(404)
  return '<h1>Hello, {}</h1>'.format(user.name)
```

# Chapter 03 Templates

pg 47
