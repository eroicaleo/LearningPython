
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

function App() {
  return (
    <div>
      <h1>My Hacker Stories</h1>
      <label htmlFor="search">Search: </label>
      <input id="search" type="text" />

      <List />
      <hr />
      <List2 />
    </div>
  );

}

function List() {
  return list.map(function (item) {
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
            <span>{item.author}</span>
            <span>{item.num_comments}</span>
            <span>{item.points}</span>
          </div>
        );
      })}
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
