//cohort interview code challenge
function result(arr, n) {
	for (let i = 0; i < arr.length; i++) {
		for (let j = i + 1; j < arr.length; j++) {
			let sum = arr[i] + arr[j];
			if (sum == n) {
				return [i, j];
			}
		}
	}
	return [-1, -1];
}

console.log(result([1, 9, 10], 8));
