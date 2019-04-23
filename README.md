# Stock Data Time-Series Analysis and Forecasting in Python
------
### Introduction to the Stock Market
The New York Stock Exchange (NYSE), the American stock exchange, 
sanctions the buying and trading of shares for publicly 
registered companies. The public stock exchange allows businesses to
raise financial capital by selling shares of ownership. The value of a share to 
investors is measured by a stock price. There are many variables and uncertainties which
can influence a stock's price away from market equilibrium. Overly optimistic or pessimistic 
conditions can drive stock value excessively high or low. The erratic nature of 
stock behavior creates a market risk. Investors look for stocks with 
value expected to rise while avoiding stocks with value expected to decrease.
Knowledge of stock price movement is essential for minimizing market risk.    

### Objective
The goal of this project is to explore the process of knowledge discovery from
financial data (financial KDD) for several stocks in the technology sector (listed in table). 
The information (historical stock quotes) will be retrieved live from the Yahoo! Finance web service. 
The Collected information is then formatted as a financial time series. 
This mathematical model is ideal for finding statistical descriptions and data visualizations of 
asset evaluation over time. 

| Technology Stock | Ticker |
|---------------|--------------|
| Adv Micro Devices | (**AMD**) | 
| Cisco Systems Inc | (**CSCO**) | 
| Intel Corp | (**INTC**) | 
| Micron Technology | (**MU**) | 
| Oracle Corp | (**ORCL**) | 
| Qualcomm Inc | (**QCOM**) | 

The process of knowledge discovery from the financial data will be split into two parts:
   
**Part 1**: For the first part, interesting knowledge will be discovered using statistical methods. These will describe 
the collection, analysis, interpretation, and presentation of the data. A *statistical model* is established
mathematical functions describing the behavior of objects in terms of random variables and their associated
probability distributions. This Project is based on the previously mentioned statistical model 
known as a time series. A central idea of the project will be understanding a financial time series using 
*statistical descriptions*. These will be used to identify the properties of the series and find 
data values which are noise or outliers. This will merge with the last concept of Part 1, *relevance analysis*, 
which is the first step in the data mining functionality: Classification and Regression for Predictive Analysis. 
This is described as attempting to identify attributes which are more relevant to the predictive process. 

**Part 2**: The second part of the knowledge discovery from data (KDD) process is based on 
the *predictive analysis* concepts of the data mining functionality: Classification and Regression for 
Predictive Analysis. This predictive process will be a type of *Supervised Learning* because the extracted 
dataset serves as "supervision" for the learning process. Attributes from the preprocessed 
data in Part 1 will make up the training set for the Classification learning phase. A classifier will 
be constructed to predict a financial attribute.    

### Outline
* **Time Series Analysis:**
    * Describe Time Series
         - Definition
         - Frequency
    * Getting Stock Price Quotes
         - Python Package Imports
         - Getting Stock Quote Data
         - Grouping Quotes
         - Visualize a Time Series
    * Exploring Time Series Data
         - Data Structure
         - Descriptive Statistics
         - Daily Returns
         - Visualizing Daily Returns
    * Stationary Components of Time Series
         - Description
         - Decomposition
    * Data Processing
        - Exponential Smoothing
* **Predictive Process:**
    * Feature Extraction
    * Predictive Analysis
        
 
### References
1. Ruey S. Tsay, Wiley (2010). Analysis of Financial Time Series, Third Edition 
    ISBN: 0-470-41435-9; 13-digits: 978-0470414354 [Link][1]

2. Pal, A. (2017). Practical time series analysis: Master time series data processing, visualization, and 
    modeling using Python. Birmingham: Packt. [link][2]

3. Heydt, M. (2015). Mastering pandas for Finance. Packt Publishing. [link][3]

4. J Han, M Kamber, J Pei, M Kaufmann, (2011). Data Mining: Concepts and Techniques, 3rd edition 
    ISBN: 9780123814791 [link][4]

5. Khaidem, Luckyson, Snehanshu Saha, and Sudeepa Roy Dey (2016). Predicting the Direction 
    of Stock Market Prices Using Random Forest, Cornell. [link][5]

[1]: http://faculty.chicagobooth.edu/ruey.tsay/teaching/
[2]: https://www.amazon.com/Practical-Time-Analysis-Processing-Visualization/dp/1788290224
[3]: https://www.amazon.com/Mastering-Pandas-Finance-Michael-Heydt/dp/1783985100
[4]: https://www.amazon.com/Data-Mining-Concepts-Techniques-Management/dp/0123814790
[5]: https://arxiv.org/pdf/1605.00003.pdf

#%% md
# (Part 1) Time Series Analysis
---------------
## Description
-------
### Definition:

The **Time Series** on a variable/attribute *a* is indicated as *a<sub>t</sub>*, with the subscript t 
representing time. The first and last observations available on attribute *a* are at t = 1, and t = T.


The set of times t = {1, 2,.. ,T} is referred to as the *observation period*.
<pre>    
    Observations are typically measured in equally spaced intervals (frequency), (i.e minute, hour, 
    day, etc... for finance). 
</pre>

Essentially, a time series contains quantitative observations on one or more assessable characteristics of
an entity, taken at multiple points in time. 

### Frequency

Financial data is a *fixed frequency* time series, meaning the 
data points occur at regular intervals. This project will focus on financial time series with a daily 
frequency. Higher frequencies in financial time series is referred to as "high frequency" or "tick-by-tick" data.
   
### Analysis:

time series analysis applies different statistical methods to explore and model the internal 
structures of the time series data. 

Several interesting internal structures are: trend, seasonality, stationarity, autocorrelation, etc..

The internal structures require special formulation and techniques for their analysis