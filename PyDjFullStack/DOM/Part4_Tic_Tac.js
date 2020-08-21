console.log("Hello Tic Tac Toe!");

var my_button = document.querySelector("#my_button");
var my_td = document.querySelectorAll("td");

my_button.addEventListener("click", function () {
  console.log("botton got click");
  for (var i = 0; i < my_td.length; i++) {
    my_td[i].textContent = "";
  }
  console.log("botton got click again");
})

console.log(my_td);
for (var i = 0; i < my_td.length; i++) {
  my_td[i].addEventListener("click", function () {
    if (this.textContent == "X") {
      this.textContent = "O";
      this.style.color = "red";
    } else if (this.textContent == "O") {
      this.textContent = "";
    } else {
      this.textContent = "X";
      this.style.color = "black";
    }
  })
}
