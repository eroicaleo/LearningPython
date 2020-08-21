console.log("Hello Part 6");

var employee = {
  name : "John Smith",
  job : "Programmer",
  age : 31,
  namelength : function () {
    console.log("The name length of " + this.name + " is: " + this.name.length);
  }
};

employee.namelength();

employee = {
  name : "John Smith",
  job : "Programmer",
  age : 31,
}

// for (var key in employee) {
//   if (employee.hasOwnProperty(key)) {
//       alert(key + " is " + employee[key])
//   }
// }

employee = {
  name : "John Smith",
  job : "Programmer",
  age : 31,
  lastname : function () {
    var ln = this.name.split(" ").pop()
    console.log("The last name of " + this.name + " is: " + ln);
  }
}

employee.lastname()
