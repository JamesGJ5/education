// const btn = document.querySelector('#btn');
// // btn.onclick = () => alert("Hello World!");

// // btn.addEventListener('click', () => {
// //     alert("Hello World");
// // });

// // function alertFunction() {
// //     alert("Hello World");
// // };

// // btn.addEventListener('click', alertFunction);

// btn.addEventListener('click', function (e) {
//     console.log(e.target);
//     e.target.style.background = 'blue';
// });

const buttonNodelist = document.querySelectorAll('button');

buttonNodelist.forEach((button) => {
    button.addEventListener('click', () => {
        alert(button.id);
    });
});