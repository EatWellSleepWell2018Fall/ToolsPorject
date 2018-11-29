
# coding: utf-8

# In[6]:


import datetime
from random import gauss
import math
from math import exp, sqrt

def generate_asset_price(S,v,r,T):
    return S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))

def call_payoff(S_T,K):
    return max(0.0,S_T-K)

S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14%
T = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0
K = 860.
simulations = 5000
payoffs_T = []
discount_factor = math.exp(-r * T)


for i in range(simulations)[1:]:
    payoffs = []
    for time in range(i)[1:]:
        S_T = generate_asset_price(S,v,r,T)
        payoffs.append(call_payoff(S_T, K))
    simulate_price = discount_factor * (sum(payoffs) / i)
    payoffs_T.append(simulate_price)
    


# In[7]:


import matplotlib.pyplot as plt
plt.plot(payoffs_T)
plt.show()


# In[8]:


import numpy as np
from random import gauss
import math
from math import exp, sqrt

#for a certain time T
def mc_euro_options(option_type,S,strike,T,r,v,simulations):
    payoff_sum = 0
    for j in range(simulations):
        st = S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))
        if option_type == 'c':
            payoff = max(0,st-strike)
        elif option_type == 'p':
            payoff = max(0,strike-st)
        payoff_sum += payoff
    price_T = (payoff_sum/float(simulations))*math.exp(-r * T)
    return price_T
mc_euro_options('c',927.96,785,100.0/252,0.01,0.23,500)


# In[9]:


#in a whole year, with 252 trading days
price_path = []
S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14%
K = 860
steps = 252
simulations = 8
time_delta = 1/365
for j in range(simulations):
    price_path = [S]
    St = S
    for t in range(252):
        St = St * exp((r - 0.5 * v**2)* time_delta  + v * sqrt(time_delta) * gauss(0,1.0))
        price_path.append(St)
    plt.plot(price_path)
plt.ylabel('stock price',fontsize=15)
plt.xlabel('steps',fontsize=15)

