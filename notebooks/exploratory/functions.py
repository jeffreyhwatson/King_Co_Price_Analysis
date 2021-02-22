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