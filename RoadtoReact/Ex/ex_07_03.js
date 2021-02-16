import React from 'react';

const list1 = [
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

const list2 = [
  {
    title: 'Django',
    url: 'https://djangoproject.com/',
    author: 'Adrian Holovaty, Simon Willison',
    num_comments: 3,
    points: 4,
    objectID: 0,
  },
  {
    title: 'Flask',
    url: 'https://flask.palletsprojects.com',
    author: 'Armin Ronacher',
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
      <hr />
      <List list={list1} />
      <hr />
      <List list={list2} />
    </div>
  );

}

function List(props) {
  const list = props.list;
  return list.map(function (item) {
    return (
      <div key={item.objectID}>
        <a href={item.url}>{item.title}</a>
        <span> {item.author}</span>
      </div>
    );
  });
}

export default App;
