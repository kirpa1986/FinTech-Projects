# Financial and User Data Analysis

This projects aims to anaalyze the company's financial and user data for [MercadoLibre](http://investor.mercadolibre.com/investor-relations). With over 200 million users, MercadoLibre is the most popular e-commerce site in Latin America. The analysis shows if the Google search traffic for the company links to any financial events at the company or if the search traffic data just present random noise. As an outcome the notebook also produces a time series model that analyzes and forecasts patterns in the hourly search data. 

In addition, the notebook produces a forecast of the total sales for the next quarter that in turn dramatically increases the ability to plan budgets and helps guide expectations for the company investors.

---

## Technologies

This analysis is prepared in Jupyter Notebook using python 3.8 and the rich features of the [**pandas library**](https://pandas.pydata.org/) to perform the data analysis. 

[**Fecebook Prophet**](https://facebook.github.io/prophet/) is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality 

[**hvPlot**](https://hvplot.holoviz.org/) provides a high-level plotting API built on [**HoloViews**](https://holoviews.org/) that provides a general and consistent API for plotting data in all the abovementioned formats.

---
## Installation Guide

Before running the application first install the following dependencies to be able to import the Prophet library the right way because installing it can be tricky on some machines. 

```python
# On Prompt install Ephem
conda install -c anaconda ephem

# Install Pystan
conda install -c conda-forge pystan

# Finally install Fbprophet
conda install -c conda-forge fbprophet
```


Another option is to use [**Google Colab**](https://colab.research.google.com/) that is an IDE that allows you to run Jupyter Notebooks in the cloud. To configure your Google Colab workspace to include the needed libaries, you'll create a notebook using **Google Colab**, then install the necessary libraries. To use **Prophet**, you'll need to install *fbprophet* as well as its dependency *pystan*.
To use **hvPlot** in Google Colab, you'll need to install both *hvplot* and its dependency *holoviews*. The following code accomplishes these tasks:

```python
# Install the required libraries
from IPython.display import clear_output
try:
  !pip install pystan
  !pip install fbprophet
  !pip install hvplot
  !pip install holoviews
except:
  print("Error installing libraries")
finally:
  clear_output()
  print('Libraries successfully installed')
```

---

## Outcomes

Using the above mentioned libraries including fbprophet allowed to analyse and predict financial figures like revenue for the next quarter and build a near-term forecast for the popularity of MercadoLibre.

**Search traffic trends:**

![<search_traffic_trends>](static/pics/search_traffic_trends.PNG)

**Revenue Forecast (+90 days):**

![<revenue_forecast>](static/pics/revenue_forecast.PNG)

---
## Usage

To use the ETF Analyzer project simply clone the repository and open the **forecasting_net.prophet.ipynb** file in Jupyter Notebook. 


## Contributors

Brought to you by [Kirill Panov](https://www.linkedin.com/in/kirill-panov-696455192/) (us.kirpa1986@gmail.com).

---

