import numpy as np 
from math import *

# resource: https://en.wikipedia.org/wiki/Binomial_options_pricing_model
def BinomialTreeCRR(T, S, K, r, sigma, n):
	'''
	T: expiration date
	S: stock price
	K: strike price
	r: risk free rate corresponding to the risk of the option
	n: height of the binomial tree
	'''

	# u: up factor, d: down factor
	u = exp(sigma * sqrt(T/n))
	d = 1/u

	# p: Risk-neutral 
	p = (exp(r*T/n) - d) / (u - d)

	# initial values at time T
	ValueFlow = [max(K - (S * (u ** (n-i)) * (d ** i)), 0) for i in range(n+1)]
	callValueFlow = [max((S * (u ** (n-i)) * (d ** i)) - K, 0) for i in range(n+1)]

	# trace back to time 0
	for time in range(n-1,-1,-1):
		EarlyExercise = [max(K - (S * (u ** (n-i)) * (d ** i)), 0) for i in range(n+1)]
		ValueFlow = [((p * ValueFlow[i] + (1-p) * ValueFlow[i+1]) / exp(r*T/n)) for i in range(time+1)]
		ValueFlow = [max(EarlyExercise[i], ValueFlow[i]) for i in range(len(ValueFlow))]

	print ('call: %d' % callValueFlow[0])
	print ('put: %d' % ValueFlow[0])

BinomialTreeCRR(1,100,95,0.03,0.25,300)
