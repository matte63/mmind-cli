import os
import random



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

def play(letters = "QWERTY", length = 4, total_guesses = 16):

	letters = letters.upper()

	guesses_left = total_guesses

	black = 'B'
	white = 'W'

	sequence = "".join([letters[random.randint(0, len(letters) - 1)] for i in range(length)])

	print(f"Guess correct {length} letter sequence composed with {letters}:")
	print(f"\t\'{black}\' = right letter in right position")
	print(f"\t\'{white}\' = right letter in wrong position")
	print(f"You have {total_guesses} attempts.\nGood luck!")


	# print(f"Correct sequence: {sequence}.")

	while (guesses_left):
		guess = input(f"{total_guesses + 1 - guesses_left}: ")
		if len(guess) != length:
			print(f"Your guess must be {length} letters long.")
		elif guess.upper() != sequence.upper():
			print(f"Check: {check(sequence.upper(), guess.upper(), black, white).upper()}")
			guesses_left += -1
		else:
			print("You did it!")
			return

	print("You lost.")
	print(f"The sequence was: {sequence}")

