import numpy as np


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
        A data frame with the selected columns dropped."""
    
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
        percent: A float in decimal form referring the to the percent change in the predictor.
        """
    for p in position:
        print(round(results.params[p]*np.log(1+percent),2))
        
def log_all(results, position, percent):
    """Prints % change in a logged target given a % change in logged predictor.
    
    Agrs:
        results: An ols model object.
        position: An list of log-transformed predictors.
        percent: A float in decimal form referring the to the percent change in the predictor.
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