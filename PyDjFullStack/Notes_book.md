
# Ch01 Structures

* Elements are usually
made up of two tags: an opening tag and a closing tag. (The closing tag
has an extra forward slash in it.) Each HTML element tells the browser
something about the information that sits between its opening and
closing tags.

* Tags act like containers. They tell you
something about the information that lies
between their opening and closing tags.

* The terms "tag" and "element" are often used interchangeably.

* Strictly speaking, however, an element comprises the opening

* tag and the closing tag and any content that lies between them.

* Attributes appear on the opening tag of the element and are
made up of two parts: a name and a value,
separated by an equals sign.
    * Attributes name should be in lower case
    * Attributes value should be in double quotes.

```html
<p lang="en-us">Paragraph in English</p>
```

# Ch02 Text

Pg 47

* `<h1>` through `<h6>`
* `<p>`
* `<i>`, `<b>`
* `<sub>, <sup>`
* whitespace will be collapsing.
* line break tag: `<br />`
* horizontal breaker: `<hr />`

## Semantic Markup

* `<strong>, <em>`
* `<blockquote> <q>`
* `<abbr>`
* `<cite> <dfn>`
* `<ins> <del> <s>`

# Ch03 List

* Ordered List: use bullets
    * `<ol>, <li>`
* Unodered List: use numbers
    * `<ul>, <li>`
* Definition list: define terminology
    * `<dl>`
    * `<dt>`: the term to be defined
    * `<dd>`: the real definition
* List can be nested

# Ch04 Links

pg 81

* Created with `<a></a>`

```html
<a href="http://www.imdb.com">IMDB</a>
```

* Linking to Other Sites
    * `<a>`
* Linking to other pages on the same site, no need to specify
  absolute URL.
    * `<a href="ch02.html">Chapter 02</a>`
* Relative Link Type
    * Same Folder: `<a href="reviews.html">Reviews</a>`
    * Child Folder: `<a href="music/listings.html">Listings</a>`
    * Grandchildren folder: `<a href="movies/dvd/reviews.html">Reviews</a>`
    * GrandParent Folder: `<a href="../../index.html">Home</a>`
* Email links
    * `<a href="mailto:jon@example.org">Email Jon</a>`
* Open in new window: Use `target="_blank"`
* Link to a specific part in the same page.
    * `<h1 id="top">Film Making Terms</h1>`
    * `<a href="#top">Top</a>`

# Ch05 Images

Pg 101

* `<img>` element
    * `src`: the location of the image
    * `alt`: used by screen reader software
    * `title`: mouse hover on to the image
    * `height`/`width`
    * `align="left"`, `align="right"`
    * `align="top"`, `align="middle"`, `align="bottom"`
* 3 rules:
    * Save image in the right format
    * Save image in the right size
    * Save image use correct resolution
* `<figure>` and `<figurecaption>`

# Ch 06 Tables

Pg 133

* `<table>`
    * `<tr>`: table row
    * `<td>`: table data
    * `<th>`: table heading, the `scope` attribute indicates
      `row` or `col`
* Spanning columns/rows
    * Use attr `colspan="2"`
    * Use attr `rowspan="2"`
* Long tables: `thead`, `tbody`, `tfoot`
    * Use css can change its appearance
* Width and spacing, old code, **replaced by CSS**
    * `width`, can add in the `<table>` or the first row, in pixels.
    * `cellpadding` attribute to add space inside each cell of
      the table, in pixels.
    * `cellspacing`: to create space between each cell of the table,
      in pixels.
* Border and background:
    * `border=2`, can be used in `table` and `td`, in pixels.
    * `bgcolor=#cccccc`, can be used for entire table or cell,
      usually hex code.

# Ch 07 Forms

Pg 151

* Different types of form
    * Adding Text:
        * Text input
        * Password
        * Text area
    * Make Choices:
        *  Radio button
        * checkbox
        * drop-down box
    * Submit forms:
        * submit buttons
        * image button
    * Uploading files
        * File upload
* `<form>`
    * attribute: `action`, is the URL for the page on the
      server that will receive the
      information
    * attribute: `method`, can be `get` or `post`
        * `get` good for short forms and retrieving data
        * `post` upload file/very long
    * attribute: `id`

* Text input:
    * `size`: should not be used for new form.
      no. of characters to display.
    * `maxlength`: limit the characters
    * `name`: The value of this attribute identifies the form
      control and is sent along with the information
      they enter to the server.

```HTML
<form action="http://www.example.com/login.php">
  <p>Username:
    <input type="text" name="username" size="15" maxlength="30">
  </p>
</form>
```

* Password input:

```HTML
<p>Password:
  <input type="password" name="password" size="15" maxlength="30" />
</p>
```

* `<textarea>`: it's not an empty element.

```HTML
<textarea name="comments" cols="20" rows="4">Enter your comments...
</textarea>
```

* Radio button
    * `name`: the value of the name attribute should be the
      same for all of the radio buttons
      used to answer that question.
    * `value`: will send to the server.
    * `checked="checked"`: the default value when the page loads.

```html
<p>Please select your favorite genre:</p>
<br />
<input type="radio" name="genre" value="Rock" checked="checked"/> Rock
<input type="radio" name="genre" value="Pop" /> Pop
<input type="radio" name="genre" value="Jazz" /> Jazz
```

* Check box: `<checkbox>`
    * `name`: the value of the name attribute should be the
      same for all of the radio buttons
      used to answer that question.
    * `value`: will send to the server.
    * `checked="checked"`: the default value when the page loads.

```html
<input type="checkbox" name="service" value="itunes" checked="checked" /> Itunes
<input type="checkbox" name="service" value="lastfm" /> Last.fm
<input type="checkbox" name="service" value="spotify" /> Spotify
```

* Drop down list: `<select>`
    * `selected="selected"`: the default value when the page loads.

```html
<select name="devices">
  <option value="ipod">iPod</option>
  <option value="radio" selected="selected">Radio</option>
  <option value="computer">Computer</option>
</select>
```

* Comparison between radio button and drop down list:
1. If users need to see all options at a glance, radio buttons are
better suited.
2. If there is a very long list of options (such as a list of
countries), drop down list boxes work better.

* Multiple select box: `<select>`
    * `size`: how many options are shown
    * `multiple`: this determines the multiple select.

```HTML
<select name="instruments" size="3" multiple="multiple">
  <option value="guitar">Guitar</option>
  <option value="drum">Drum</option>
  <option value="keyboard">Keyboard</option>
  <option value="bass">Bass</option>
</select>
```

* File Input Box `<input>`
    * `typt=file`

```html
<p>upload your song in MP3 format:</p>
<input type="file" name="user-song" > <br />
<input type="submit" value="Upload">
```

* Submit button `<input>`
    * `type="submit"`
    * `value`: control the text that appears on a button.

```HTML
<p>Subscribe to our email list:</p>
<input type="email" name="email" value="">
<input type="submit" name="" value="Subscribe">
```

* Image button `<input>`
    * `type="image"`

```HTML
<input type="email" name="email" value="">
<input type="image" src="./images/GEB.webp" value="Subscribe"
      height="20" width="100" align="bottom"
/>
```

* Button

```HTML
<button><img src="images/add.gif" alt="add"
width="10" height="10" /> Add</button>
<input type="hidden" name="bookmark"
value="lyrics" />
```

* Labelling Form Controls `<label>`.
    * Wrap around both the text description and the form input
    * Be kept separate from the form control and use the for
      attribute to indicate which form control it is a label for
    * `for`: When a `<label>` element is used with a checkbox
      or radio button, users can click on either the form control or the
      label to select.  

```HTML
<label>Age: <input type="text" name="age"></label>
<br />
Gender:
<input id="female" type="radio" name="gender" value="f">
<label for="female">Female</label>
<input id="male" type="radio" name="gender" value="m">
<label for="male">Male</label>
```

* Above or to the left:
    * Text inputs
    * Text areas
    * Select boxes
    * File uploads
* To the right:
    * Check boxes
    * Radio button

* Grouping form elements: `<fieldset>`, `<legend>`

```html
<h1>fieldset</h1>
<fieldset>
  <legend>Contact details</legend>
  <label for="email">Email:</label> <br />
  <input id="email" type="email" name="email" /> <br />
  <label for="mobile">Mobile:</label> <br />
  <input id="mobile" type="text" name="mobile" /> <br />
  <label for="tele">Telephone:</label> <br />
  <input id="tele" type="text" name="tele" />
</fieldset>
```

* HTML5: Form Validation
    * `required="required"`

* HTML5: Date Input
    * `type="date"`

```HTML
<label for="date">Departure Date:</label>
<input id="date" type="date" name="date" />
```

* HTML5: Email & URL Input

```html
<input type="email" name="email">
<input type="submit" value="Submit">
<input type="url" name="url">
<input type="submit" value="Submit">
```

* HTML5: Search Input
    * `type="search"`
    * `placeholder`

# Ch08 Extra Markup

Pg 182 - Pg 205

* ID Attribute
    * uniquely identify that element from other elements
    * allows you to style it differently than any other
      instance of the same element on the page.
    * it's a global attribute, can be used on any element.
* Class attribute
    * Identifying several elements as being different from other elements.
    * Use CSS to change the appearance.
    * An element belongs to several classes: `class="important admittance"`
* Block element: will always appear to start a new line.
    * example: `<h1>, <p>, <ul>, <li>`
* Inline element: will always appear on the same line
    * example: `<a>, <b>, <em>, <img>`
* Grouping Text & Elements In a Block.
    * `<div>`
    * In a browser, the contents of the `<div>` element will start on
      a new line, but other than this it will make no difference to the
      presentation of the page.
    * Using an id or class attribute on the `<div>` element, however,
      means that you can create CSS style rules to indicate how
      much space the `<div>` element should occupy on the screen and
      change the appearance of all the elements contained within it.
    * Each section with `<div>`, it's easier to read the code.
    * Add a comment at the closing `<div>`, it's easier to find the opening tag.
* Grouping Text & Elements Inline with `<span>`:
    * Contain a section of text where there is no other suitable element to
      differentiate it from its surrounding text.
    * Contain a number of inline elements
    * People can control appearance through CSS.
* `<iframe>`
    * can see another page.
* `<meta>`
    * lives inside the `<head>`
    * `name="blabla"`, `content="blabla"`
* Escape Characters, see pg 194/201

# Ch09 Flash, Video, Audio

* Skip

# Ch10 Introducing CSS

Pg 233 - 251

* Understanding CCS:
    * The key to understanding how CSS works is to
      imagine that there is an invisible box around
      every HTML element.
    * Using CSS, you could add a border around any of the boxes,
      specify its width and height, or add a background color. You
      could also control text inside a box — for example, its color,
      size, and the typeface used.
    * Boxes:
        * width, height,
        * Borders: color, width, and style
        * BG color and Images
        * Positions
    * Text:
        * typeface
        * Size
        * Color
        * Italics, bold, uppercase, lowercase, small-caps
    * Specific:
        * Lists
        * Tables
        * Forms
* CSS rules:
    * selector: element the rule applies to.
      more than one element if you separate the element names
      with commas.
    * declaration, two parts, a property and a value.

```css
p {
  font-family: Arial;
}
```

* Using external CSS: To include a `css` file

```html
<link rel="stylesheet" href="./css/ch10.css" type="text/css">
```

* Using internal CSS:
    * Sits inside the `<head>` element
    * Note 2 ways to specify color

```html
<style type="text/css">
  body {
    font-family: arial;
    background-color: rgb(185,179,175);}
  h1 {
    color: #ffffff;}
</style>
```

* CSS Selectors (pg 238)
    * Universal Selector: `*`: all elements in the doc
    * Type selector, `h1, h2, h3 {}`
    * Class selector:
        * `.note {}` any element whose class attribute is `note`
        * `p.note {}` only `<p>` element whose class attribute is `note`
    * ID Selector: `#introduction {}`
    * Child Selector: `li>a {}`: Targets any `<a>` elements that
      are children of an `<li>` element
    * Descendant Selector: `p a {}`: Targets any `<a>` elements that
      sit inside a `<p>` element, even if there are other elements nested
      between them.
    * Adjacent Sibling Selector: `h1+p {}`, Targets the first `<p>` element
      after any `<h1>` element (but not other `<p>` elements)
    * General Sibling Selector `h1~p {}`: If you had two `<p>` elements that
      are siblings of an `<h1>` element, this rule would apply to both
* CSS rules cascade
    * last rule: If the two selectors are identical, the latter of the two wil
      take precedence.
    * SPECIFICITY: If one selector is more specific than the others, the more
      specific rule will take precedence over more general ones. In the following
          * `<h1>` is more specific than `*`
          * `p b ` > `b`
          * `p#intro` > `p`
    * IMPORTANT: any property value to indicate that it should be considered
      more important than other rules that apply to the same element.

```css
* {
font-family: Arial, Verdana, sans-serif;}
h1 {
font-family: "Courier New", monospace;}
i {
color: green;}
i {
color: red;}
b {
color: pink;}
p b {
color: blue ;}
p b {
color: violet !important;}
p#intro {
font-size: 100%;}
p {
font-size: 75%;}
```

* Inheritance
    * For example, `font-family` can be inherited by most child elements.
    * Force properties to inherit values from their parent using `inherit`

```css
body {
font-family: Arial, Verdana, sans-serif;
color: #665544;
padding: 10px;}
.page {
border: 1px solid #665544;
background-color: #efefef;
padding: inherit;}
```

* Advantages to use external style sheets
    * All of the webpages can share the same style sheet.
    * Only need to edit one file.
* When to consider use internal CSS
    * Just have single page
    * One page requires extra rules
    * This book's code, so you just need to open one file.
* Use the following to test your website:
    * BrowserCam.com
    * BrowserLab.Adobe.com
    * BrowserShots.org
    * CrossBrowserTesting.com

# Ch11 Color

Pg 253 - 269

* Foreground Color: `color`
    * color name: 147 predefined color name:
      [here](https://htmlcolorcodes.com/color-names/)
    * hex code
    * rgb value
* Background Color: `background-color`
    * If you do not specify a background color, then the
      background is transparent.
* Understanding Color
    * Saturation: amount of grey
    * Brightness: how much black in the color
* Contrast
    * foreground and background needs to have enough contrast.
    * check it out: [here](https://coolors.co/contrast-checker)

```css
/* color name */
h1 {
color: DarkCyan;}
/* hex code */
h2 {
color: #ee3e80;}
/* rgb value */
p {
color: rgb(100,100,90);}
```

* CSS3: `opacity`, `rgba`

```css
p.one {
background-color: rgb(0,0,0);
opacity: 0.5;}
p.two {
background-color: rgb(0,0,0);
background-color: rgba(0,0,0,0.5);}
```

* CSS3: HSL Colors

```CSS
body {
background-color: #C8C8C8;
background-color: hsl(0,0%,78%);}
p {
background-color: #ffffff;
background-color: hsla(0,100%,100%,0.5);}
```

# Ch12 Text

pg 271 - 305

* 2 groups of properties:
    * Those that directly affect the font and its appearance
    * Those that would have the same effect on text no matter
      what font you were using

## Typeface Terminology

* Serif, SANS-Serif, monospace
* Ascender: above the cap height
* Cap height: top of flat letters
* X-height: height of letter x
* Baseline: line the letter sits on
* Descender: below the base line
* Weight: light/medium/bold/black
* Style: normal/italic/oblique
* Stretch: Condensed/regular/extended

![typeface](./BookCode/BookNoteImages/ch12_typeface.png)

* Typeface example:
    * Serif: Georgia/Times/Times new roman
    * Sans-Serif: Arial/ Verdana/ Helvetica
    * Monospace: Courier/ Courier New
    * Cursive: Comic Sans MS/ Monotype Corsiva
    * Fantasy: Impact/ Haettenschweiler
    * Browsers are supposed to support at least one typeface from each of
      the groups above. For this reason, it is common to add the generic font
      name after your preferred choice of typefaces.
    * `font-family: Georgia, Times, serif;`
* Specifying Typefaces: `font-family`
* Size of Type: `font-size`
    * pixels: `12px`
    * Percentage: `font-size: 200%;`, default is `16px`, then if body is 75%
      then it is 12px. If the an element inside body is 75%, then it's 9px.
    * ems: equivalent to the width of a letter "m"
* Type Scales
    * 1-inch is 72 pixels.
* More Font Choice:
    * https://fontlibrary.org/en
    * http://www.fontex.org/
    * https://www.fontsquirrel.com/
    * google fonts
* Bold: `font-weight`
    * `bold`
    * `normal`
* `font-style`: `normal/italic/oblique`
* upper/lower case: `text-transform`
    * `uppercase/lowercase/capitalize`
* Underline & Strike: `text-decoration`:
    * `none/underline/overline/line-through/blink`
* Leading: `line-height`
    * Leading is measured from the bottom of the descender on one line to the
      top of the ascender on the next.
    * `line-height` property sets the height of an entire line of text, so the
      difference between the `font-size` and the `line-height` is
      equivalent to the leading.

```css
p {
line-height: 1.4em;}
```

* `letter-spacing, word-spacing`
    * It is particularly helpful to increase the kerning when
      your heading or sentence is all in uppercase.
    * When you specify a value for these properties, it should
      be given in ems, and it will be added on top of the default value
      specified by the font.

```css
h1, h2 {
text-transform: uppercase;
letter-spacing: 0.2em;}
.credits {
font-weight: bold;
word-spacing: 1em;}
```

* Alignment: `text-align`
    * `left/right/center`
    * `justify`: every line in a paragraph, except the last line,
      should be set to take up the full width of the containing box.

```css
h1 {
text-align: left;}
p {
text-align: justify;}
.credits {
text-align: right;}
```

* `vertical-align`:
    * It is not intended to allow you to vertically align text in the middle
      of block level elements such as `<p>` and `<div>`
    * it does have this effect when used with table cells: the `<td>` and `<th>`
    * `baseline sub super top text-top middle bottom text-bottom`

* `text-indent`

```css
h1 {
background-image: url("images/logo.gif");
background-repeat: no-repeat;
text-indent: -9999px;}
.credits {
text-indent: 20px;}
```

* `text-shadow`
    * The first length indicates how far to the left or right the shadow
      should fall.
    * The second value indicates the distance to the top or bottom
      that the shadow should fall.
    * The third value is optional and specifies the amount of blur that
      should be applied to the drop shadow.
    * The fourth value is the color of the drop shadow.

```css
p.one {
background-color: #eeeeee;
color: #666666;
text-shadow: 1px 1px 0px #000000;}
```

* First Letter or Line: `:first-letter, :first-line`
    * They are pseudo-elements.
    * pseudo-element is at the end of the selector.

```css
p.intro:first-letter {
font-size: 200%;}
p.intro:first-line {
font-weight: bold;}
```

* Styling links
    * `a:link`: This allows you to set styles for links that have not yet been
      visited.
    * `a:visited`: This allows you to set styles for links that have been
      clicked on.
    * `:hover`:
        * This is applied when a user hovers over an element with a pointing
          device such as a mouse.
        * This has commonly been used to change the appearance of
          links and buttons when a user places their cursor over them.
        * Not working for iPad.
    * `:active`:
        * This is applied when an element is being activated by a user.
        * when a button is being pressed or a link being clicked.
    * `:focus`:
        * Focus occurs when a browser discovers that you are ready to
          interact with an element on the page.
        * For example, when your cursor is in a form input ready
          to accept typing, that element is said to have focus.
        * It is also possible to use the tab key on
          your keyboard to move through the interactive items on a page.

```css
a:link {
color: deeppink;
text-decoration: none;}
a:visited {
color: black;}
a:hover {
color: deeppink;
text-decoration: underline;}
a:active {
color: darkcyan;}
input {
padding: 6px 12px 6px 12px;
border: 1px solid #665544;
color: #ffffff;}
input.submit:hover {
background-color: #665544;}
input.submit:active {
background-color: chocolate;}
input.text {
color: #cccccc;}
input.text:focus {
color: red;}
```

## Attribute Selectors

Pg 292/299

* More general is in Pg 238
* `p[class]`, Existence: Targets any `<p>` element with an
  attribute called `class`
* `p[class="dog"]`: Targets any `<p>` element with an attribute called class whose
  value is dog
* `p[class~="dog"]`: Targets any `<p>` element with an attribute called class whose
  value is a list of space-separated words, one of which is dog
* `p[attr^"d"]`: Targets any `<p>` element with an attribute whose value begins
  with the letter "d"
* `p[attr*"do"]`: Targets any `<p>`element with an attribute whose value contains
  the letters "do"
* `p[attr$"g"]`: Targets any `<p>` element with an attribute whose value ends with
  the letter "g"

# Ch13 Boxes

Pg 307 - 335
