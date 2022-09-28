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