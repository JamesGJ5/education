// console.log("Hello, World!")


// https://javascript.info/variables

// VARIABLE DECLARATION USING LET
// let message
// message = 'Hello'

// let message = 'Hello'


// CREATING EACH NEW VARIABLE ON A DIFFERENT LINE IS RECOMMENDED
// let user = 'John'
// let age = 25
// let message = 'Hello'

// let user = 'John'
//     age = 25,
//     message = 'Hello'

// let user = 'John'
//     , age = 25
//     , message = 'Hello'


// VAR INSTEAD OF LET IS FOUND IN OLDER SCRIPTS
// var message = 'Hello'


// CAN CHANGE A VARIABLE THAT'S BEEN DEFINED USING LET
// let message
// message = 'Hello!'
// message = 'World!'


// ALIASING
// let hello = 'Hello world!'

// let message
// message = hello

// alert(hello)
// alert(message)

// hello = 'Hello, James!'

// alert(hello)
// alert(message)


// CAN'T DECLARE A VARIABLE TWICE USING LET
// let message = 'This'
// let message = 'That'

// alert(message)


// CAMELCASE IS COMMONLY USED IN JAVASCRIPT
// let userName;


// THE ONE SYMBOLS (I.E. NOT LETTERS OR DIGITS) ALLOWED IN VARIABLE NAMES:
// let $ = 1
// let _ = 2

// alert ($ + _)


// NON-LATIN LETTERS ARE ALLOWED BUT NOT RECOMMENDED

// ASSIGNING A VARIABLE WITHOUT DECLARATION FIRST IS BAD PRACTICE AND CAUSES ERROR IN STRICT MODE:
// HOWEVER, MAY NOT WORK ONCE THE VARIABLE IS ALREADY ASSIGNED, SO PUT AT THE BEGINNING OF SCRIPT IF UNIVERSAL
// num = 5
// alert(num)

// "use strict";
// num = 5
// alert(num)


// UNCHANGING VARIABLE, CAN'T BE REASSIGNED WITHOUT ERROR
// const myBirthday = '18.04.1982'

// myBirthday = '01.01.2001'


// CONSTANTS ARE OFT USED AS ALIASES FOR DIFFICULT-TO-REMEMBER VALUES PRIOR TO 
// EXECUTION, AND CAPITAL LETTERS ARE OFT USED TO IDENTIFY THEM
const COLOR_ORANGE = "#FF7F00"

// let color = COLOR_ORANGE
// alert(color)


// ON THE OTHER HAND, CONSTANTS CALCULATED DURING RUNTIME BUT DO NOT CHANGE AFTER THEIR 
// INITIAL ASSIGNMENT ARE NAMED WITHOUT SOLELY UPPERCASE LETTERS
// const = pageLoadTime = /* calculated during runtime*/


// TASK: WORKING WITH VARIABLES
// let admin
// admin = 'Bob'
// let name
// name = 'John'
// admin = name
// alert(admin)


// TASK: GIVING THE RIGHT NAME
// let ourPlanetName = 'earth'
// let currentUserName = 'John'

// TASK: UPPERCASE CONST
// const BIRTHDAY = '18.04.1982'
// const age = someCode(birthday)



// https://www.w3schools.com/js/js_arithmetic.asp
// INCREMENTATION OPERATORS
// let x = 0
// x++
// alert(x)
// x ++
// alert(x)
// x--
// alert(x)
// x --
// alert(x)


// EXPONENTIATION
// let x = 5
// let z = x ** 3
// alert(z)
// z = Math.pow(x, 5)
// alert(z)


// ORDER OF OPERATIONS
// Follow BODMAS, which is BIDMAS, which is PEMDAS
// Can use parentheses


// UPDATE
// Can use +=, -=, *= and /= like in Python
// let x = 5
// x += 6
// alert(x)
// x -= 6
// alert(x)
// x *= 6
// alert(x)
// x /= 6
// alert(x)


// https://www.w3schools.com/js/js_numbers.asp
// JAVASCRIPT HAS ONLY ONE TYPE OF NUMBER (UNLIKE PYTHON, WHICH HAS FLOAT, INT ETC.)
// let x = 3.14
// let y = 3


// STANDARD FORM
// let x = 123e5
// let y = 123e-5
// alert(x)
// alert(y)


// THE NUMBERS ARE ALWAYS 64-BIT FLOATING POINT (WHICH IS CALLED 'DOUBLE PRECISION')
// SEE THE WEBPAGE FOR MORE DETAILS


// INTEGERS ARE ACCURATE UP TO 15 DIGITS
// THE MAXIMUM NUMBER OF DECIMAL DIGITS IS 17


// FLOATING POINT ARITHMETIC IS NOT ALWAYS 100% ACCURATE, SO YOU MAY WANT TO MULTIPLY IT UP 
// INTO AN INTEGER AND DIVIDE LATER (OR MAYBE FIND A FUNCTION THAT DOES THIS)


// ADDING NUMBER AND STRING LEADS TO STRING CONCATENATION
// let x = 5
// let y = 'hello'
// let z = 6

// alert(x + y)
// alert(y + x)

// alert(x + y + z)
// alert(y + x + z)

// NOTE, THIS IS DIFFERENT TO THE ABOVE TWO, BECAUSE THE OPERATIONS WORK FROM LEFT 
// TO WRITE, ESPECIALLY SINCE THERE'S ONLY ONE TYPE OF OPERATOR (SO NO OPERATOR 
// TAKES SPECIAL PRECEDENCE OVER THE OTHER IN ACCORDANCE WITH PEMDAS)
// alert (x + z + y)


// STRINGS CAN HAVE NUMERIC CONTENT
// JAVASCRIPT WILL TRY TO CONVERT THESE STRINGS TO INTEGERS IN ALL NUMERIC OPERATIONS, 
// EXCEPT WHEN + IS USED (BECAUSE THIS SUGGESTS CONCATENATION)
// let x = "100"
// let y = "10"
// alert(x / y)
// alert(x + y)


// TO FIND OUT IF A VALUE IS NOT A NUMBER
// let x = 100 / 'Apple'
// console.log(isNaN(x))
// console.log(isNaN(100 / '5'))


// NaNs might be concatenated
// alert(NaN + '5')


// TYPE
// alert(typeof NaN)

// INFINITY
// DIVISION BY 0 GENERATES INFINITY OR -INFINITY (DEPENDING ON SIGN OF NUMERATOR)
// alert(typeof Infinity)
// alert(typeof -Infinity)


// ASSIGNMENTS AT https://www.theodinproject.com/lessons/foundations-fundamentals-part-1
// console.log(23 + 97)

// x = 6 + 5 + 4 + 3 + 2 + 1
// console.log(x)

// console.log((4 + 6 + 9) / 77)

// let a = 10
// console.log(a)

let max = 57
actual = max - 13
percentage = actual / max



// https://javascript.info/types
// String in backticks is the same as an f-string in Python


// Explicitly assigning undefined to a variable is not recommended


// The result of typeof null is "object". That’s an officially recognized error in 
// typeof, coming from very early days of JavaScript and kept for compatibility. 
// Definitely, null is not an object. It is a special value with a separate type 
// of its own. The behavior of typeof is wrong here.

// The result of typeof alert is "function", because alert is a function. We’ll 
// study functions in the next chapters where we’ll also see that there’s no 
// special “function” type in JavaScript. Functions belong to the object type. 
// But typeof treats them differently, returning "function". That also comes from 
// the early days of JavaScript. Technically, such behavior isn’t correct, but 
// can be convenient in practice.

// typeof is an operator, not a function.