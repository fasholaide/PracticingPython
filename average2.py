#! /usr/bin/env python3
def sort(listed):
	outercount = 1
	while outercount < len(listed):
		temp = listed[outercount]
		innercount = outercount - 1
		while innercount >= 0 and temp < listed[innercount]:
			listed[innercount + 1] = listed[innercount]
			innercount -= 1
		listed[innercount + 1] = temp
		outercount += 1
	return listed

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
		print("The sorted numbers are: ", sort(numbers))
		median = 0
		if len(numbers) % 2 != 0:
			median = sort(numbers)[int(len(numbers)/2)]
		else:
			median = (sort(numbers)[int(len(numbers)/2) - 1] + sort(numbers)[int(len(numbers)/2)])/2
		print("Count = ", count, "Sum = ", total, "Lowest =", low, "Mean = ", total/count, "Highest = ", high, "Median = ", median)
		break
