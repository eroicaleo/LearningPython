import React from 'react';

const App = () => {

  const stories = [
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

  const stories2 = [
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

  console.log("lala");
  const handleChange = event => {
    console.log(event.target.value);
  }

  const handleOnClick = event => {
    console.log("I have been clicked!");
    console.log(event.target.text)
  }

  const handleOnMouseEnter = event => {
    console.log("Mouse entered!");
  }

  const handleOnMouseLeave = event => {
    console.log("Mouse left!");
  }

  return (
    <div>
      <h1 onClick={handleOnClick} onMouseEnter={handleOnMouseEnter}
      onMouseLeave={handleOnMouseLeave}>
        My Hacker Stories
      </h1>
      <label htmlFor="search">Search: </label>
      <input id="search" type="text" onChange={handleChange} />
      <hr />
      <List list={stories} />
      <hr />
      <List list={stories2} />
    </div>
  );
}

const List = (props) => props.list.map(item => (
      <div key={item.objectID}>
        <a href={item.url}>{item.title}</a>
        <span> {item.author}</span>
        <span> {item.num_comments} </span>
        <span> {item.points} </span>
      </div>
    )
  );

export default App;
