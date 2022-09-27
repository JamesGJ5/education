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



// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Strings
// Using template literals for string concatenation usually gives you more 
// readable code, for example:

// console.log(`${greeting}, ${name}`)

// versus

// console.log(greeting + ", " + name)


// The Number OBJECT converts anything to a number if it can, while the toString() 
// METHOD converts to string (surprisingly)


// Template literals respect the line breaks in the source code



// https://www.w3schools.com/js/js_string_methods.asp
// Using .replace with the /g flag replaces all matches

// Using .replace with the /i flag replaces case insensitive



// chrome.google.com/webstore/detail/grepper/amaaokahonnfjjemodnpmeenfpnnbkco?hl=en
// == will say that 0 and an empty string are each equal to false

// The === checks the equality without type conversion, so it will differentiate 
// 0 and an empty string from false

// !== (not !=) is analogous of ===, for non-equalities

// null == undefined returns true, but null === undefined returns false;
// conversely, null != undefined returns false, but null !== undefined returns true

// For maths and other operators, null is converted to 0 and undefined to NaN

// null == 0 returns false and null > 0 returns false, but null >= 0 returns true 
// in spite of this--this is because the use of the > operator means null is 
// converted to 0 and then the comparison is done (0 of course == 0), whereas 
// this didn't occur in the case of null == 0

// NaN is a special numeric value which returns false for all comparisons. Therefore, 
// undefined > 0 and undefined < 0 both return false (the > and < cause undefined 
// to be converted to NaN before the comparison)

// the equality check == for undefined and null is defined such that, without any 
// conversions, they equal each other and don’t equal anything else. Therefore, 
// undefined == 0 and null == 0 return false, because 0 is not in the list mentioned 
// (which contains just undefined and null)


// Suggestions:

// 1. Treat any comparison involving undefined/null, except that done by the strict 
// equality === with exceptional care.

// 2. Don’t use comparisons >= > < <= with a variable which may be 
// null/undefined, unless you’re really sure of what you’re doing. If a variable 
// can have these values, check for them separately.



// https://javascript.info/logical-operators
// Precedence of AND (&&) is higher than that of OR (||)


// For readability, it's recommended that one does not use && to replace if, but 
// uses && when necessary


// NOT is !

// !! is sometimes used for converting a value to boolean type--it implements 
// NOT twice

// The precedence of NOT is higher than all other logical operators (including 
// AND and OR)



// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals
// Any value that is not false, undefined, null, 0, NaN, or an empty string ('') 
// actually returns true when tested as a conditional statement



// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions#anonymous_functions_and_arrow_functions
// "We recommend that you use arrow functions, as they can make your code shorter 
// and more readable."


// The same scoping rules regarding functions (discussed in the current webpage) 
// don't apply to loops and conditional blocks in JS



// https://javascript.info/function-basics
// A parameter of a function is a declaration-time variable, while an argument 
// passed to a function (to a specific parameter, for example) is a call-time 
// term


// If a function is called, but an argument is not provided, then the 
// corresponding value becomes undefined.


// See current webpage for common function prefixes (show, get, calc, create and 
// check) and what they commonly mean


// Try to follow the "One function - one action" principle, where one action means 
// one *independent* action, for easy refactoring.


// To make the code clean and easy to understand, it’s recommended to use mainly 
// local variables and parameters in the function, not outer variables.



// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong
// It seems that any declaration of a variable returns undefined, but assigning a variable to a value 
// without any declaration returns the value. Remembering this may be important in preventing 
// bugs.



// https://www.w3schools.com/js/js_arrays.asp
// Best to initialise an array using the array literal method (i.e. const array = [1, 2, 3]) 
// rather than const array = new Array(1, 2, 3)


// Adding elements to an array with high indexes (i.e. indices greater than 
// array.length) can create undefined "holes" in an array (in between the 
// end of the array beforehand and the new end of the array)


// If you accidentally try to use named indexes to access and array element, 
// JavaScript redefines the array to an object. After that, some array methods and 
// properties will produce incorrect results


// In JavaScript, arrays (which are special types of object) use numbered indexes 
// while other objects use named indexes

// Rather than using index equal to current array length to an append an element 
// to the array, I guess it'd be best to just use push()


// typeof <an array> returns "object". To see if a variable points specifically to 
// an array object, use Array.isArray() or the instanceof operator



// https://www.w3schools.com/js/js_array_methods.asp
// Array elements can be deleted using the delete operator but this leaves 
// undefined holes in the array, so you may want to use pop() or shift() instead


// The concat() method does not change the existing arrays. It always returns a 
// new array.


// You can use splice() to remove elements without leaving "holes" in the array


// Note: slice(), unlike splice, does not modify the array on which it is called. 
// It is similar to a typical slice in Python (like y = x[1:5]).


// Printing an array implements what toString() implements before displaying the 
// contents of the array (i.e. comma-separated elements)


// ALL JavaScript objects have a toString() method



// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Looping_code
// The main difference between a do...while loop and a while loop is that the code 
// inside a do...while loop is always executed at least once



// https://javascript.info/while-for
// Labels can help you break out of multiple loops at once