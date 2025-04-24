// let day = prompt("Введи день недели:");
// // if (day == "понедельник") {
// //   alert("пн");
// // } else if (day == "вторник") {
// //   alert("вт");
// // } else if (day == "среда") {
// //   alert("ср");
// // } else if (day == "четверг") {
// //   alert("чт");
// // } else if (day == "пятница") {
// //   alert("пт");
// // } else if (day == "суббота") {
// //   alert("сб");
// // } else if (day == "воскресенье") {
// //   alert("вс");
// // } else {
// //   alert("ошибка ввода");
// // }

// switch (day) {
//   case "понедельник":
//     alert("пн");
//     break;
//   case "вторник":
//     alert("вт");
//     break;
//   case "среда":
//     alert("ср");
//     break;
//   case "четверг":
//     alert("чт");
//     break;
//   case "пятница":
//     alert("пт");
//     break;
//   case "суббота":
//     alert("сб");
//     break;
//   case "воскресенье":
//     alert("вс");
//     break;
//   default:
//     alert("некоректные данные");
// }

// let age = +prompt("введи возраст");
// if (age > 0 && age < 120) {
//   alert("корректно");
// } else {
//   alert("ЭЛЬФ!");
// }

// let hou = +prompt("введи часы");
// let min = +prompt("введи минуты");
// let seс = +prompt("введи секунды");
// if (hou < 0 || hou >= 24) {
//   alert("неправельно введены часы");
// }
// if (min < 0 || min >= 60) {
//   alert("неправельно введены минуты");
// }
// if (sec < 0 || sec >= 60) {
//   alert("неправельно введены секунды");
// }

// let x = +prompt("введи значение по оси Х");
// let y = +prompt("введи значение по оси Y");

// if (x > 0 && y > 0) {
//   alert("первая четверть");
// } else if (x < 0 && y > 0) {
//   alert("вторая четверть");
// } else if (x < 0 && y < 0) {
//   alert("третья четверть");
// } else if (x > 0 && y < 0) {
//   alert("четвертая четверть");
// } else {
//   alert("на оси координат");
// }

// let num1 = +prompt("введи первое число");
// let num2 = +prompt("введи второе число");
// let flag = true;
// if (num1 > num2) {
//   flag = false;
// }
// alert(flag ? "второе больше или равно первому" : "первое больше");

// let num1 = +prompt("введи первое число");
// let num2 = +prompt("введи второе число");
// let calc = prompt("введи действие: + - * /");

// switch (calc) {
//   case "+":
//     alert(num1 + num2);
//     break;
//   case "-":
//     alert(num1 - num2);
//     break;
//   case "*":
//     alert(num1 * num2);
//     break;
//   case "/":
//     alert(num1 / num2);
//     break;
//   default:
//     alert("некорректные данные");
// }
// let count = 0;
// while (count < 10) {
//   console.log(++count);
// }

// let count = 0;
// do {
//   let num = +prompt("введи число");
//   count++;
// } while (num != 0);
// console.log(count);

// let num = +prompt("сколько раз вывести?");
// let count = 0;
// while (count < num) {
//   console.log("#");
//   count++;
// }

// let num = +prompt("введи положительное число");
// while (num >= 0) {
//   console.log(num--);
// }

// let num = +prompt("введи число");
// let n = +prompt("введи степень");
// let res = 1;
// while (n > 0) {
//   res *= num;
//   n--;
// }
// alert(res);

// let num1 = +prompt("введи первое число");
// let num2 = +prompt("введи второе число");

// if (num2 >= num1) {
//   n = num1;
// } else {
//   n = num2;
// }
// while (n > 0) {
//   if (!(num1 % n) && !(num2 % n)) console.log(n);
//   n--;
// }

// let num = +prompt("введи число");
// result = 1;

// while (num > 0) {
//   result *= num;
//   num--;
// }
// alert(result);

// let result;
// do {
//   result = +prompt("2+2*2=");
// } while (result != 6);

// alert("верно");

// let n = +prompt("введи число  больше 50:");
// let count = 0;
// do {
//   n /= 2;
//   count++;
// } while (n >= 50);
// alert(n + " " + count);

let num1 = +prompt("введи мин число");
let num2 = +prompt("введи макс число");

for (let i = num1 + 4; i < num2; i += 4) {
  console.log(i);
}
