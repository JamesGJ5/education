// function Book(title, author, pages, read) {
//     this.title = title;
//     this.author = author;
//     this.pages = pages;
//     this.read = read;
//     // this.info = function() {
//     //     x = (this.read === true) ? "read already" : "not read yet";
//     //     statement = `${this.title} by ${this.author}, ${this.pages} pages, ${x}`;
//     //     return statement;
//     // };
// }

// Book.prototype.info = function() {
//     x = (this.read === true) ? "read already" : "not read yet";
//     statement = `${this.title} by ${this.author}, ${this.pages} pages, ${x}`;
//     return statement;
// };

// const theHobbit = new Book("The Hobbit", "J.R.R. Tolkien", 295, false);
// console.log(theHobbit.info());

// "If we declare the function directly in the constructor, like we did when they 
// were first introduced [above], that function would be duplicated every time a new 
// Student is created. In this example, that wouldn’t really matter much, but in 
// a project that is creating thousands of objects, it really can make a 
// difference", so we don't tend to do that. We instead define the function on 
// the prototype.

// Recommended method for prototypal inheritance, according to TOP, is to use 
// Object.create:

// function Student() {
// }

// Student.prototype.sayName = function() {
//   console.log(this.name)
// }

// function EighthGrader(name) {
//   this.name = name
//   this.grade = 8
// }

// EighthGrader.prototype = Object.create(Student.prototype)

// const carl = new EighthGrader("carl")
// carl.sayName() // console.logs "carl"
// carl.grade // 8