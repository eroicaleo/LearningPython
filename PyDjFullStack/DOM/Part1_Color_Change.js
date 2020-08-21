console.log("Hello!");

console.log(document.URL);

console.log(document.getElementById("pickme"));
console.log(document.getElementsByClassName("myul"));
console.log(document.getElementsByTagName('li'));
console.log(document.querySelector("#pickme"));
console.log(document.querySelectorAll(".myul"));
console.log(document.querySelectorAll("li"));
console.log(document.querySelector(".myul"));

var myheader = document.querySelector("h1")
console.log(myheader);
myheader.style.color = 'red';

function getRandomColor() {
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color;
}

function changeHeaderColor() {
  colorInput = getRandomColor();
  myheader.style.color = colorInput;
}

setInterval("changeHeaderColor()", 500);
