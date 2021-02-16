# Contents

* [link here](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/Book.txt)

# 00 Hello React

* The "How to learn React, Angular or Vue in 2019?"
  * (1) narrow down your learning material and supplement it with material for all your senses
  * (2) consume the learning material and start to produce on the side
  * (3) pick up a project that keeps you motivated
  * (4) break out in a cold sweat and take hours to tinker on your project
  * (5) get help with your search engine, Slack groups or StackOverflow
  * (6) finish you project and gather feedback from others
  * (7) if still stuck in analysis paralysis, implement the same project in another framework
  * repeat (3) to (6)

# 01 Requirements

* Read [link](https://www.robinwieruch.de/react-js-macos-setup) here.
* `npm install -g create-react-app`
* Solved problems with this [link](https://stackoverflow.com/questions/47252451/permission-denied-when-installing-npm-modules-in-osx)
* This command: `sudo chown -R yg943079 /usr/local/lib/node_modules`

# 02 Setting up a React Project

* [link here](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/react-modern/setup.md)
* `npx create-react-app hacker-stories`
* Main focus for now: `src/App.js`: implement react components.
* `src/App.test.js`: for your test.
* `src/index.js`: for entering the React.
* `package.json`: can find the specific commands.
  * `npm start`
  * `npm test`
  * `npm run build`

# 03 Meet the React Component

* [link here](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/react-modern/meet-the-react-component.md)
* The `APP` component is commonly called function component.
* It doesn't receive any parameters in its function signature.
* It returns code that resembles HTML which is called JSX.

## Exercise

### 3.1 Read More about `let`

* Difference with `var`: `let` allows you to declare variables with the
  scope of a block.

### 3.2 `const`

* It cannot be reassigned or redeclared.

# 04 React JSX

* If we want to use a variable inside JSX returned, we just use `{var}`
  like: `<h1>Hello {title} world!</h1>`
* JSX replaces a handful of internal HTML attribus: [supported html attributes](https://reactjs.org/docs/dom-elements.html#all-supported-html-attributes)
* Everything in curly braces in JSX can be used for JavaScript expressions (e.g. function execution), this is pretty much like python's f-string.

## Exercise

* Read more about [JSX](https://reactjs.org/docs/introducing-jsx.html)
    * If a tag is empty, you may close it immediately with `/>`, like XML:

```javascript
const element = <img src={user.avatarUrl}></img>;
const element = <img src={user.avatarUrl} />;
```

# 05 Lists in React

* [link](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/react-modern/lists.md)
* The list can be used with `map` method. Example:

```javascript
{list.map(function(item){
  return (
    <div key={item.objectID}>
      <span>
        <a href={item.url}>{item.title}</a>
      </span>
      <span>{item.author}</span>
      <span>{item.num_comments}</span>
      <span>{item.points}</span>
    </div>
  );
})}
```

## Exercise

* 2.0 One way to generate unique key for each list item:

```javascript
{joshs.map((person, index) => (
  <span key={`key-${person.Name}`}>{person.Name}</span>
))}
```

* 2.1 Robin's example:

```javascript
const [list, setList] = React.useState(robinlist);

const handleClick = event => {
  setList(list.slice().reverse());
  console.log(list);
};

<div>
  <ul>
    {list.map((item, index) => (
      <li key={item.id}>
        <label>
          <input type="checkbox" />
          {item.name}
        </label>
      </li>
    ))}
  </ul>

  <button type="button" onClick={handleClick}>
    Reverse List
  </button>
</div>
```

* 2.2 Official doc
    * Assume function `NumberList` returns a JSX, then
      in another JSX, we can do the follow 2 ways.
```javascript
<ul>
{Ex2_2()}
<Ex2_2 />
</ul>
```

    * Keys help React identify which items have changed, are added, or are removed. Keys should be given to the elements inside the array to give the elements a stable identity.
    * May use index as the last resort. But it's not recommended.
    * Keys only make sense in the context of the surrounding array.
      A good rule of thumb is that elements inside the map() call need keys.
    * Keys used within arrays should be unique among their siblings. However they don’t need to be globally unique. We can use the same keys when we produce two different arrays.

# 06 Meet Another React Component

* There are 2 ways that can put JSX in another function, or component in React's
  language.

```javascript
function List() {
  return list.map(function (item) {
    return (
      <div key={item.objectID}>
        <span>
          <a href={item.url}>{item.title}</a>
        </span>
        // Omit the additional code
      </div>
    );
  });
}

function List2() {
  return (
    <div>
      {list.map(function (item) {
        return (
          <div key={item.objectID}>
            <span>
              <a href={item.url}>{item.title}</a>
            </span>
            // Omit the additional code
          </div>
        );
      })}
    </div>
  );
}
```

* Larger React applications have **component hierarchies** (also called **component trees**).
* There is usually one uppermost entry point component (e.g. `App`) that spans a tree of components below it.
* The `App` is the **parent component** of the `List`, so the `List` is a **child component** of the App.
* In a component tree, the `App` is the root component, and the components that don't render any other components are called **leaf components** (e.g. `Item`).
* The `App` can have multiple children, as can the List. If the `App` has another child component, the additional child component is called a **sibling component** of the `List`.

# 07 React Component Instantiation

* Once we've defined a **component**, we can use it like an HTML **element** anywhere in our JSX.
* The element produces an **component instance** of your component, or in other words, the component gets instantiated.
* You can create as many component instances as you want. It's not much different from a JavaScript class definition and usage.

## ex 7.3

* Think about how it could be possible to give each List component its own `list`.
* This has been covered in previous exercises, when we went through
  the official doc.

```javascript
<List list={list1} />
```

# 08 React DOM

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

* We move to `index.js`.
* A library called `react-dom` has been imported in this file, `ReactDom.render()`
  is called.
* `ReactDOM.render()` expect 2 arguments.
    1. The first is to instantiate `App` components. We can also just pass simple
       JSX.
    2. The second argument specifies where the React application enters your HTML. It expects an element with an `id='root'`. found in the *public/index.html* file.

## ex03

* React elements are **immutable**, like a single frame in a movie.
* React DOM compares the element and its children to the previous one, and only applies the DOM updates necessary to bring the DOM to the desired state.
* In our experience, thinking about how the UI should look at any given moment, rather than how to change it over time, eliminates a whole class of bugs.

# 09 React Component Definition (Advanced)

* JavaScript allow to use `arrow` to define functions

```javascript
// allowed
const item => { ... }

// allowed
const (item) => { ... }

// not allowed
const item, index => { ... }

// allowed
const (item, index) => { ... }
```

* `concise body`: If an arrow function doesn't do anything in between, but only
  returns something, -- in other words, if an arrow function doesn't perform any
  task, but only returns information --, you can remove the `block body`
  (curly braces) of the function.
  In a concise body, an `implicit return statement` is attached, so you can remove
  the return statement:

```javascript
// with block body
count => {
  // perform any task in between

  return count + 1;
}

// with concise body
count =>
  count + 1;
```

## ex02 Read more about arrow functions

* remove function, remove body brackets, remove argument parentheses.
* If body needs additional lines of processing, then we need brackets and `return`
* To return an object literal expression requires parentheses around expression,
  this is kinda like return a JSX.
* Destructuring within params supported

```javascript
let anne = ([a, b] = [10, 20]) => a+b;
console.log(anne());
console.log(anne([50,60]));

let ben = ({ a, b } = { a: 10, b: 20 }) => a + b;
console.log(ben({a:70, b:80, c:90}));
```

# 10 Handler Function

* The `input` fields have a `onchange handler`.
* Now the function can be passed to the `onChange` attribute of the `input` field.

```javascript
const App = () => {
  const handleChange = event => {
    console.log(event);
  };

  return (
    <div>
      // ...
      <input id="search" type="text" onChange={handleChange} />
      // ...
    </div>
  );
};
```

* This is called a `synthetic event` defined by a JavaScript object.
* Always pass functions to these handlers, not the return value of the function,
  except when the return value is a function.

  ```javascript
  // Don't do this
  const App = () => {
    // ...
    return (
      <div>
        // ...
        <input id="search" type="text" onChange={handleChange()} />
        // ...
      </div>
    );
  };
  ```

## ex 02 Read more about React Event

* [here](https://reactjs.org/docs/events.html)
* Every synthetic event has the following attribus:

```javascript
boolean bubbles
boolean cancelable
DOMEventTarget currentTarget
boolean defaultPrevented
number eventPhase
boolean isTrusted
DOMEvent nativeEvent
void preventDefault()
boolean isDefaultPrevented()
void stopPropagation()
boolean isPropagationStopped()
void persist()
DOMEventTarget target
number timeStamp
string type
```

# 11 React Props

* There, we can access it through the first function
  signature's argument, called `props`
* Here is the example

```javascript

const App = () => (
    <div>
      <List list={list1} />
    </div>
);

const List = (props) => props.list.map(item => (
      <div key={item.objectID}>
        <a href={item.url}>{item.title}</a>
        <span> {item.author}</span>
        <span> {item.num_comments} </span>
        <span> {item.points} </span>
      </div>
    )
  );
```

## Exercise

* Read more about [how to pass props to React components](https://www.robinwieruch.de/react-pass-props-to-component).

* The following are the same:

```javascript
const Greeting = props => (
    <div>
      <h1>{props.greeting}</h1>
    </div>
  );

const Greeting2 = ({greeting}) => <h1>{greeting}</h1>
```

* We can even pass an object

```javascript
<Greeting3 greeting={{text: "greeting"}}/>
const Greeting3 = ({greeting}) => <h1>{greeting.text}</h1>
```

* We will skip from the 2nd section for now.
