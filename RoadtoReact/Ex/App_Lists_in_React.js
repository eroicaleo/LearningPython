
import React from 'react';

const list = [
  {
    title: 'React',
    url: 'https://reactjs.org/',
    author: 'Jordan Walke',
    num_comments: 3,
    points: 4,
    objectID: 0,
  },
  {
    title: 'Redux',
    url: 'https://redux.js.org/',
    author: 'Dan Abramov, Andrew Clark',
    num_comments: 2,
    points: 5,
    objectID: 1,
  },
];

const joshs = [{  Name: "Josh", }, { Name: "Joshina", }, {  Name: "Notjosh", }]

// This is for Exercise 2.1
const robinlist =  [
  { id: 'a', name: 'Learn React' },
  { id: 'b', name: 'Learn GraphQL' },
];

function Ex2_1() {

  const [list_2_1, setList] = React.useState(robinlist);

  const handleClick = event => {
    setList(list_2_1.slice().reverse());
    // console.log(list);
  };

  return (
    <div>
      <ul>
        {list_2_1.map((item, index) => (
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
  );
}

// This is for Exercise 2.2
function Ex2_2() {
  const numbers = [1,2,3,4,5];
  const doubled = numbers.map((number) => number*2);
  console.log(doubled);

  const listItems = numbers.map((number) =>
    <li>{number}</li>
  );

  return listItems;
}

function NumberList(props) {
  const numbers = props.numbers;
  const ListItems = numbers.map((number) =>
    <li key={number.toString()}>
      {number}
    </li>
  );

  return (
    <ul>{ListItems}</ul>
  );
}

function ListItem(props) {
  return <li>{props.value}</li>
}

function NumberList2(props) {
  const numbers = props.numbers;
  const ListItems = numbers.map((number) =>
    <ListItem key={number.toString()} value={number}/>
  );

  return (
    <ul>{ListItems}</ul>
  );
}

function NumberList3(props) {
  const numbers = props.numbers;

  return (
    <ul>
    {numbers.map((number) =>
      <ListItem key={number.toString()} value={number}/>
    )}
    </ul>
  );
}

function Blog(props) {
  const sidebar = (
    <ul>
      {props.posts.map((post) =>
        <li key={post.id}>
          {post.title}
        </li>
      )}
    </ul>
  );

  const content = props.posts.map((post) =>
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
        </div>
      );

  return (
    <div>
      {sidebar}
      <hr />
      {content}
    </div>
  );
}

function App() {

  const numbers = [1, 2, 3, 4, 5];

  const posts = [
    {id: 1, title: 'Hello World', content: 'Welcome to learning React!'},
    {id: 2, title: 'Installation', content: 'You can install React from npm.'}
  ];

  return (
    <div>
      <h1>My Hacker Stories</h1>

      <label htmlFor="Search">Search: </label>
      <input id="search" type="text" />

      <hr />
      {Ex2_1()}

      <hr />
      <ul>
      {Ex2_2()}
      </ul>

      <hr />
      <h3>This uses function</h3>
      <NumberList numbers={numbers} />

      <hr />
      <h3>User NumberList and ListItem</h3>
      <NumberList2 numbers={numbers} />

      <hr />
      <h3>Use key in 2 JSX, but in the same function</h3>
      <Blog posts={posts} />

      <hr />
      <h3>User NumberList3: embed <code>map</code> into JSX</h3>
      <NumberList3 numbers={numbers} />

    </div>
  );
}

export default App;


// This is for React JSX

// import React from 'react';
//
// const title = "React";
// const welcome = {
//   greeting: 'Hey',
//   title: 'React',
// };
//
// function getTitle(title) {
//   return title
// }
//
// var countries = ["USA", "Germany", "China"];
//
// function App() {
//
//   return (
//     <div>
//       <h1>Hello {title} world!</h1>
//
//       <h1>{welcome.greeting} {welcome.title}</h1>
//
//       <h1>Hello {getTitle('React')}</h1>
//
//       <h1>Hello countries: {countries}</h1>
//
//       <label htmlFor="search">Search:</label>
//       <input id="search" type="text" />
//     </div>
//   );
// }
//
// export default App;

// import React from 'react';
// import logo from './logo.svg';
// import './App.css';
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//
// export default App;
