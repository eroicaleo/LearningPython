var hot = false
var temp = 10

if (temp > 80) {
  console.log("Hot Outside!");
} else if (50 <= temp && temp <= 80) {
  console.log("Average temp Outside");
} else if (32 <= temp && temp < 50) {
  console.log("It's pretty cold out!");
} else {
  console.log("It's very cold out!");
}

console.log(hot)

var x = 0

while (x < 5) {
  console.log("x is currently: " + x);

  if (x === 3) {
    console.log("x IS EQUAL TO THREE");
    break;
  }
  x++;
}

x = 0;
while (x < 11) {
  if (x % 2 == 0) {
    console.log("x is even: " + x);
  }
  x++;
}

for (var i = 0; i < 5; i++) {
  console.log("Number is: " + i);
}

var word = "ABCDEFGHIJK"
for (var i = 0; i < word.length; i++) {
  console.log(word[i]);
}

word = "ABABABABABAB"
for (var i = 0; i < word.length; i += 2) {
  console.log(word[i]);
}
