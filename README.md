# IEOR 4501 Tools For Analytics -- Project  

## Project Description
[TO DO]  
This project is to write a library for option value prediction propose:
- Create functions for option pricing by using 
    - Monte Carlo simulation   
      The method is to generate 'n' times simulation of the underlying assets' path (in this case are stocks) in daily basis with each simulation has same input variables but one independent random varibale. Then put the value of each simalation into the option payoff formula. After repeately doing the simulations and get the payoff values for, preferable, thousands of times, we take the mean of all the simulated payoff values and get the option price.
      Visualization of the stock prices movement and simulation process are also provided.
    
    - Binomial option pricing model (Cox, Ross and Rubinstein, CRR Model)   
    The model is to an options valuation method. It uses an iterative procedure, allowing for the specification of nodes, or points in time, during the time span between the valuation date and the option's expiration date. The model reduces possibilities of price changes, and removes the possibility for arbitrage. A simplified example of CRR model is in form of a binomial tree.

    - Black Scholes Formula with sensitivity analysis     
    
    - Functions to gather stock data from public sources e.g. yahoo-finance or by doing real time web scarping on financial websites and use statistics package to sample necessary data for the simulations and formula mentioned.
    
    - Visualizations of all the methods are also presented to make users better understand the process and for further analysis. 
  
  The aim is to use financial data and models to predict European option value and compare the result across different methods.


## Group Name: EatWellSleepWell (Section 2)
#### Group Members: 
    Varoon Kitayaporn
    Aries Li
    Chenxuerui Li
    Xiaosu Qi   

## Installation Instructions 
To run in jupyter notebook:   

    open jupyter notebook
      
To run locally:   

    git clone https://github.com/EatWellSleepWell2018Fall/ToolsPorject.git
    cd ToolsProject
    pip install -r requirements.txt

## Run Instructions
[TO DO]    
Parameters:   

    stock_name: 
    strike_price:
    ttm: time to maturity
    option_type: default value is 'Call' for call option, can also be set to 'Put' for put option
    visualization: default value is 'Ture', which means a graph will also show
    MC_simulations: Times of Monte Carlo Simulations

**Jupyter notebook**    
_BS_:    
_Monte Carlo Simulation_: In this part, I predict option prices based on Monte Carlo model. Provide a function stock_time() drawing graph of stock price movement during time. Another function simulations_converge() drawing graph to show how the prediction converges to a fixed value when simulations times increase.
For example
    
    stock_time(S,K,r,v,T)
    stock_time(857.29,860,0.0014,0.2076,1/20)
   
    mc_euro_options(option_type,S,K,T,r,v,simulations)
    mc_euro_options('Call',857.29,860,1/20,0.0014,0.2076,10000)
    
    simulations_converge(option_type,S,K,T,r,v,simulations)
    simulations_converge('Call',857.26,860,1/20,0.00140.2076,10000)


_CRR_: In this part, we write a function to calculate the stock price and decide the option price both in the future. Then considering the distribution the option price follows and the probability of the fluation
    
    O = OptionPricing(stock_name, strike_price, ttm)
    O.BinomialTreeCRR()
    
    For example:
    O = OptionPricing('AAPL', 170, 1)
    O.BinomialTreeCRR()
    
**Locally**   
_BS_:    
_Monte Carlo Simulation_:    
_CRR_:   
