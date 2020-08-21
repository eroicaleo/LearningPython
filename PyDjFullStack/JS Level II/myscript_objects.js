console.log("Hello Objects!");

var myCar = {
    make: 'Ford',
    modle: 'Mustang',
    year: 1969,
};

console.log(myCar);
console.log(myCar["make"])

var myNewO = {a:"hello", b:[1,2,3], c:{inside:['a', 'b']}}

console.log(myNewO["b"][1]);
console.log(myNewO["c"]["inside"][1]);

myCar['year'] = 2006
console.log(myCar['year']);
myCar['year'] += 1
console.log(myCar['year']);
console.dir(myCar);

for (var key in myCar) {
  if (myCar.hasOwnProperty(key)) {
    console.log(key);
    console.log(myCar[key]);
  }
}

var carInfo = {
  make: "Toyota",
  year: 1990,
  model: "Camry",
  carAlert: function(){
    alert("We've got a car here!")
  }
};

var myObj = {
  prop: 37,
  reportProp: function() {
    return this.prop;
  }
};

console.log(myObj.reportProp());

var simple = {
  prop : "Hello",
  myMethod : function () {
    console.log("The myMethod was called");
  }
}

console.log(simple.myMethod);
simple.myMethod()
console.log(simple);

var myObj = {
  name : "Jose",
  greet : function () {
    console.log("Hello " + this.name);
  }
};

myObj.greet()
console.log(myObj["name"]);
