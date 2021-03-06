import pandas as pd
import numpy as np
import scipy.stats as stats

from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer


import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor


def lookup(df, lu_type, lu_item=None):
    """
    Return a dataframe from 'df_look' with 'LUType' == lu_type
    and 'LUItem' == lu_item (if specified)
    """
    if lu_item:
        return df[(df.LUType == str(lu_type)) & (df.LUItem == str(lu_item))]
    else:
        return df[(df.LUType == str(lu_type))]
    
def col_stripper(df, column):
    "Returns column with leading and trailing whitespaces removed."
    return df[column].apply(lambda x: x.strip())

def fetch(cur, q):
    """Returns an SQL query."""
    return cur.execute(q).fetchall()

def chunker(df, li):
    """Returns data frame slice with selected columns"""
    return df[li].head(3)

def dropper(df, li, inplace=None):
    """Return data frame with select columns dropped
    
    Agrs:
        df: A data frame.
        li: A list of columns to be dropped.
        inplace: A Boolean.
    Returns:
        A data frame with the selected columns dropped.
        """
    if inplace:
        return df.drop(li, axis=1, inplace=True)
    else:
        return df.drop(li, axis=1)
    
def print_uniques(df, li):
    """Prints number of unique values in columns from a list."""
    for x in li:
        print(f'{x}: ', len(df[x].unique()))

def not_in(list1,list2):
    """Returns list of values fron list1 that are not in list2"""
    return [x for x in li1 if x not in li2]
    
def log_interpret(results, position, percent):
    """Prints change in target given a percent change in a logged predictor.
    
    Agrs:
        results: An ols model object.
        position: A list of log transformed predictors.
        percent: A float in decimal form indicating
                 the percent change in the predictor.
        """
    for p in position:
        print(round(results.params[p]*np.log(1+percent),2))
        
def log_all(results, position, percent):
    """Prints % change in a logged target given a % change in logged predictor.
    
    Agrs:
        results: An ols model object.
        position: An list of log-transformed predictors.
        percent: A float in decimal form indicating
                 the percent change in the predictor.
        """
    for p in position:
        print(round((((1+percent)**results.params[p])-1)*100,4))
        
def log_target(results, position):
    """Prints change in a logged target given a unit change in predictor.
    
    Agrs:
        results: An ols model object.
        position: An list of log transformed predictors.
        """
    for p in position:
        print(round((np.exp(results.params[p])-1)*100, 4))
        
def logger(df, features):
    """Logs values in columns and appends new logged columns to data frame.
    
    Args:
        df: A data frame.
        features: A list of columns.
    """
    for feature in features:
        df[f'{feature}_log'] = np.log(df[feature])
        
def create_formula(target_name, df):
    """Returns a formula string.
    
    Args:
        target_name: A string containing the target feature.
        df: A data frame.
    Returns:
        A string containing an ols model formula.
        """
    features = df.drop(target_name, axis=1).columns
    features = "+".join(features)
    return target_name + "~" + features

def rainbow(model_results):
    """Returns the statistic and p-value of a rainbow test.
    
    Agrs:
        model_results: an ols model object.
    Returns:
        A printout containing the statistic and p-value of a rainbow test.
    """
    rainbow_statistic, rainbow_p_value = linear_rainbow(model_results)
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)

def bp_test(df, target, model_results):
    """Returns the multiplier and p-value of a breusch-pagan test.
    
    Args:
        df: A data frame.
        target: A string containing the name of the target feature.
        model_results: A ols model object
    Returns:
            A printout of the multiplier and p-value of aa breusch-pagan test.
    """
    cols = df.columns[1:]
    y = df[target]
    y_hat = model_results.predict()
    lm, lm_p_value, fvalue, f_p_value = het_breuschpagan(y-y_hat, df[cols])
    print('Lagrange Multiplier p-value:', lm_p_value)
    print('F-statistic p-value:', f_p_value)

def vif(df):
    """Returns a data frame containing feature names and their VIF values.
    
    Agrs:
        df: A data frame.
    Returns:
        A data frame containing feature names and their VIF values.
    """
    cols = df.columns[1:]
    rows = df[cols].values
    vif_df = pd.DataFrame()
    vif_df["VIF"] = [variance_inflation_factor(rows, i) for i in range(len(cols))]
    vif_df["feature"] = cols
    return vif_df

def one_hot(df, feature):
    ohcoder = OneHotEncoder(drop='first')
    ohcoder.fit(df[[feature]])
    transformed = ohcoder.transform(df[[feature]])
    return ohcoder, transformed

#_________________________________________________________________________________
# Title: forward_selected source code
# Author: Schumacher, A & Smith, T
# Date: Thursday April 23, 2015
# Code Version: 1.0
# Availability: https://planspace.org/20150423-forward_selection_with_statsmodels/
#_________________________________________________________________________________
def forward_selected(data, response):
    """Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model
    
def cohens_d(sample1, sample2):
    """
    Returns Cohen's d value.
    
    Args: 
        sample1: A pandas series or numpy array.
        sample2: A pandas series of numpy array.
    Returns:
        Cohen's d value.
    """
    
    diff = sample1.mean() - sample2.mean()
    n1 = len(sample1)
    n2 = len(sample2)
    var1 = sample1.var(ddof=1)
    var2 = sample2.var(ddof=1)
    pooled_var = ((n1-1) * var1 + (n2-1) * var2) / (n1 + n2 - 2)
    d = diff / np.sqrt(pooled_var)
    return d

def test_ys(df, target, results):
    y = df[target]
    y_hat = results.predict()
    return y, y_hat