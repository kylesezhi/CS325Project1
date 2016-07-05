#!/usr/bin/env python

def linear_time(A):
	subarray = [None] * len(A)
	max_prior = max_current = 0
	for x in A:
		max_prior = max(0, max_current + x)
		if max_current > max_prior:
			subarray[x] = max_current
		max_current = max(max_prior, max_current)

	return [A, subarray, max_current, '']
