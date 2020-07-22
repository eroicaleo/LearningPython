
var i = 0

console.log("while loop");
while (i++ < 5) {
  console.log("Hello " + i);
}

console.log("For loop");
for (var i = 0; i < 5; i++) {
  console.log("Hello " + i);
}

i = 1
while (i <= 25) {
  console.log("while loop: " + i);
  i += 2
}

for (var i = 1; i < 26; i += 2) {
  console.log("for loop: " + i);
}
