import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aapl_stock = pd.read_excel('aaplStock.xlsx', index_col = None, na_values=['NA'])

aapl_stock.head()
aapl_stock.describe()
pd.value_counts(aapl_stock['Open']).plot.bar()
def show(): 

    plt.plot(aapl_stock['Date'], aapl_stock['Open'], label='Open Price')
    plt.plot(aapl_stock['Date'], aapl_stock['Close/Last'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL Stock Prices Over Time')
    plt.xticks(rotation=45)  # Rotate dates for readability
    plt.legend() #box aka legend
    plt.show() 

show()