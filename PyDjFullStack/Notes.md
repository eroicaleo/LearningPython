
# Section 8 Bootstrap Overview

## Bootstrap Introduction

### What is Framework?

* Framework defines the rules for you to follow
    * Tells how you can manipulate the code
* Large part: how to reference the doc for your own use cases

### Bootstrap V3 VS V4

* We won't notice any difference
* The most important thing is to reference to documentation
* getbootstrap.com -> download Bootstrap
* Use CDN, i.e. content delivery network, pretty much similar as we use google fonts
* The documentation for each component is [here](https://getbootstrap.com/docs/4.4/components/alerts/).

## Bootstrap Part One - Buttons

### Put the bootstrap in html

* go to [here](https://getbootstrap.com/docs/4.4/getting-started/download/)
* Navigate to `BootstrapCDN`
* Copy `<link ...>` and  put it into `<head></head>`
    * Just like we did with `font`


* Go over
    * button
    * container
    * Jumbotron
* Container class
    * will center the staff in it.
* Button class
    * type `button` in atom
    * Keep adding the style you like in `class="btn btn-lg btn-success"`
    * `disabled`
    * We can override the attribute by adding `.css` file to the header
      like `Part1_Buttoms.css`

## Bootstrap Part Two - Forms

* [Bootstrap Form Doc](https://getbootstrap.com/docs/4.4/components/forms/)
* Important class is `<div class="form-group">`, forms will be nicely separated
  with spacing.
    * Try take it out to see the effects.
* `form-control` class:
  * Try take it out to see the effects.
  * rounding the corner.
  * stretch the container size.
  * Highlighting differently.
* `<small></small>` make the font smaller. when you want to give form a little
  bit note.
* `<select></select>`, `<select multiple></select>`
* `<textarea></textarea>`
* `<input type="file">`
* Radio button
* `form-check`

## Bootstrap Part Three - Navbars

* [Bootstrap Navbar Doc](https://getbootstrap.com/docs/4.4/components/navbar/)
* `<nav></nav>`
* `class="navbar-dark bg-dark fixed-top"`
* Put it into `<div class="collapse navbar-collapse" id="navbarTogglerDemo01">`
* Hamburg button: needs to copy the `<script ... javascript>` to the bottom

## Bootstrap Part Four Grid System

* [examples](https://getbootstrap.com/docs/4.4/examples/grid/)
* `<div class="row">` this means we are dealing with grid system
* Grid system provides core mechanism allows websites to look good.
* Split the entire screen into 12 equal columns
* make use of the `class="row"`
* `col-ScreenSize-NumberOfColumns`, like `col-md-6`, and `col-lg-4`
    * it says when the screen is median size, defined by pixels, use 6 columns.
* `<style></style>`
* large/median/small/xs: `col-lg-6/col-md-6/col-sm-6/col-6`. Note extra small
  is changed: [here](https://getbootstrap.com/docs/4.4/migration/#grid-system)
* Further documentation: []

## Bootstrap Part Five Project

* Have to use `card` class.

# Section 9 JS Level One - Basics

## Introduction

* Chrome -> New Incog Window -> F12
* Hello world: `alert("Hello World!")`
* Comment: `//`
* Data type:
    * numbers
    * Strings
    * Boolean: ""
    * `undefined` and `null`
* `clear()` to clear console doesn't work for me, `ctrl+L` and `console.clear()`
  works.
* strings:
    * `s1+s2`
    * `s1.length`
    * escape: `\t \n \"`
    * Indexing: `"hello"[0]`
* Variables
    * `var varName = value`
    * JS uses camel case
    * `undefined` and `null`
* A few more methods:
    * `console.log()`
    * `prompt("enter something:")`

## Part Two Connecting JS

* In header: `<script src="./myscript.js"></script>`
    * This script gets called before anything

## Part Four Operators

* `"2" == 2`, true. `"2" === 2`, false.
    * `==` use type coercion.
    * `===`, `!==`

```javascript
null == undefined
true
null === undefined
false
NaN == NaN
false
```

## Part Six `while` loop

* `while`/`break`

## Part Seven `for` loop

* `For` - loops through a number of times
* `For/In` - loops through a JS object
* `For/of` - used with arrays

```javascript
for (var i = 0; i < 5; i++) {

}
```

# Section 10 JS Level Two - Basics

## Part 1 function

* Global variable, first check in the function scope, then if don't find
  then check the global scope

## Part 3 Arrays

* `var countries = ["USA", "Germany", "China"];`
* string is immutable, array is mutable.
* array can have mixed types.
* Mozilla reference [link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
* `for of` loop
* `myArr.forEach(alert)`

## Part 4 Objects

* Like the dictionary in other languages
* `{key1: "val1", key2: "val2"}`
* [link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)
* A little difference with python

```python
myCar = {"make": "Ford"}
print(myCar["make"])
```

```javascript
myCar = {make: "Ford"};
console.log(myCar["make"])
```

* To display an object: `console.dir()`
* `for in` loop to iterate through dictionary.
* `this` can be used in function inside Object
* Reference: [link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

# Section 11 Document Object Model

## Part 0 Introduction

* DOM allow JS to interact with HTML and CSS.
* Browsers construct DOM, meaning storing all the HTML tags as JS objects.
* Go to a website and in the console type: `document`. It returns the HTML text
  of page
* To see the actual object, need to use `console.dir(document)`
* DOM is enormous, most developer just need some.
* No need to memorize all of them. But need to know where to get help.

## Part 1 74 DOM Iteraction

* Important attributes:
    * `document.URL`
    * `document.body`: everything inside the body
    * `document.head`: everything in the head of the page
    * `document.links`: all the links on the page
* Methods for grabbing elements from the DOM:
    * `document.getElementByID()`: when you define an element which has id
    * `document.getElementByClassName()`: return a list of element of the class
    * `document.getElementByTagName()`
    * `document.querySelector()`: return the first object matching the CSS
      style selector
    * `document.querySelectorAll()`: returns all objects matching the CSS
      style selector
* example: `Part1_Color_Change.js`
* `myheader.style.color = 'red';`

## Part2 75 Content Interaction

* `myvariable.textContent`: This returns just the text.
* `myvariable.innerHTML`: like the inline html code
* `myvariable.getAttribute()`:
* `myvariable.setAttribute()`:

* We can call multiple `querySelector` multiple times.

```javascript
var special = document.querySelector("#special")
var specialA = special.querySelector("a")
```

## Part3 76 Events

* Most of the time, we only want to respond to certain event, such as a click
  or a hover.
* We can add event listener, JS will listen for an event and then execute a
  function when it happens.
* `myvariable.addEventListener(event, func)`

```javascript
var head = document.querySelector("h1");
had.addEventListener("click", changeColor);
```

* Many possible events:
    * `Clicks, Hovers, Double Clicks, Drags`
    * refernce [here](https://developer.mozilla.org/en-US/docs/Web/Events)

* Examples:

```javascript
head1.addEventListener("mouseover", function () {
  head1.textContent = "Mouse Currently Over";
  head1.style.color = "red";
})
```
