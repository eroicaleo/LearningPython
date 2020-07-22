
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
