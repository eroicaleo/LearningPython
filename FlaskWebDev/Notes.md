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

* A request also triggers a change in the state of the application, and
the view function is where this change is generated.
* User register an account:
    * Business logic: view function needs to talk to the database to get the new user added.
    * presentation logic: generate a response to send back to the browser that
      includes a success or failure message.

## The Jinja2 Template Engine

The function render_template() provided by Flask integrates the Jinja2 template
engine with the application.

```html
<!-- user.html -->
<h1>Hello, {{ name }}!</h1>
```

```python
from flask import Flask, render_template

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
```

### Variables

* Jinja2 recognizes variables of any type, even complex types such as
 `lists`, `dictionaries`, and `objects`.

```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

* Variables can be modified with filters, table 3-1 page 50

| Filter name    | Desc           |
| :------------- | :------------- |
| safe         | Renders the value without applying escaping |
| capitalize   | Converts the first character of the value to uppercase and the rest to lowercase |
| lower        | Converts the value to lowercase characters |
| upper        | Converts the value to uppercase characters |
| title        | Capitalizes each word in the value |
| trim Removes | leading and trailing whitespace from the value |
| striptags    | Removes any HTML tags from the value before rendering |

* Jinja2 Documentation

### Control Structures

```html
{% if user %}
  Hello, {{ user }}!
{% else %}
  Hello, Stranger!
{% endif %}

<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

* macros, similar to function

```html
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>

{% import 'macros.html' as macros %}
<ul>
  {% for comment in comments %}
    {{ macros.render_comment(comment) }}
  {% endfor %}
</ul>
```

* template inheritance

```html
<!-- base.html -->
<html>
<head>
  {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
  {% endblock %}
  </head>
  <body>
    {% block body %}
    {% endblock %}
  </body>
</html>
```

```html
<!-- derived.html -->
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
  {{ super() }}
  <style>
  </style>
{% endblock %}
{% block body %}
  <h1>Hello, World!</h1>
{% endblock %}
```

## Bootstrap Integration with Flask-Bootstrap

```shell
conda install -c conda-forge flask-bootstrap
```

* Also check out the The Bootstrap official documentation
* See my code `ch03/user_bootstrap.html`

* Table 3-2 pg 55

| Header One     | Header Two     |
| :------------- | :------------- |
| doc            | The entire HTML document |
| html_attribs   | Attributes inside the `<html>` tag |
| html            | The contents of the `<html>` tag |
| head            | The contents of the `<head>` tag |
| title            | The contents of the `<title>` tag |
| metas            | The list of `<meta>` tags |
| styles            | CSS definitions |
| body_attribs  | Attributes inside the <body> tag |
| body            | The contents of the <body> tag |
| navbar            | User-defined navigation bar |
| content            | User-defined page content |
| scripts            | JavaScript declarations at the bottom of the document |

* IMPORTANT: has to call `super()` first if want to override any of them.

## Custom Error Pages

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

* Create separate `404.html` and `505.html` causing too much code, we can
  use inheritance.
* Create a `base.html`, see `ch03/base.html`
* Then in `404.html` and `user.html`, override `{% block page_content %}`

## Links

* `url_for()` helper function
    * `url_for('index')` -> `/`
    * `url_for('index', _external=True)` -> `http://localhost:5000/`
    * `url_for('user', name='john', _external=True)` -> `http://localhost:5000/user/john`
    * `url_for('user', name='john', page=2, version=1)` ->
      `/user/john?page=2&version=1`

## Static

* images, JavaScript files, CSS files.
* `url_for('static', filename='css/styles.css', _external=True)` ->
  `http://localhost:5000/static/css/styles.css`

```html
{% block head %}
    {{ super() }}
    <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
{% endblock %}
```

## Localization of Dates and Times with Flask-Moment

* `Flask-Moment` is an extension for Flask applications that makes the integration
  of `Moment.js` into `Jinja2` templates very easy.

```shell
conda install -c conda-forge flask-moment
```

* Then in applicaton:

```python
from flask_moment import Moment
moment = Moment(app)
```

* In the html, we need include `jQuery.js` (included by bootstrap) and `Moment.js`.

```html
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```

* In `index.html`, add the following:
    * The `format('LLL')` function renders the date and time according to the
      time zone and locale settings in the client computer.
    * The `fromNow()` render style shown in the second line renders a relative timestamp
      and automatically refreshes it as time passes.
    * Flask-Moment implements the `format(), fromNow(), fromTime(), calendar(),
      valueOf(), and unix()` methods from `Moment.js`.

```html
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```

* Also check Moment.js documentation.
* Also can support foreign languages: the [2 letter code](https://en.wikipedia.org/wiki/ISO_3166-1)

```html
{% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    {{ moment.locale('fr') }}
{% endblock %}
```

# Chapter 4 Web Forms

Pg 65

* Install

```shell
conda install -c anaconda flask-wtf
```

## Configuration

* `flask-wtf` doesn't require to be initialized.

```python
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

* `app.config` dictionary is a general-purpose place to store configuration
  variables used by Flask.

## Form Classes

* When using `Flask-WTF`, each web form is represented in the server by a class that
  inherits from the class `FlaskForm`.
* The class defines the list of fields in the form, each represented by an object.
* Each field object can have one or more validators attached.

```python
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

* In the example:
    * the `NameForm` form has a text field called name
    * and a `submit` button called submit.
    * The DataRequired() validator ensures that the field is not submitted empty.

* Table 4-1 pg 67

| Field type | desc     |
| :------------- | :------------- |
| Item One       | Item Two       |
| BooleanField      | Checkbox with True and False values |
| DateField         | Text field that accepts a datetime.date value in a given format |
| DateTimeField     | Text field that accepts a datetime.datetime value in a given format |
| DecimalField      | Text field that accepts a decimal.Decimal value |
| FileField         | File upload field |
| HiddenField       | Hidden text field |
| MultipleFileField | Multiple file upload field |
| FieldList         | List of fields of a given type |
| FloatField          | Text field that accepts a floating-point value |
| FormField           | Form embedded as a field in a container form |
| IntegerField        | Text field that accepts an integer value |
| PasswordField       | Password text field |
| RadioField          | List of radio buttons |
| SelectField         | Drop-down list of choices |
| SelectMultipleField | Drop-down list of choices with multiple selection |
| SubmitField         | Form submission button |
| StringField         | Text field |
| TextAreaField       | Multiple-line text field |

* Table 4-2 WTForms validators pg 68

## HTML Rendering of Forms

* Different ways:

```html
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.name.label }} {{ form.name() }}
  {{ form.submit() }}
</form>

<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.name.label }} {{ form.name(id='my-text-field') }}
  {{ form.submit() }}
</form>

{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

* The imported `bootstrap/wtf.html` file defines helper functions that render Flask-WTF forms using Boot‐
strap.
* The `wtf.quick_form()` function takes a Flask-WTF form object and renders it
using default Bootstrap styles.

## Form Handling in View Functions

* I have the following error:
  `jinja2.exceptions.TemplateNotFound: bootstrap/wtf.html`
  Needs to add the following:

```python
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
```

* We added `GET` and `POST` requests.
* The `validate_on_submit()` method of the form returns True when the form was
  submitted and the data was accepted by all the field validators.
* If the user submits the form with an empty name, the `DataRequired()` validator
  catches the error.

## Redirects and User Sessions

* When `POST`, refresh page, browser will asks for confirmation from the user.
  This happens because browsers repeat the last request they sent when they are asked to
  refresh a page.
* it is considered good practice for web applications to never leave a POST request as the last
  request sent by the browser.
* This is achieved by responding to `POST` requests with a redirect instead of a normal
response.
* Applications can “remember” things from one request to the next by storing them in
the `user session`.

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```

## Message Flashing

* Sometimes it is useful to give the user a status update after a request is completed.
    * message, warning, error.
    * Eg, submit wrong info to a website, server response with a warning message.
* Use `flash`

```python
app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if (old_name is not None) and (old_name != form.name.data):
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```

* Also need to update the `base.html`

```html
{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}

    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

# CHAPTER 5 Databases

Pg 79
