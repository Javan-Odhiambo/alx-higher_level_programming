#!/usr/bin/python3
""""Read file module that serves the function read_file"""
def read_file(filename=""):
	"""Reads a given text file and prints it's content to the stdout

	Args:
		filename (str, optional): name of the file to be read.
	"""
	if filename:
		with open(filename, 'r', encoding="utf-8") as f:
			for line in f.readlines():
				print(line, end="")
