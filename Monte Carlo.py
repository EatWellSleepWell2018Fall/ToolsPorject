
# coding: utf-8

# In[1]:


def mc_euro_options(option_type,S,K,T,r,v,simulations):
    
    #option_type:'c'-call, 'p'-put
    #S :underlying price
    #K: strike price
    #r: risk free interest rate to discount by
    #v: volatility of the stock
    #simulations: time of simulations
    
    
    from random import gauss
    import math
    from math import exp, sqrt
    
    payoff_sum = 0
    
    for j in range(simulations):
        st = S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))
        if option_type == 'c':
            payoff = max(0,st-K)
        elif option_type == 'p':
            payoff = max(0,K-st)
        payoff_sum += payoff
    price_T = (payoff_sum/float(simulations))*exp(-r * T)
    return price_T
    
    
    


# In[17]:


def simulations_converge(option_type,S,K,T,r,v,simulations):
    
    import matplotlib.pyplot as plt
    
    
    simulation_path = []
    for simulation in range(simulations)[1:]:
        price_T_simulation = mc_euro_options(option_type,S,K,T,r,v,simulation)
        simulation_path.append(price_T_simulation)
        
    plt.plot(simulation_path)
    
    plt.xlabel('simulation times')
    plt.ylabel('option price')
    plt.show()
        


# In[12]:


def stock_time(S,K,r,v,simulations,steps,T):
    
    from random import gauss
    import math
    from math import exp, sqrt
    import matplotlib.pyplot as plt
    
    time_delta = T/252
    
    for j in range(simulations):
        price_path = [S]
        St = S
        for t in range(steps):
            St = St * exp((r - 0.5 * v**2)* time_delta  + v * sqrt(time_delta) * gauss(0,1.0))
            price_path.append(St)
         
        plt.plot(price_path)
        
    plt.ylabel('stock price',fontsize=15)
    plt.xlabel('steps',fontsize=15)
    
    plt.show()


# In[15]:


S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14%
K = 860
simulations = 8
T = 1/12
stock_time(S,K,r,v,T,simulations)


# In[18]:


S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14%
K = 860
T = 60/365
option_type = 'c'
simulations = 9000
simulations_converge(option_type,S,K,T,r,v,simulations)


# In[19]:


S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14%
K = 860
T = 60/365
option_type = 'c'
simulations = 9000
mc_euro_options(option_type,S,K,T,r,v,simulations)

