# IEOR 4501 Tools For Analytics -- Porject  

## Project Description
[TO DO]  
This project is to write a library for option value prediction propose:
- Create functions for option pricing by using 
    - Monte Carlo simulation 
    The method is to generate 'n' times simulation of the underlying assets' path (in this case are stocks) in daily basis with each simulation has same input variables but one independent random varibale. Then put the value of each simalation into the option payoff formula. After repeately doing the simulations and get the payoff values for, preferable, thousands of times, we take the mean of all the simulated payoff values and get the option price.
    
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
    git clone https://github.com/EatWellSleepWell2018Fall/ToolsPorject.git
    cd ToolsProject
    pip install -r requirements.txt

## Run Instructions
[TO DO] 
    CRR: [In this part, we write a function to calculate the stock price and decide the option price both in the future. Then considering the distribution the option price follows and the probability of the fluation] 
