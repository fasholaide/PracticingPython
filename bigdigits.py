#! /usr/bin/env python3
import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
	digits = sys.argv[1]
	row = 0
	while row < 7:
		column = 0
		line = ""
		while column < len(digits):
			number = int(digits[column])
			digit = Digits[number]
			newline = ""
			tmpline = digit[row]
			for i in tmpline:
				if i == '*':
					newline += str(number)
				else:
					newline += i
			line += newline + "  "
			column += 1
		print(line)
		row += 1
except IndexError as err:
	print("Usage: bigdigits.py <number>")
except ValueError as err:
	print(err, "in", digits)
