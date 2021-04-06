//Day1 https://www.codewars.com/kata/57a77726bb9944d000000b06/train/javascript
function mango(quantity, price) {
	const free = Math.floor(quantity / 3);
	const cost = (quantity - free) * price;
	return cost;
}
