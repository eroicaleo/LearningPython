var countries = [
  "USA",
  "Germany",
  "China"
]

console.log(countries);
for (var i = 0; i < countries.length; i++) {
  console.log(countries[i]);
}

var mixed = [
  true,
  20,
  "string",
]
for (var i = 0; i < mixed.length; i++) {
  console.log(mixed[i]);
}

var myArr = [
  'one',
  'two',
  'three',
]

myArr.forEach(function(item, index, array) {
  console.log(item, index)
})

var lastItem = myArr.pop()
console.log("lastItem: " + lastItem);

myArr.forEach(function(item, index, array) {
  console.log(item, index)
})

myArr.push("new_item")

myArr.forEach(function(item, index, array) {
  console.log(item, index)
})

var matrix = [[0,1,2],[4,5,6],[7,8,9]]

for (var letter of myArr) {
  console.log(letter);
}

// myArr.forEach(alert)

function addAwesome(name) {
  console.log(name+ " is awesome!");
}

var topics = ["python", "django", "science"]
topics.forEach(addAwesome)
