// factorial
function factorial(n) {

    if (n === 0 || n === 1) {
        return 1;
    }
    
    else {
       return n * factorial(n - 1);
    }
}
let num = parseInt(prompt());
let result = factorial(number);
console.log(`The factorial of ${number} is ${result}`);

//FIBONACCI
function fibo(n) {
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    } else {
        return fibo(n - 1) + fibo(n - 2);
    }
}
let number = parseInt(prompt(""));
console.log(`The Fibonacci number at position ${number} is ${result}`);

//sumofseries
function sumOfSeries(n) {
    if (n === 0) {
        return 0;  
    } else {
        return n + sumOfSeries(n - 1);  
    }
}
let numb = parseInt(prompt("Enter a positive integer to calculate the sum of series:"));


    let results = sumOfSeries(number);
    console.log(`The sum of the series from 1 to ${numb} is ${results}`);

//anonymous ascending order
let array = [5, 2, 9, 1, 5, 6];
array.sort(function(a, b) {
    return a - b;
});
console.log("Sorted array in ascending order:", array);

//IIFE 
(function(a, b) {
    let sum = a + b;
    console.log(`The sum of ${a} and ${b} is: ${sum}`);
})(5, 3);  
