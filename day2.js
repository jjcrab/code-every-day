//Challenge 1: countTheBits
//Prompt:
// Write a function called countTheBits that accepts a single numeric argument that will be an integer.
// The function should return the number of bits set to 1 in the number's binary representation.
// Hints:
// We typically work with "decimal" numbers daily. Decimal is "base 10", where there are 10 digits available - 0 thru 9. However, it's binary that computers understand - 1's and 0's. The 1's and 0's are called bits.
// As an example, the decimal value of 13 is represented in binary as 1101. There are 3 one bits and 1 zero bit in the decimal number of 13.
// Carefully read the documentation for the Number.prototype.toString method.
// Examples:
// countTheBits( 0 ) // => 0
// countTheBits( 13 ) // => 3
// countTheBits( 256 ) // => 1
// countTheBits( 255 ) //=> 8
// countTheBits( 65535 ) //=> 16

function countTheBits(num) {
	const biNum = num.toString(2);
	let count = 0;
	for (i = 0; i < biNum.length; i++) {
		if (biNum[i] == 1) {
			count += 1;
		}
	}
	return count;
}
console.log(countTheBits(13)); // => 3

// Prompt:
// Write a function called addChecker that accepts two arguments.
// The first argument is an array containing at least two integers. The integers in the array have been pre-sorted in ascending order.
// The second argument is an integer.
// The addChecker function should return true if there are two integers in the array of integers (first argument) that, when added together, equals the integer passed in as the second argument.
// If there are no two integers in the array with a sum equal to the second argument, addChecker should return false.
// Hint:
// An efficient solution can leverage the fact that the integers in the array come sorted for you.
// Examples:

// addChecker( [1, 2], 3 ) // => true
// addChecker( [-3, 2], 9 ) // => false
// addChecker( [10, 15, 16, 22], 32 ) // => true
// addChecker( [10, 15, 16, 22], 19 ) // => false

function addChecker(arr, int) {
	let sum = null;
	for (let i = 0; i < arr.length; i++) {
		sum += arr[i];
	}
	let result = null;
	if ((sum = int)) {
		result = 'true';
	} else {
		result = 'false';
	}
	return result;
}
