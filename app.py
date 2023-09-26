#! /usr/bin/python3

import argparse

import mmind

if __name__ == '__main__':

	parser = argparse.ArgumentParser(
		prog = 'MMind Game CLI'
		)

	group = parser.add_mutually_exclusive_group()

	group.add_argument(
		'-s',
		'--letters-set',
		default = "qwerasdf",
		type = str,
		help = "input the set of letters you can type (default: %(default)s)"
		)

	group.add_argument(
		'-m',
		'--max-guesses',
		default = 10,
		type = int,
		help = "set guesses limit (default: %(default)s)"
		)

	group.add_argument(
		'-l',
		'--guess-length',
		default = 4,
		type = int,
		help = "set guess length (default: %(default)s)"
		)

	args = parser.parse_args()

	mmind.play( args.letters_set, args.guess_length, args.max_guesses )
