
function sleepIn(weekday, vacation) {
  return (!weekday) || vacation;
}

console.log(sleepIn(false, false));
console.log(sleepIn(true, false));
console.log(sleepIn(false, true));

console.log("Test monkeyTrouble");

function monkeyTrouble(aSmile, bSmile) {
  return !(aSmile ^ bSmile);
}

console.log(monkeyTrouble(true, true));
console.log(monkeyTrouble(false, false));
console.log(monkeyTrouble(true, false));

console.log("Test stringTimes");

function stringTimes(str, n) {
  ret = "";
  for (var i = 0; i < n; i++) {
    ret += str
  }
  return ret;
}

console.log(stringTimes("Hi", 2));
console.log(stringTimes("Hi", 3));
console.log(stringTimes("Hi", 1));

console.log("lucky sum");

function luckySum(a, b, c) {
  ret = 0
  if (a == 13) {
    return ret;
  } else {
    ret += a;
  }
  if (b == 13) {
    return ret;
  } else {
    ret += b;
  }
  if (c == 13) {
    return ret;
  } else {
    ret += c;
  }
  return ret;
}

console.log(luckySum(1,2,3));
console.log(luckySum(1,2,13));
console.log(luckySum(1,13,3));

function caught_speeding(speed, is_birthday) {
  if (speed <= 60+is_birthday*5) {
    return 0;
  } else if (61+is_birthday*5 <= speed && speed <= 80+is_birthday*5) {
    return 1;
  } else {
    return 2;
  }
}
console.log("Test caught_speeding");
console.log(caught_speeding(60, false));
console.log(caught_speeding(65, false));
console.log(caught_speeding(65, true));
console.log(caught_speeding(85, true));
console.log(caught_speeding(81, false));

console.log("Test makeBricks");

function makeBricks(small, big, goal) {
  while (goal >= 5 && big > 0) {
    goal -= 5;
    big--;
  }
  return (goal <= small);
}

console.log(makeBricks(3,1,8));
console.log(makeBricks(3,1,9));
console.log(makeBricks(3,2,10));
