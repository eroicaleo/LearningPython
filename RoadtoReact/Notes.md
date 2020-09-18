# Contents

* [link here](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/Book.txt)

# Hello React

* The "How to learn React, Angular or Vue in 2019?"
  * (1) narrow down your learning material and supplement it with material for all your senses
  * (2) consume the learning material and start to produce on the side
  * (3) pick up a project that keeps you motivated
  * (4) break out in a cold sweat and take hours to tinker on your project
  * (5) get help with your search engine, Slack groups or StackOverflow
  * (6) finish you project and gather feedback from others
  * (7) if still stuck in analysis paralysis, implement the same project in another framework
  * repeat (3) to (6)

# Requirements

* Read [link](https://www.robinwieruch.de/react-js-macos-setup) here.
* `npm install -g create-react-app`
* Solved problems with this [link](https://stackoverflow.com/questions/47252451/permission-denied-when-installing-npm-modules-in-osx)
* This command: `sudo chown -R yg943079 /usr/local/lib/node_modules`

# Setting up a React Project

* [link here](https://github.com/the-road-to-learn-react/the-road-to-react/blob/master/manuscript/react-modern/setup.md)
* `npx create-react-app hacker-stories`
* Main focus for now: `src/App.js`: implement react components.
* `src/App.test.js`: for your test.
* `src/index.js`: for entering the React.
* `package.json`: can find the specific commands.
  * `npm start`
  * `npm test`
  * `npm run build`

# Meet the React Component

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

# React JSX

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

# Lists in React

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
