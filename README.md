# IEOR 4501 Tools For Analytics -- Project  

## Project Description
This project is to write a library for option value prediction propose:
- Create functions for option pricing by using 
    - Monte Carlo simulation   
      The method is to generate 'n' times simulation of the underlying assets' path (in this case are stocks value) in daily basis with each simulation has same input variables but one independent random varibale. Then put the value of each simalation into the option payoff formula. After repeately doing the simulations and get the payoff values for, preferable, thousands of times, we take the mean of all the simulated payoff values and get the option price.
    
    - Binomial option pricing model (Cox, Ross and Rubinstein, CRR Model)   
    The model is an options valuation pricing method. It uses an iterative procedure, allowing for the specification of nodes, or points in time, during the time span between the valuation date and the option's expiration date. The model reduces possibilities of price changes, and removes the possibility for arbitrage. A simplified example of CRR model is in form of a binomial tree.

    - Black Scholes Formula with sensitivity analysis 
        Black Scholes Formula (BS Model) is a close-form formula to to calculate option prices given parameter which are current stock price, option strike price, stock's volatility, option time to maturity, risk-free interest rate, assuming that stock price movement follows lognormal distribution. This also model allow us to do a sensitivity for the option price by varying each parameters and see its effect to the option price.
    
    - Functions to gather stock data from public sources e.g. yahoo-finance or by doing real time web scarping on financial websites and use statistics package to sample necessary data for the simulations and formula mentioned.
    
    - Visualizations of all the methods are also presented to make users better understand the process and for further analysis. 
  
  The aim is to use real-time stock price data and financial models to predict European option value, and compare the results across different methods.


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
Parameters:   

    stock_name: Name of underlying asset that user want to calculate it's option price. Stock name are all stocks available from yahoo-finance
    strike_price: User input value base on strike price (excercise price) on the option.
    ttm: time to maturity of the option
    option_type: Default value is 'Call' for call option, can also be set to 'Put' for put option
    visualization: Default value is 'Ture', which means a graph will also show
    MC_simulations: Times of Monte Carlo Simulations

**Jupyter notebook**
   **Remarks: Current stock price, stock volatility, and risk-free interest rate are automatically calculated by get latest stock price data from yahoo-finance, 10-year average stock volatility, and latest 10-year treasaury bond interest rate scrapped from US-Tresuary website as risk-free interest rate.**
    
_BS_: This part will get the option price for both Call and Put option from the parameters given. This also give sensitivity factors of stock price to each factor e.g. Delta is volatility of option price to stock price and return all results in dataframe for both Call and Put option. Graphs for changes of option price due to each factor are also presented from this method.  
For example
    O = OptionPricing(stock_name, strike_price, ttm)
    O.BS_model()
    
    O = OptionPricing('AAPL', 170, 1)
    O.BS_model()
    
    Result:
   	           Call	    Put
      Price	24.888208	11.267450
      Delta	0.670278	-0.329722
      Gamma	0.008038	0.008038
      Vega	64.650657	64.650657
      Theta	-11.006388	-6.041115
      Rho	94.810044	-70.149200

![BS](https://github.com/EatWellSleepWell2018Fall/ToolsPorject/blob/master/images/BS.png)   

_Monte Carlo Simulation_: In this part, I predict option prices based on Monte Carlo model. Provide a function stock_time() drawing graph of stock price movement during time. Another function simulations_converge() drawing graph to show how the prediction converges to a fixed value when simulations times increase.
For example
    
    O = OptionPricing(stock_name, strike_price, ttm)
    O.Monte_Carlo_option()
    
    O = OptionPricing('AAPL', 170, 1)
    O.Monte_Carlo_option()
    
    Result:
    23.89030359110339

![Monte Carlo1](https://github.com/EatWellSleepWell2018Fall/ToolsPorject/blob/master/images/simulation1.png)
![Monte Carlo2](https://github.com/EatWellSleepWell2018Fall/ToolsPorject/blob/master/images/simulation2.png) 

_CRR Model_: In this part, we write a function to calculate the stock price and decide the option price both in the future. Then considering the distribution the option price follows and the probability of the fluctuation. We also provide options to draw option value figures or not.
    
    O = OptionPricing(stock_name, strike_price, ttm)
    O.BinomialTreeCRR()
    
    For example:
    O = OptionPricing('AAPL', 170, 1)
    O.BinomialTreeCRR()
    Result:
    25.24934795132345

![CRR](https://github.com/EatWellSleepWell2018Fall/ToolsPorject/blob/master/images/crr-call.png)

**Locally**   
_BS Model_:

    python3 OptionPricing.py
    BS stock_name strike_price ttm [optional]option_type
    
    Example:
    python3 OptionPricing.py
    BS AAPL 170 1

_Monte Carlo Simulation_:    

    python3 OptionPricing.py
    MC stock_name strike_price ttm [optional]option_type
    
    Example:
    python3 OptionPricing.py
    MC AAPL 170 1
    
_CRR Model_:   
    
    python3 OptionPricing.py
    BS stock_name strike_price ttm [optional]option_type
    
    Example:
    python3 OptionPricing.py
    CRR AAPL 170 1
