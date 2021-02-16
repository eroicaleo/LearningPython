console.log("Hello ex_09_02.js");

const materials = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium'
];

console.log(materials.map(material => material.length));

let bob = a => a+100;
console.log(bob(100));

// let anne = () => ({foo: "a"})
let anne = ([a, b] = [10, 20]) => a+b;
console.log(anne());
console.log(anne([50,60]));

let ben = ({ a, b } = { a: 10, b: 20 }) => a + b;
console.log(ben({a:70, b:80, c:90}));
