// var student1 = new Object();
// var journal = new Object();
// journal["math"] = 4;
// journal["rus"] = 4;
// journal["lit"] = 4;
// journal["hist"] = 4;
// student1["mark"] = 4.5;
// student1["age"] = 23;
// student1["group"] = "5a";
// student1["journal"] = journal;

// console.log(student1);
// console.log(student1.mark);
// student1.mark = 4.6;
// var student2 = new Object();
// student2["mark"] = 4.0;
// student2["age"] = 21;
// student2["group"] = "5a";
// student2["journal"] = journal;
// console.log(student2);
// var st3 = {};
// // Object.assign(st3, student2);

// console.log(student2);
// console.log(st3);

// let jsonSt1 = JSON.stringify(student1);
// let student3 = JSON.parse(jsonSt1);

// for (let i in student2) {
//   st3[i] = student2[i];
// }

// student2.journal.rus = 5;
// st3.age = 44;
// console.log(st3);
// console.log(student3);

students = [];
students[0] = { name: "Vlad", age: "41", mark: 5 };
students[1] = { name: "Andrey", age: "30", mark: 4.5 };
students[2] = { name: "Maria", age: "25", mark: 4.1 };
students[3] = { name: "Khamid", age: "35", mark: 2.5 };
students[4] = { name: "Robert", age: "21", mark: 3.5 };
console.log(students);

function astolop(ball) {
  for (let i in students) {
    if (students[i].mark >= ball) {
      console.log(students[i]);
    }
  }
}

astolop(5);
function nyashnost() {
  for (let i in students) {
    console.log(
      `${students[i].name}\t| ${students[i].age}\t| ${students[i].mark}`
    );
  }
}
nyashnost();
