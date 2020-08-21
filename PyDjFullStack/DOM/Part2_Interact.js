console.log("Hello Part2 Interact!");

var p = document.querySelector("p");
console.log(p);

p.textContent = "new text";
p.innerHTML = "<strong>I'am bold</strong>"

var special = document.querySelector("#special")
console.log(special);
var specialA = special.querySelector("a")
console.log(specialA);
console.log(specialA.getAttribute("href"));
specialA.setAttribute("href", "https://www.goodreads.com")
