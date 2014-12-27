#! /usr/bin/env python3

import random
import sys

articles = ["the", "a", "an"]
subjects = ["cat", "dog", "woman", "man", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "is" ,"are", "dash", "walk"]
adverbs = ["loudly", "quietly", "rapidly", "well", "badly"]
try:
	count = 5
	if 1 < len(sys.argv) <= 2:
		count = int(sys.argv[1])
	line = ""
	while count > 0:
		article = random.choice(articles)
		subject = random.choice(subjects)
		verb = random.choice(verbs)
		adverb = random.choice(adverbs)
		decide = random.randint(1, 2)
	
		if decide == 1:
			line = article + " " + subject + " " + verb + " " + adverb
		else:
			line = article + " " + subject + " " + verb
		print(line)
		count-=1
	print("\n")
except ValueError as err:
	print(err)
except IndexError as err:
	print(err)
