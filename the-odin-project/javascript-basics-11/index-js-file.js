const container = document.querySelector('#container');


const content = document.createElement('div');
content.classList.add('content');
content.textContent = 'This is the glorious text-content!';

container.appendChild(content);


const para = document.createElement('p');
para.style.color = 'red'
para.textContent = "Hey, I'm red!";

container.appendChild(para);


const lvl3Heading = document.createElement('h3');
lvl3Heading.style.color = 'blue'
lvl3Heading.textContent = "I'm a blue h3!"

container.appendChild(lvl3Heading)


const div2 = document.createElement('div');
div2.style.border = 'solid black';
div2.style.backgroundColor = 'pink';

const lvl1Heading = document.createElement('h1');
lvl1Heading.textContent = "I'm in a div!"

div2.appendChild(lvl1Heading)

const para2 = document.createElement('p')
para2.textContent = 'ME TOO!'

div2.appendChild(para2)

container.appendChild(div2);