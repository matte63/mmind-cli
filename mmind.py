import os
import random

import aux

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
			print(f"Check: {aux.check(sequence.upper(), guess.upper(), black, white).upper()}")
			guesses_left += -1
		else:
			print("You did it!")
			return

	print("You lost.")
	print(f"The sequence was: {sequence}")

