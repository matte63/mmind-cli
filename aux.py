
def find(string, ch):
	return [i for i, c in enumerate(string) if c == ch]

def check(string, guess, black='b', white='w'):

	matches = ''
	res = ''

	for ch in guess:



		fg = find(guess, ch)
		fs = find(string, ch)

		if fs:

			if ch not in matches:

				if fg == fs:
					res += black * min(len(fg), len(fs))

				else:
					res_b = ''
					res_w = ''

					for i in fg:

						if i in fs:
							res_b += black
						else:
							res_w += white

					res += res_b + white * min(len(fs) - len(res_b), len(res_w))

			matches += ch


	return ''.join(sorted(res))




# DEBUG

# sequence = "asdd"

# guesses = ["sadd", "ffff", "asdd", "ddsa", "fafs", "ssss", "faas", "aaas", "daff", "adff", "dasd", "adsd"]
# control = ["bbww", "",     "bbbb", "wwww", "ww",   "b",    "ww",   "bw",   "ww",   "bw",   "bwww", "bbww"]

# print('\t'.join([sequence for i in guesses]))
# print('\t'.join(guesses))
# print('\t'.join(control))
# print('\t'.join([check(sequence, guess) for guess in guesses]))

# print(check(sequence, guesses[5]))

