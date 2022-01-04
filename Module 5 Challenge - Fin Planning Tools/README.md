# Financial Planning Tools

This small project aims to analyze the portfolio (crypto, stocks, bonds) through using two financial analysis tools:
1. A financial planner for emergencies. The members of local communities will be able to use this tool to visualize their current savings. The members can then determine if they have enough reserves for an emergency fund. 
2. A financial planner for retirement. This tool will forecast the performance of their retirement portfolio in 30 years. 

---

## Technologies

This analysis is prepared in Jupyter Notebook using python 3.8 and the rich features of the [**pandas library**](https://pandas.pydata.org/) to perform the data analysis. 

**requests** and **json** modules are used to fetch and work with the data provided by [**alternative.me Crypto API**](https://alternative.me/crypto/api/).

[**Alpaca Client SDK**](https://alpaca.markets/docs/api-documentation/client-sdk/) is used to retrieve and work with the market data (stocks and bonds here). Useful step by step video tutorials are available on this [link](https://alpaca.markets/docs/get-started-with-alpaca/tutorial-videos/).

**MCForecastTools library** (located in the project root folder) is used to create a Monte Carlo simulation (MCSimulation class) for the portfolio. To get more info on how to configure and use it run the command in Jupyter Notebook: 
```python
?MCSimulation
```
---

## Installation Guide

Before running the application first install the following dependencies (some of them can already be installed for your environment).

```python
  pip install requiests
  pip install json
  pip install alpaca_trade_api
  pip install dotenv
```

---

## Usage

To use the Financial Planning project simply clone the repository and open the **financial_planning_tools.ipynb** file in Jupyter Notebook. 

To be able to use Alpaca API or Client SDK create *.env* file in project root folder which should store your Alpaca Key ID and Secret ID. 



---

## Contributors

Brought to you by [Kirill Panov](https://www.linkedin.com/in/kirill-panov-696455192/) (us.kirpa1986@gmail.com).

---

