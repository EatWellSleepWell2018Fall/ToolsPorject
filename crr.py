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
	p = (u- exp(-r*T/n)) / (u**2 - 1)
	p1 = exp(-r*T/n) - p

	# initial values at time T
	ValueFlow = [max(K - S * (u ** (2*i-n)), 0) for i in range(n)]
	callValueFlow = [max((S * u ** (2*i-n) - K), 0) for i in range(n)]

	# trace back to time 0
	for time in reversed(range(n)):
		PutExercise = [K - S * (u ** (2*i-time)) for i in range(time)]
		CallExercise = [S * (u ** (2*i-time)) - K for i in range(time)]
		ValueFlow = [p * ValueFlow[i+1] + p1 * ValueFlow[i] for i in range(time)]
		callValueFlow = [p * callValueFlow[i+1] + p1 * callValueFlow[i] for i in range(time)]
		# print (ValueFlow)
		# print ('----')
		ValueFlow = [max(PutExercise[i], ValueFlow[i]) for i in range(len(ValueFlow))]
		callValueFlow = [max(CallExercise[i], callValueFlow[i]) for i in range(len(callValueFlow))]
		# print (ValueFlow)
		# print ('----')
		if len(callValueFlow) == 1:
			break

	# print (callValueFlow)
	print ('call: %f' % callValueFlow[0])
	# print (ValueFlow)
	print ('put: %f' % ValueFlow[0])


BinomialTreeCRR(1,100,100,0.03,0.1,10)
