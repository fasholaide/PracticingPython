#! /usr/bin/env python3

count = 0
total = 0
low = high = 0
numbers = []
while True:
	try:
		number = int(input("Enter a Number or Enter to finish  "))
		if count == 0:
			low = number
		if number < low:
			low = number
		if number > high:
			high = number
		#numbers += str(number)
		numbers.append(number)
		total += number
		count += 1
		#print("Count = ", count, "Sum = ", sum, "Lowest =", low, "Highest = ", high)
	except ValueError as err:
		print(err)
		continue
	except EOFError as err:
		print("\n")
		print("The numbers are ", numbers)
		print("Count = ", count, "Sum = ", total, "Lowest =", low, "Highest = ", high)
		break
