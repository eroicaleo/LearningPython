console.log("Yang Ge");
var name = prompt("What's your name")
var name_array = name.split(" ")
console.log(name_array);
var age = prompt("What's your age")
console.log(age);
var ht = prompt("How tall are you in (cm)")
var pet = prompt("What's your pet's name");

var condition = 0
if ( name_array[0][0] == name_array[1][0]) {
  console.log("First name and last name starts with the same letter: " + name_array[0][0]);
  condition++;
}

if (20 <= age && age <= 30) {
  console.log("Age is between 20 and 30: " + age);
  condition++;
}

if (ht >= 170) {
  console.log("Height is higher than 170: " + ht);
  condition++;
}

if (pet[pet.length-1] === "y") {
  console.log("Pet ends with y: " + pet);
  condition++;
}

if (condition == 4) {
  console.log("Congrats: happy coding!");
} else {
  console.log("Can't tell you!");
}
