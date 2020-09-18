console.log("Hello jQuery Part1");

// var x = $('h1');
// x.css('color', 'red');
// x.css('background', 'blue');
//
// var newCSS = {
//   'color': 'white',
//   'background': 'green',
//   border: '20px solid red',
// };
//
// x.css(newCSS)

var listItems = $('li');
console.log(listItems);

listItems.css('color', 'blue');
listItems.eq(0).css('color', 'orange');

listItems.eq(-1).css('color', 'orange');

console.log($('h1').text());
$('h1').text("Brand New Text")
$('h1').html("<em>New</em>")

$('input').eq(1).attr("type", 'checkbox');
$('input').eq(0).val("new value!")

$('h1').addClass('turnRed');
$('h1').removeClass('turnRed');

function changeColor() {
  $('h1').toggleClass('turnBlue');
}

setInterval(changeColor, 500)
