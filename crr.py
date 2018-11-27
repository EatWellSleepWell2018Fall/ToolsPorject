from math import *
import numpy as np
import matplotlib.pyplot as plt 

# resource: https://en.wikipedia.org/wiki/Binomial_options_pricing_model
def BinomialTreeCRR(T, S, K, r, sigma, n, option_type='C'):
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
	p = exp(-r*T/n) * ((exp(r*T/n) - d) / (u - d))
	p1 = exp(-r*T/n) * (1 - p)

	# initial values at time T
	ValueFlow = [max(K - S * (u ** (2*i-n)), 0) for i in range(n)]
	callValueFlow = [max((S * u ** (2*i-n) - K), 0) for i in range(n)]

	# trace back to time 0
	# for time in reversed(range(n)):
	# 	exercise = [K - S * (u ** (2*i-time)) for i in range(time)]
	# 	ValueFlow = [p * ValueFlow[i+1] + p1 * ValueFlow[i] for i in range(time)]
	# 	callValueFlow = [p * callValueFlow[i+1] + p1 * callValueFlow[i] for i in range(time)]
	# 	# print (ValueFlow)
	# 	# print ('----')
	# 	ValueFlow = [max(exercise[i], ValueFlow[i]) for i in range(len(ValueFlow))]
	# 	callValueFlow = [max(exercise[i], callValueFlow[i]) for i in range(len(callValueFlow))]
	# 	# print (ValueFlow)
	# 	# print ('----')
	# 	if len(callValueFlow) == 1:
	# 		break

	# print (callValueFlow)
	# print ('call: %f' % callValueFlow[0])
	# print (ValueFlow)
	# print ('put: %f' % ValueFlow[0])

	## In matrix
	# Resource: http://www.quantandfinancial.com/search/label/Binomial%20Tree
	stockValue = np.zeros((n+1,n+1))
	stockValue[0,0] = S
	for i in range(1,n+1):
		stockValue[i,0] = stockValue[i-1,0] * u
		for j in range(1,i+1):
			stockValue[i,j] = stockValue[i-1,j-1] * d

	optionValue = np.zeros((n+1,n+1))
	for i in range(n+1):
		if option_type == 'C': # Call Option
			optionValue[n,i] = max(stockValue[n,i]-K, 0)
		elif option_type == 'P': # Put Option
			optionValue[n,i] == max(K-stockValue[n,i], 0)

	# backtracking
	for i in range(n-1,-1,-1):
		for j in range(i+1):
			if option_type == 'C':
				optionValue[i,j] = max(stockValue[i,j]-K, 0, p*optionValue[i+1,j]+p1*optionValue[i+1,j+1])
			elif option_type == 'P':
				optionValue[i,j] = max(K-stockValue[i,j], 0, p*optionValue[i+1,j]+p1*optionValue[i+1,j+1])

	# print (optionValue[0,0])
	return optionValue[0,0]

T = 1 
S = 100
K = 100
r = 0.03
sigma = 0.1
n = 10

y = [-BinomialTreeCRR(T,S,K,r,sigma,n,'C')] * K
y += [x - BinomialTreeCRR(T,S,K,r,sigma,n,'C') for x in range(K)] 

plt.plot(range(2*K), y)
plt.axis([0, 2*K, min(y) - 10, max(y) + 10])
plt.xlabel('Asset price')
plt.ylabel('Profits')
plt.axvline(x=K, linestyle='--', color='black')
plt.axhline(y=0, linestyle=':', color='black')
plt.title('Call Option')
plt.text(100, 0, 'K')
plt.show()

z = [-x + K - BinomialTreeCRR(T,S,K,r,sigma,n,'P') for x in range(K)] 
z += [-BinomialTreeCRR(T,S,K,r,sigma,n,'P')] * (K)

plt.plot(range(2*K), z, color='red')
plt.axis([0, 2*K, min(y) - 10, max(y) + 10])
plt.xlabel('Asset price')
plt.ylabel('Profits')
plt.axvline(x=K, linestyle='--', color='black')
plt.axhline(y=0, linestyle=':', color='black')
plt.title('Put Option')
plt.text(100, 0, 'K')
plt.show()
# BinomialTreeCRR(1,100,100,0.03,0.1,10,'C')
