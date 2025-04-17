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
num = 0;

elNum = document.getElementsByClassName("num")[0];
console.log(elNum.textContent);

function up() {
  elNum.textContent++;
}
function down() {
  elNum.textContent--;
}

console.log(num);
