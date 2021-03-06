import pandas as pd
import numpy as np
# import scipy.stats as stats

# from sklearn import preprocessing
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.preprocessing import FunctionTransformer


import matplotlib.pyplot as plt
import seaborn as sns

# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# from statsmodels.formula.api import ols
# from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
# from statsmodels.stats.outliers_influence import variance_inflation_factor

def heat_map(corr):
    """Returns a heatmap of a correlation matrix
    
    Args:
        corr: A corelation matrix object.
    """
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    fig1, ax1 = plt.subplots(figsize=(11, 9))
    sns.heatmap(corr, mask=mask, cmap='viridis');

def error_plot(df, target, model_results):
    """Returns an error plot visualization.
    
    Args:
        df: A data frame.
        target: A string containing the name of the target feature.
        model_results: A ols model object.
    Returns:
        A visualization of the residuals vs predicted values.
    """
    y = df[target]
    y_hat = model_results.predict()
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set(xlabel='Predicted Sale Price',
        ylabel='Residuals (Predicted-Actual Sale Price)')
    ax.scatter(x=y_hat, y=y_hat-y, color="mediumaquamarine", alpha=0.4);
    
def corr_area_price(df):
    """Returns a plot of SalePrice vs SqFtTotliving 
    
    Args:
        df: A data frame.
        """
    fig, ax = plt.subplots(figsize=(20,8))
    ax = sns.regplot(x='SqFtTotLiving', y='SalePrice', data=df, ci=None)
    ax.tick_params(labelsize=20) 
    ax.set_xlabel("")
    ax.set_ylabel("Mean Sale Price", size=20) 
    ax.set_title( "Correlation Between Total Living Area & Sale Price", size=30)
    # plt.savefig('corr_area_price',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()