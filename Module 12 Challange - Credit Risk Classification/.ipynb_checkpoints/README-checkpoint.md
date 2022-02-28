# Credit Risk Classification

This project aims to analyze and build a logistic regression model to classify a credit risk based on imbalanced data. The data, a dataset of historical lending activity from a peer-to-peer lending services, is used here to build a model that can identify the creditworthiness of borrowers. 

---

## Technologies

This analysis is prepared in Jupyter Notebook using python 3.8 and the rich features of the [**pandas library**](https://pandas.pydata.org/) to perform the data analysis. 

[**scikit-learn**](https://scikit-learn.org/stable/index.html) that is open source library with a huge number of simple and efficient tools for predictive data analysis. The scikit-learn library categorizes the machine learning models into different groups, which it calls modules.Each group of functions implements different machine learning techniques. 

[**LogisticRegression model**](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) is one of the models in *sklearn.linear_model* group of models that is used to predict a binary outcome based on a set of independent variables.


[RandomOverSampler](https://imbalanced-learn.org/dev/references/generated/imblearn.over_sampling.RandomOverSampler.html) is class in *imblearn.over_sampling* library that is used to perform random over-sampling - object to over-sample the minority class(es) by picking samples at random with replacement. 

---
## Installation Guide

Before running the application first install the following dependencies (some of them can already be installed for your environment).

```python
conda install scikit-learn (it will also install all required dependencies)
```

---

## Outcomes

This analysis compares two models and makes a recommendation. As a summary of this analysis I would recommend the logistic regression model built on the oversampled data since it shows better results making predictions using test data.


---
## Usage

To use the ETF Analyzer project simply clone the repository and open the **credit_risk_resampling.ipynb** file in Jupyter Notebook. 


## Contributors

Brought to you by [Kirill Panov](https://www.linkedin.com/in/kirill-panov-696455192/) (us.kirpa1986@gmail.com).

---

