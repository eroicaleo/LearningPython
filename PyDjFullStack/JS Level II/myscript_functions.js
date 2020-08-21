console.log("Hello!");

function hello() {
  console.log("hello world!");
}

hello()

function helloyou(name) {
  console.log("Hello " + name);
}

helloyou("Shannon")
helloyou()

function addNum(num1, num2) {
  console.log(num1+num2);
}

addNum("Hello", "world")

function helloSomeone(name="Frankie") {
  console.log("Hello " + name);
}

helloSomeone()

function formal(name="Sam", title='Sir') {
  return title+ " "+name
}

console.log("Welcome " + formal());

function timesFive(numInput) {
  var result = numInput*5;
  return result
}

console.log(timesFive(100));

var v = "global v"
var stuff = "global stuff"

function fun(stuff) {
  console.log(v);
  stuff = "reassign stuff inside func"
  console.log(stuff);
}

fun();
console.log(stuff);
