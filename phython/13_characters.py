test_str = "GeeksforGeeks"

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))
