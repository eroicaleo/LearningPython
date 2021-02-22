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

## SQL Databases

* A table has a fixed number of columns and a variable number of rows.
* Tables have a special column called the primary key.
* relational databases store data efficiently and avoid duplication.

| Users     |
| :------------- |
| id      |
| username      |
| password      |
| role_id      |

| roles     |
| :------------- |
| id      |
| name      |

## NoSQL Databases

* NoSQL is difficult for join, most don't support them.

| Users     |
| :------------- |
| id      |
| username      |
| password      |
| role      |

* Expensive to change the role name for all users.
* Easier to list all users with their roles.

## SQL or NoSQL?

* ACID: Atomicity, Consistency, Isolation, and Durability.

## Python Database Frameworks

* Flask can work with all:
    * `MySQL, Postgres, SQLite, Redis, MongoDB, CouchDB, or DynamoDB`
* Database abstraction layer packages:
    * such as `SQLAlchemy` or `MongoEngine`.
    * allow you to work at a higher level with regular Python objects instead of
      database entities such as tables, documents, or query languages.
* Easy of use with object-relational mappers (ORMs) or object-document mappers (ODMs)
* Performance: ORM and ODM will incur some overhead, but negligible.
    * We can always implement some operations directly.
* Portability, with SQL‐Alchemy, can access MySQL, Postgres, and SQLite.
* Flask integration: package specifically designed as a Flask extension should be preferred.

## Database Management with Flask-SQLAlchemy

* Install: `conda install -c conda-forge flask-sqlalchemy`
* In Flask-SQLAlchemy, a database is specified as a URL.

| DB engine | URL     |
| :------------- | :------------- |
| MySQL                 | mysql://username:password@hostname/database |
| Postgres              | postgresql://username:password@hostname/database |
| SQLite (Linux, macOS) | sqlite:////absolute/path/to/database |
| SQLite (Windows)      | sqlite:///c:/absolute/path/to/database |

* `hostname` refers to the server that hosts the database service, which
  could be `localhost` or a remote server.
* `database` indicates the name of the database to use.
* `SQLite` databases do not have a server.

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

* Check SQLAlchemy documentation for configuration options.

## Model Denition

* In the context of an ORM, a model is typically a Python class with attributes that
match the columns of a corresponding database table.
* The database instance from `Flask-SQLAlchemy` provides a base class for models as
well as a set of helper classes and functions that are used to define their structure.

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f'<User {self.username}>'
```

* `__tablename__`: class variable defines the name of the table in the database.
* The first argument given to the `db.Column` constructor is the type of the
  database column and model attribute.

* Table 5-2 Most common SQLAlchemy column types

| Type name     | Python Type     | Desc     |
| :------------- | :------------- | :------------- |
| Item One       | Item Two       | Item Two       |
| Integer       | int                | Regular integer, typically 32 bits |
| SmallInteger  | int                | Short-range integer, typically 16 bits |
| BigInteger    | int or long        | Unlimited precision integer |
| Float         | float              | Floating-point number |
| Numeric       | decimal.Decimal    | Fixed-point number |
| String        | str                | Variable-length string |
| Text          | str                | Variable-length string, optimized for large or unbounded length |
| Unicode       | unicode            | Variable-length Unicode string |
| UnicodeText   | unicode            | Variable-length Unicode string, optimized for large or unbounded length |
| Boolean       | bool               | Boolean value |
| Date          | datetime.date      | Date value |
| Time          | datetime.time      | Time value |
| DateTime      | datetime.datetime  | Date and time value |
| Interval      | datetime.timedelta | Time interval |
| Enum          | str                | List of string values |
| PickleType    | Any Python object  | Automatic Pickle serialization |
| LargeBinary   | str                | Binary blob |

* Table 5-3. Most common SQLAlchemy column options

| Option         | Desc           |
| :------------- | :------------- |
| primary_key | If set to True, the column is the table’s primary key. |
| unique      | If set to True, do not allow duplicate values for this column. |
| index       | If set to True, create an index for this column, so that queries are more | ecient.
| nullable    | If set to True, allow empty values for this column. If set to False, the | column will not allow null values.
| default     | Define a default value for the column. |

## Relationships

* Relational databases establish connections between rows in different tables through
the use of relationships.

```python
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')

class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

* The `roles.id` argument to `db.ForeignKey()`
  specifies that the column should be interpreted as having id values from rows
  in the roles table.
* The users attribute added to the model Role represents the object-oriented view of
  the relationship, as seen from the “one” side.
* Given an instance of class Role, the users attribute will return the list of users
  associated with that role (i.e., the “many” side).
* The first argument to `db.relationship()` indicates what model is on the other
  side of the relationship.
* The `backref` argument to `db.relationship()` defines the reverse direction of the
  relationship, by adding a role attribute to the User model.
* This attribute can be used on any instance of `User` instead of the `role_id` foreign key to
  access the `Role` model as an object.
* Table 5-4. Common SQLAlchemy relationship options
    * backref: Add a back reference in the other model in the relationship.
    * primaryjoin: Specify the join condition between the two models explicitly. This is necessary only for ambiguous relationships.
    * lazy: Specify how the related items are to be loaded. Possible values are select (items are loaded on demand the first time they are accessed), immediate (items are loaded when the source object is loaded), joined (items are loaded immediately, but as a join), subquery (items are loaded immediately, but as a subquery), noload (items are never loaded), and dynamic (instead of loading the items, the query that can load them is given).
    * uselist: If set to False, use a scalar instead of a list.
    * order_by: Specify the ordering used for the items in the relationship.
    * secondary: Specify the name of the association table to use in many-to-many
      relationships.
    * secondaryjoin: Specify the secondary join condition for many-to-many relationships when
      SQLAlchemy cannot determine it on its own.

## Database Operations

### Creating the Tables

```shell
flask shell
>>> from hello import db
>>> db.create_all()
>>> db.drop_all()
>>> db.create_all()
```

### Inserting Rows

```python
from hello import Role, User
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)
```

* Note that the role attribute can be used, even though it is not a real database
  column but a high-level representation of the one-to-many relationship.
* The objects exist only on the Python side so far; they have not been written
  to the database yet.

```python
>>> print(admin_role.id)
None
>>> print(mod_role.id)
None
>>> print(user_role.id)
None
```

* Changes to the database are managed through a database session:

```python
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

# Or
db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])

# Then
db.session.commit()

print(user_david.role_id)
3
print(user_david.role.id)
3
```

* The commit operation writes atomically.

### Modifying Rows

```python
>>> print(admin_role.name)
Admin
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()
>>> print(admin_role.name)
Administrator
```

### Deleting Rows

```python
db.session.delete(mod_role)
db.session.commit()
```

### Query

```python
Role.query.all()
User.query.all()
User.query.filter_by(role=user_role).all()
str(User.query.filter_by(role=user_role))
user_role = Role.query.filter_by(name='User').first()
```

* If you then start a brand-new shell session, you have to re-create the Python
objects from their database rows.

* Table 5-5. Common SQLAlchemy query filters

| Option | Description     |
| :------------- | :------------- |
| `filter()`    | Returns a new query that adds an additional filter to the original query |
| `filter_by()` | Returns a new query that adds an additional equality filter to the original query |
| `limit()`     | Returns a new query that limits the number of results of the original query to the given number |
| `offset()`    | Returns a new query that applies an offset into the list of results of the original query |
| `order_by()`  | Returns a new query that sorts the results of the original query according to the given criteria |
| `group_by()`  | Returns a new query that groups the results of the original query according to the given criteria |

* Table 5-6. Most common SQLAlchemy query executors

| Option | Description     |
| :------------- | :------------- |
| `all()`           | Returns all the results of a query as a list |
| `first()`         | Returns the first result of a query, or None if there are no results |
| `first_or_404()`  | Returns the first result of a query, or aborts the request and sends a 404 error as the response if there are no results |
| `get()`           | Returns the row that matches the given primary key, or None if no matching row is found |
| `get_or_404()`    | Returns the row that matches the given primary key or, if the key is not found, aborts the request and sends a 404 error as the response |
| `count()`         | Returns the result count of the query |
| `paginate()`      | Returns a Pagination object that contains the specified range of results |

* `lazy`

```python
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role', lazy='dynamic')
    # ...

# Then we can do:
user_role.users.order_by(User.username).all()
user_role.users.count()
```

## Database Use in View Functions

* New `index` function

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))
```

## Integration with the Python Shell

* Having to import the database instance and the models each time a shell session is
started is tedious work.
* To avoid having to constantly repeat these steps, the flask
shell command can be configured to automatically import these objects.
* Use `@app.shell_context_processor`


```python
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

* Otherwise I have to do `from hell import db, User, Role` everytime.

## Database Migrations with Flask-Migrate

* In case DB models need to change, the only way is to destroy old tales first.
* A better solution is to use a database migration framework, like version
  control.
* User `flask-migrate`

```shell
conda install -c conda-forge flask-migrate
```

* Add the following to `hello.py`

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

* Then run `flask db init`
* A folder called `migrations/` will be generated.

### Creating a Migration Script

* `upgrade()`: applies the database changes that are part of the migration.
* `downgrade()`: removes them.
* To make changes to your database schema with Flask-Migrate, the following
  procedure needs to be followed:
    1. Make the necessary changes to the model classes.
    2. Create an automatic migration script with the flask db migrate command.
    3. Review the generated script and adjust it so that it accurately represents
      the changes that were made to the models.
    4. Add the migration script to source control.
    5. Apply the migration to the database with the flask db upgrade command.

* `flask db migrate -m "initial migration`

```shell
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.env] No changes in schema detected.
```

### Upgrading the Database

* `flask db upgrade`

```shell
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
```

* For a first migration, this is effectively equivalent to calling `db.create_all()`
* In successive migrations the flask db upgrade command applies updates to the tables
without affecting their contents.

### Adding More Migrations

* The procedure to introduce a change in the database is similar to what was
 done to introduce the first migration:
    1. Make the necessary changes in the database models.
    2. Generate a migration with the flask db migrate command.
    3. Review the generated migration script and correct it if it has any inaccuracies.
    4. Apply the changes to the database with the flask db upgrade command.
* Consult the Flask-Migrate documentation to learn about other subcommands related
 to database migrations.
