import string
import random

strings = list(string.punctuation) + list(string.digits) + list(string.ascii_letters)
try:
	length = int(input("Length > "))

	key = ""

	for s in strings:
		if len(key) < length:
			key += random.choice(strings)

	print(key)
except ValueError:
	print("\nOnly int char.")
except KeyboardInterrupt:
	print("\nExiting.")
except:
	print("\nExiting.")