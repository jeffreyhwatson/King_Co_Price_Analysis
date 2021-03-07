import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

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
    
def strict_porches(series1, series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    porch_strict = pd.DataFrame({'type': ['Open', 'Enclosed'],\
                                 'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=porch_strict)
    ax.set_xlabel("Porch Type", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With Strictly Open Porches Have Higher Mean Sale Prices", size=30)
    # plt.savefig('strict_porches',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()
    
def heat_means(df):
    """Returns a plot of the heat system sale price means. 
    
    Args:
        df: A data frame.
        """
    sns.barplot(x='HeatNames', y='SalePrice', data=df, palette='winter_r')
    plt.xticks(rotation=45, ha='right');

def elecbb(series1, series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    elecbb = pd.DataFrame({'type': ['Higher Performing Types','ElecBB & Floor-Wall'],\
                                 'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=elecbb)
    ax.set_xlabel("Heating System Type", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With ElecBB & Floor-Wall Heat Have Lower Mean Sale Prices", size=30)
    # plt.savefig('elecbb_floor',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()

def finished(series1,series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    finished = pd.DataFrame({'type': ['Unfinished', 'Finished'],\
                             'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=finished)
    ax.set_xlabel("Basement Type", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With Finished Basements Have Higher Mean Sale Prices", size=30)
    # plt.savefig('finished',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()
    
def ave_hi(series1,series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    av_vs_hi = pd.DataFrame({'type': ['Average', 'High'],\
                             'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=av_vs_hi)
    ax.set_xlabel("Basement Quality", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With High Quality Finished Basements Have Higher Mean Sale Prices", size=30)
    # plt.savefig('av_vs_hi',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()
    
def po_hi(series1,series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    po_vs_hi = pd.DataFrame({'type': ['Poor', 'High'],\
                             'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=po_vs_hi)
    ax.set_xlabel("Basement Quality", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With High Quality Finished Basements Have Higher Mean Sale Prices", size=30)
    # plt.savefig('po_vs_hi',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show()
    
def po_ave(series1,series2):
    """Returns a plot of the mean sale prices
    
    Args:
        series1: A pandas series.
        series2: A pandas series.
        """
    po_vs_ave = pd.DataFrame({'type': ['Poor', 'Average'],\
                             'values': [series1.mean(), series2.mean()]})
    fig, ax=plt.subplots(figsize=(20,7))
    ax = sns.barplot(x='type', y='values', data=po_vs_ave)
    ax.set_xlabel("Basement Quality", size=20)
    ax.set_ylabel(" Average Sale Price", size=20)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=20)
    ax.set_title("Homes With Average Quality Finished Basements Have Higher Mean Sale Prices", size=30)
    # plt.savefig('po_vs_hi',  bbox_inches ="tight",\
    #             pad_inches = .25, transparent = False)
    plt.show() 