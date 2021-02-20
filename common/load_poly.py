from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import time
import matplotlib.pyplot as plt


def PolynomialModel(degree=1, estimator=None, **kwargs):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    if estimator is not None:
        model = estimator()
        pipline = Pipeline([('polynomial_features:', polynomial_features),
                            ('model', model)])
        return pipline


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1,
                        train_sizes=np.linspace(0.1, 1.0, 5)):
    plt.title(title)
    if ylim is not None:
        plt.ylim(ylim)
    plt.xlabel('Train Example')
    plt.ylabel('Scores')
    train_sizes, train_scores, test_scores = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=1, color='r')
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=.1, color='g')
    plt.plot(train_sizes, train_scores_mean, 'o--', color='b', label='Training score')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Test score')
    plt.legend(loc='best')
    return plt
