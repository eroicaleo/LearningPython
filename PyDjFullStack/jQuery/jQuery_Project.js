console.log("Hello jQuery_Project");

var user0 = prompt('First user please enter your name:')
var user1 = prompt('Second user please enter your name:')
var user_list = [user0, user1];
var rule_string = " it's your turn, please pick a column to drop your blue chip";

$('h3').text(user0 + rule_string)

var columns = [5,5,5,5,5,5,5];
var dot_in_row = 7;
var dot_in_col = 6;
var num_of_row = dot_in_col;
var num_of_col = dot_in_row;

var dot_colors = []
for (var i = 0; i < dot_in_col; i++) {
  dot_colors.push(Array(dot_in_row).fill('x'));
}

function check_row() {
  for (var row = 0; row < dot_in_col; row++) {
    var row_string = dot_colors[row].toString()
    if (row_string.includes('0,0,0,0')) {
      return 0;
    } else if (row_string.includes('1,1,1,1')) {
      return 1;
    }
  }
  return -1;
}

function check_col() {
  for (var i = 0; i < dot_in_row; i++) {
    var col_string = '';
    for (var j = 0; j < dot_in_col; j++) {
      col_string += (dot_colors[j][i].toString()+',')
    }
    if (col_string.includes('0,0,0,0')) {
      console.log('col_string: ', col_string);
      return 0;
    } else if (col_string.includes('1,1,1,1')) {
      console.log('col_string: ', col_string);
      return 1;
    }
  }
  return -1;
}

function check_dia() {
  let start_index = [[2,0],[1,0],[0,0],[0,1],[0,2],[0,3]]
  start_index.forEach((item) => {
    let x = item[0];
    let y = item[1];
    let dia_string = '';
    for (; x < num_of_row && y < num_of_col; x++, y++) {
      dia_string += (dot_colors[x][y].toString()+',')
    }
    if (dia_string.includes('0,0,0,0')) {
      console.log('dia_string: ', dia_string);
      return 0;
    } else if (dia_string.includes('1,1,1,1')) {
      console.log('dia_string: ', dia_string);
      return 1;
    }
  });
  start_index = [[2,6],[1,6],[0,6],[0,5],[0,4],[0,3]];
  start_index.forEach((item) => {
    let x = item[0];
    let y = item[1];
    let dia_string = '';
    for (; x < num_of_row && y >= 0; x++, y--) {
      dia_string += (dot_colors[x][y].toString()+',')
    }
    if (dia_string.includes('0,0,0,0')) {
      console.log('dia_string: ', dia_string);
      return 0;
    } else if (dia_string.includes('1,1,1,1')) {
      console.log('dia_string: ', dia_string);
      return 1;
    }
  });
  return -1;
}

var usr = 0;
var usr_color = ["#4287f5", "#f58a42"];
function drop() {
  index = $('.dot').index(this);
  col = index%dot_in_row;
  row = Math.floor(index/dot_in_row);
  if (columns[col] < 0) {
    return;
  }
  new_index = columns[col]*dot_in_row+col;
  console.log(col, row);
  console.log(new_index);
  $('.dot').eq(new_index).css('background-color', usr_color[usr]);
  dot_colors[columns[col]][col] = usr;
  var win = [check_row(), check_col(), check_dia()]
  if (win.indexOf(0) > -1) {
    $('h3').text(user0 + " win!");
    return;
  } else if (win.indexOf(1) > -1) {
    $('h3').text(user1 + " win!");
    return;
  }
  usr = 1 - usr;
  columns[col] -= 1;
  $('h3').text(user_list[usr] + rule_string)
  // console.log(dot_colors);
}

$('.dot').on('click', drop)
