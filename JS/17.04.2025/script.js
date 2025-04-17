// a = 5
// let b = 67
// var c = 23

// name = prompt("введите имя :");
// alert("Привет " + name);

// function foo() {
//   console.log("2");
// }

// console.log("1");
// for (let i = 2; i < 4; i++) {
//   console.log(i);
// }

elNum = document.getElementsByClassName("num")[0];
console.log(elNum.textContent);

function up() {
  elNum.textContent++;
}
function down() {
  elNum.textContent--;
}

let a = 332904802394034820439832084n;
let b = 234324235423n + a;
console.log(b);
console.log(typeof a);
console.log(Math.floor(Math.random() * 2));

count = 0;
for (let i = 0; i < 10; i++) {
  numC = Math.floor(Math.random() * 2);
  numP = confirm("единица или ноль");
  if (numC == 1 && numP) {
    alert("угадал");
    count++;
  } else if (numC == 0 && !numP) {
    alert("угадал");
    count++;
  } else {
    alert("не угадал");
  }
}
alert(count + "раз угадал");
// name = prompt("введите имя", ["безымянный"]);
// alert(name);
// age = confirm("вилкой в глаз?");
// sport = confirm("спорт требует жертв?");
// mama = confirm("за маму и двор стреляю в упор?");
// if (age && sport && mama) {
//   alert("красава братуха жиесть");
// } else {
//   alert("доступ запрещен");
// }
