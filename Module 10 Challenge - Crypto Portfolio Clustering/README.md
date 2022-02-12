# Crypto Portfolio Clustering

This projects aims to anaalyze a crypto portfolio using unsepervised learning techniques like clustering (KMeans) and Principal Component Analysis to reduce the number of features. 

---

## Technologies

This analysis is prepared in Jupyter Notebook using python 3.8 and the rich features of the [**pandas library**](https://pandas.pydata.org/) to perform the data analysis. 

[**scikit-learn**](https://scikit-learn.org/stable/index.html) that is open source library with a huge number of simple and efficient tools for predictive data analysis. The scikit-learn library categorizes the machine learning models into different groups, which it calls modules.Each group of functions implements different machine learning techniques. [**K-means**](https://scikit-learn.org/stable/modules/clustering.html#k-means) that used in the project is a clustering technique, so we can find it in the [**cluster**](https://scikit-learn.org/stable/modules/clustering.html#clustering) module of scikit-learn library. 

Standard Scaling which is a method of centering values around the mean. [**StandardScaler**](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling) module of scikitlearn library transforms the data by calculating the mean value of the column and scaling the data in the column to a standard deviation of 1. It does this by first subtracting the mean value of the column, and then dividing by the standard deviation of the column for each value in the column: (value - mean)/standard deviation.

[**Principal Component Analysis (PCA)**](https://www.sartorius.com/en/knowledge/science-snippets/what-is-principal-component-analysis-pca-and-how-it-is-used-507186) is one of the Clustering Optimization techniques. It decomposes a multivariate dataset in a set of successive orthogonal components that explain a maximum amount of the variance.

---
## Installation Guide

Before running the application first install the following dependencies (some of them can already be installed for your environment).

```python
conda install scikit-learn (it will also install all required dependencies)
```

---

## Outcomes

Using the above mentioned techniques allows to cluster cryptocurrencies by their performance in different time periods. Scaling, Elbow Curve method and using of PCA optimized the result - points in the clusters became more close to each other. Additionally, optimizations allow to distinct the clusters of outperformers from the clusters with the pretty normal performance figures:
![<clustering_example>](static/clusters_pca.PNG)


---
## Usage

To use the ETF Analyzer project simply clone the repository and open the **crypto_investments.ipynb** file in Jupyter Notebook. 


## Contributors

Brought to you by [Kirill Panov](https://www.linkedin.com/in/kirill-panov-696455192/) (us.kirpa1986@gmail.com).

---

