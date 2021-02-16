import logo from './logo.svg';
import './App.css';
import React from 'react';

function App() {
  const greeting = 'Welcome to React';
  return (
    <div>
      <Greeting greeting={greeting}/>
      <Greeting2 greeting={greeting}/>
      <Greeting3 greeting={{text: "greeting"}}/>

    </div>
  )
}

const Greeting = props => (
    <div>
      <h1>{props.greeting}</h1>
    </div>
  );

const Greeting2 = ({greeting}) => <h1>{greeting}</h1>

const Greeting3 = ({greeting}) => <h1>{greeting.text}</h1>

export default App;
