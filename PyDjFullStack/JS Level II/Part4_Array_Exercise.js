
var roster = []

function addNew(name) {
  roster.push(name);
}

function remove(name) {
}

function display() {
  console.log(roster.toString());
}

var cmd;
while (true) {
  cmd = prompt("Enter your command:");
  // console.log(cmd);
  if (cmd == "quit") {
    break;
  } else if (cmd == "add") {
    addNew(prompt("Enter the name you want to add:"));
  } else if (cmd == "display") {
    display();
  } else if (remove) {
    var index = roster.indexOf(prompt("Enter the name you want to add:"));
    if (index > -1) {
      roster.splice(index, 1);
    }
  }
}

// addNew('Shannon');
// addNew('Wayne');
// display();
