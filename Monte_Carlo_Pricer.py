# -*- coding: utf-8 -*-
"""
@author: William J. Trenberth
Implementing a Monte-Carlo option pricing approach for exotic options.
"""
# barrier option question on stackexchange
# https://quant.stackexchange.com/questions/22621/barrier-option-monte-carlo-simulation
import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt 

def main():
    
    r = 0.05    #The interest rate
    s_0 = 1     #The inital stock price
    drift = 0.1   #The drift, \mu, of the stock
    volatility = 0.2    #The volatility, \sigma, of the stock
    
    dt = 1/365  #The time discretization of the financial model  
    n_mat = 365 #time periods until maturity
    
    #The option parameters
    strike_price = 1.1
    upper_barrier = 1.3
    lower_barrier = 0.95
    
    model = Black_Scholes_Model(dt, r, s_0, drift, volatility)
    
    euro_stock_option = European_call_option(model, n_mat, strike_price)
    asian_stock_option = Asian_call_option(model, n_mat, strike_price)
    up_and_out_stock_option = up_and_out_call_option(model, n_mat, strike_price, upper_barrier)
    down_and_out_stock_option = down_and_out_call_option(model, n_mat, strike_price, lower_barrier)
    double_barrier_out_stock_option = double_barrier_out_call_option(model, n_mat, strike_price, upper_barrier, lower_barrier)
    lookback_option = lookback_European_call_option(model, n_mat, strike_price)
    
    Num_trials = 10000
    
    
    price_1, error_1 = euro_stock_option.Monte_Carlo_pricer(Num_trials)
    price_2, error_2 = asian_stock_option.Monte_Carlo_pricer(Num_trials)
    price_3, error_3 = up_and_out_stock_option.Monte_Carlo_pricer(Num_trials)
    price_4, error_4 = down_and_out_stock_option.Monte_Carlo_pricer(Num_trials)
    price_5, error_5 = double_barrier_out_stock_option.Monte_Carlo_pricer(Num_trials)
    price_6, error_6 = lookback_option.Monte_Carlo_pricer(Num_trials)
    
    print("-----------------------------")
    print("Parameters")
    print("-----------------------------")
    print(f"Initial Stock Price: {s_0}")
    print(f"Interest Rate: {r}")
    print(f"Drift: {drift}")
    print(f"Volatility: {volatility}")
    print(f"Time to Maturity: {n_mat*dt}")
    print(f"Strike Price: {strike_price}")
    print(f"Upper Barrier: {upper_barrier}")
    print(f"Lower Barrier: {lower_barrier}")
    print("-----------------------------")
    print(f"Monte-Carlo prices with {Num_trials} trials")
    print("-----------------------------")
    print(f"The European Call Option price is: {round(price_1,5)}   (standard error: {round(error_1,5)})")
    print(f"The Asian Call Option price is: {round(price_2,5)}   (standard error: {round(error_2,5)})")
    print(f"The Up-And-Out Barrier Option price is: {round(price_3,5)}   (standard error: {round(error_3,5)})")
    print(f"The Down-And-Out Barrier Option price is: {round(price_4,5)}   (standard error: {round(error_4,5)})")
    print(f"The Double Barrier Option price is: {round(price_5,5)}   (standard error: {round(error_5,5)})")
    print(f"The Lookback European Call Option price is: {round(price_6,5)}   (standard error: {round(error_6,5)})")

def test():
    
    r = 0.0025    #The interest rate
    s_0 = 105     #The inital stock price
    drift = 0.0025   #The drift, \mu, of the stock
    volatility = 0.28    #The volatility, \sigma, of the stock
    
    dt = 1/365  #The time discretization of the financial model  
    n_mat = 365 #time periods until maturity
    
    #The option parameters
    strike_price = 100
    lower_barrier = 101
    
    model = Black_Scholes_Model(dt, r, s_0, drift, volatility)
    
    euro_stock_option = European_call_option(model, n_mat, strike_price)
    down_and_out_stock_option = down_and_out_call_option(model, n_mat, strike_price, lower_barrier)
    
    Num_trials = 10000
    
    
    price_1, error_1 = euro_stock_option.Monte_Carlo_pricer(Num_trials)
    price_2 = euro_stock_option.exact_pricer()
    price_4, error_4 = down_and_out_stock_option.Monte_Carlo_pricer(Num_trials)
    
    print("-----------------------------")
    print("Parameters")
    print("-----------------------------")
    print(f"Initial Stock Price: {s_0}")
    print(f"Interest Rate: {r}")
    print(f"Drift: {drift}")
    print(f"Volatility: {volatility}")
    print(f"Time to Maturity: {n_mat*dt}")
    print(f"Strike Price: {strike_price}")
    print(f"Lower Barrier: {lower_barrier}")
    print("-----------------------------")
    print(f"Monte-Carlo prices with {Num_trials} trials")
    print("-----------------------------")
    print(f"The European Call Option price is: {round(price_1,5)}   (standard error: {round(error_1,5)})")
    print(f"The European Call Option exact price is: {round(price_2,5)}")
    print(f"The Down-And-Out Barrier Option price is: {round(price_4,5)}   (standard error: {round(error_4,5)})")
    
class Black_Scholes_Model:
    
    def __init__(self, dt, interest_rate, s_0, drift, volatility):
        self.dt = dt
        self.interest_rate = interest_rate
        self.s_0 = s_0
        self.drift = drift
        self.volatility = volatility
    
    def stock_path(self,n):
        """Samples from the process statisfying the SDE 
        $$dX = \mu dt +\simga dW$$ according to the real world measure
        
        Returns
        ---------
        A numpy array sampling the stock price at times 0, dt, 2*dt, .... , n*dt
        """
        
        t = np.arange(0, (n+0.2)*self.dt, self.dt)
        out = self.s_0*np.exp(self.volatility*brownian(n, self.dt) 
                                + (self.drift- self.volatility**2/2)*t)
        
        return out
    
    def risk_neutral_stock_path(self, n):
        """Samples from the process statisfying the SDE 
        $$dX = \mu dt +\simga dW$$ according to the real world measure
        
        Returns
        ---------
        A numpy array sampling the stock price
        from the risk neutral measure at times 0, dt, 2*dt, .... , n*dt
        """
        
        t = np.arange(0, (n+0.1)*self.dt, self.dt)
        out = self.s_0*np.exp(self.volatility*brownian(n, self.dt) 
                                + (self.interest_rate- self.volatility**2/2)*t)
        
        return out
        
class Option:
    '''A class forming the basis for the various option classes.
    '''
    def __init__(self, Black_Scholes_Model, n_mat):
            
        self.Black_Scholes_Model = Black_Scholes_Model
        self.n_mat = n_mat
        
    def Monte_Carlo_pricer(self, Num_Trials):
        '''A function for pricing options using Monte Carlo.
        
        Arguments
        ---------
        self = A option with a contract function
        Num_trails = a integer, the number of samples
        
        Returns
        ---------
       A tuple where the first component is the Monte Carlo mean of the contract 
       fucntion and the second component is the standard error.
        '''
        
        dt = self.Black_Scholes_Model.dt 
        r = self.Black_Scholes_Model.interest_rate
        
        samples = np.zeros(Num_Trials)
         
        
        for _ in range(Num_Trials):
            samples[_] = np.exp(-dt*self.n_mat*r)*self.contract(self.Black_Scholes_Model.risk_neutral_stock_path(self.n_mat))
       
        mean = np.sum(samples)/Num_Trials
        var = np.sum((samples - mean)**2)
        
        return mean, np.sqrt(var/(Num_Trials - 1)**2)
    
#Defining various options via inheritance from the Options class. 

class European_call_option(Option):
    
    def __init__(self, Black_Scholes_Model, n_mat, strike_price):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        self.strike_price = strike_price   
        
    def contract(self, stock_prices):
        
        if stock_prices[-1] > self.strike_price:
            return stock_prices[-1] - self.strike_price
        else:
            return 0
        
    def exact_pricer(self):
        
        sigma = self.Black_Scholes_Model.volatility
        s = self.Black_Scholes_Model.s_0
        r = self.Black_Scholes_Model.interest_rate
        K = self.strike_price
        T = self.n_mat*self.Black_Scholes_Model.dt
        
        d_1 = (1/(sigma*np.sqrt(T)))*(np.log(s/K) + (r + sigma**2/2)*T)
        d_2 = d_1 - sigma*np.sqrt(T)
        
        return s*N(d_1) - np.exp(-r*T)*K*N(d_2)
    
class Asian_call_option(Option):

    def __init__(self, Black_Scholes_Model, n_mat, strike_price):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        self.strike_price = strike_price
        
    def contract(self, stock_prices):
        
        average_price = np.sum(stock_prices)/self.n_mat
        
        if average_price > self.strike_price:
            return average_price - self.strike_price
        else:
            return 0
        
class up_and_out_call_option(Option):
    
    def __init__(self, Black_Scholes_Model, n_mat, strike_price, barrier_price):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        self.barrier_price = barrier_price
        self.strike_price = strike_price
        
    def contract(self, stock_prices):
        
        for price in stock_prices:
            if price > self.barrier_price:
                return 0
            
        if stock_prices[-1] > self.strike_price:
            return stock_prices[-1] - self.strike_price
        else:
            return 0
        
class down_and_out_call_option(Option):
    
    def __init__(self, Black_Scholes_Model, n_mat, strike_price, barrier_price):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        sigma = 0.28
        num_steps = 365
        self.barrier_price = barrier_price*np.exp(+0.5826*sigma*np.sqrt(1/num_steps))
        self.strike_price = strike_price
        
    def contract(self, stock_prices):
        
        for price in stock_prices:
            if price < self.barrier_price:
                return 0
            
        if stock_prices[-1] > self.strike_price:
            return stock_prices[-1] - self.strike_price
        else:
            return 0

class double_barrier_out_call_option(Option):
    
    def __init__(self, Black_Scholes_Model, n_mat, strike_price, upper_barrier, lower_barrier):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        self.strike_price = strike_price
        self.upper_barrier = upper_barrier
        self.lower_barrier = lower_barrier
        
    def contract(self, stock_prices):
        
        for price in stock_prices:
            if price < self.lower_barrier or price > self.upper_barrier:
                return 0
            
        if stock_prices[-1] > self.strike_price:
            return stock_prices[-1] - self.strike_price
        else:
            return 0
        
class lookback_European_call_option(Option):
    
    def __init__(self, Black_Scholes_Model, n_mat, strike_price):
        Option.__init__(self, Black_Scholes_Model, n_mat)
        self.strike_price = strike_price
        
        
    def contract(self, stock_prices):
        
        max_price = np.max(stock_prices)
        
        if max_price > self.strike_price:
            return max_price - self.strike_price
        else:
            return 0
        
#Some auxillary functions
                
def brownian(n, dt):
    """ A function to sample a Brownian motion at discrete times
    
    Arguments
    ---------
    n = number of steps being taken
    dt = size of steps
    
    Returns
    -------
    A numpy array sampling the Browian motion at times 0, dt, 2*dt, ... , n*dt.
    """
    #Gnerate random numbers from normal distribution with variance sqrt(dt)
    out = np.random.normal(scale = np.sqrt(dt), size = n+1)
    out[0] = 0
    
    #Cumlative sum to give sample of Brownian path
    out = np.cumsum(out)
    
    return out      

def N(x):
    """Returns the cumulative distribution function for N(0,1) evaluated at x.
    """
    out = (1/2)*(1+erf(x/np.sqrt(2)))    
    
    return out
    

#main()
test()
