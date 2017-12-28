var counter = new Array(9);
for (var number1 = 12 ; number1 <= 98 ; number1++)
{
	for (var number2 = 123 ; number2 <= 987 ; number2++)
	{
		var product = number1 * number2;
		if (product >= 1234 && product <= 9876)
		{
			var allDigits = number1 + "" + number2 + "" + product;
			for (var i = 0 ; i < 9 ; i++)
				counter[i] = 0;
			for (var i = 0 ; i < 9 ; i++)
				counter[allDigits[i] - 1]++;
			var correctCombination = true;
			for (var i = 0 ; i < 9 && correctCombination ; i++)
				if (counter[i] != 1)
					correctCombination = false;
			if (correctCombination)
				console.log(number1 + " * " + number2 + " = " + product);
		}
	}
}
