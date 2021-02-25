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