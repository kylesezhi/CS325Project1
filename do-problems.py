#!/usr/bin/env python

import ast
import enumeration
# import better_enumeration
# import divide_and_conquer
# import linear_time # Steven

def readProblems():
	problems = []
	# with open("MSS_TestProblems-1.txt") as f:
	with open("MSS_Problems.txt") as f:
		for line in f:
			# print line
			if len(line) > 2: # skip empty strings
				problems.append(ast.literal_eval(line))
	return problems
	
def solveProblems(problems, function):
	with open("MSS_Results.txt",'a') as f: # append to the results file
		for problem in problems:
			answers = enumeration.enumeration(problem)
			for answer in answers:
				f.write(str(answer) + '\n')

problems = readProblems()
open("MSS_Results.txt", 'w').close() # zero out the results file
solveProblems(problems, enumeration.enumeration)
# solveProblems(problems, better_enumeration.better_enumeration)
# solveProblems(problems, divide_and_conquer.divide_and_conquer)
# solveProblems(problems, linear_time.linear_time)