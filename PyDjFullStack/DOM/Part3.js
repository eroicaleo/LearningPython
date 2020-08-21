console.log("Hello Part3");

var head1 = document.querySelector("#one")
var head2 = document.querySelector("#two")
var head3 = document.querySelector("#three")
console.log(head1.textContent);

head1.addEventListener("mouseover", function () {
  head1.textContent = "Mouse Currently Over";
  head1.style.color = "red";
})

head1.addEventListener("mouseout", function () {
  head1.textContent = "HOVER OVER ME";
  head1.style.color = "black";
})

var no_click = 0;
head2.addEventListener("click", function () {
  no_click++;
  if (no_click%2 == 0) {
    head2.textContent = "CLICK";
    head2.style.color = "black";
  } else {
    head2.textContent = "CLICK DONE";
    head2.style.color = "blue";
  }

})

head3.addEventListener("dblclick", function () {
  head3.textContent = "I WAS DOUBLE CLICKED";
  head3.style.color = "red";
})
