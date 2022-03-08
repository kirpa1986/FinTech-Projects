# Venture Funding with Deep Learning

This project aims to anayze startups and build models to predict their potential sucess based on the applicants data. The data (CSV file) contains more than 34000 companies that have received funding from Alphabet Soup - a venture capital firm. The analysis uses depp networks to build binary classifier models that will predict whether an applicant will become a successful business.

---

## Technologies

This analysis is prepared in Jupyter Notebook using python 3.8 and the rich features of the [**pandas library**](https://pandas.pydata.org/) to perform the data analysis. 

[**scikit-learn**](https://scikit-learn.org/stable/index.html) that is open source library with a huge number of simple and efficient tools for predictive data analysis. The scikit-learn library categorizes the machine learning models into different groups, which it calls modules.Each group of functions implements different machine learning techniques. 

[**TensorFlow**](https://www.tensorflow.org/) is an open source machine learning framework for all developers. It is used for implementing machine learning and deep learning applications.


[Kerras](https://www.tensorflow.org/api_docs/python/tf/keras) is compact, easy to learn, high-level Python library run on top of TensorFlow framework. It is made with focus of understanding deep learning techniques

---
## Installation Guide

Before running the application first install the following dependencies (some of them can already be installed for your environment).

```python
conda install scikit-learn (it will also install all required dependencies)

conda install -c conda-forge tensorflow (it will also install all required dependencies, including Keras)
```

---

## Outcomes

This analysis builds 3 models. To optimize models the following optimization techniques are used:
To optimize your model for a predictive accuracy as close to 1 as possible, you can use any or all of the following techniques:

* Adjusting the input data by dropping different features columns to ensure that no variables or outliers confuse the model.
* Add more neurons (nodes) to a hidden layer.
* Add more hidden layers.
* Add to or reduce the number of epochs in the training regimen.


---
## Usage

To use the project simply clone the repository and open the **venture_funding_with_deep_learning.ipynb** file in Jupyter Notebook. 


## Contributors

Brought to you by [Kirill Panov](https://www.linkedin.com/in/kirill-panov-696455192/) (us.kirpa1986@gmail.com).

---

