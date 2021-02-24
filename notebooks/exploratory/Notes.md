## Notes
#### In Pandas
```
df_sale.shape, df_resb.shape, df_parc.shape, look.shape
((351067, 24), (181510, 50), (205199, 82), (1208, 3))
```

#### Merged Data Frame
```
# doing a chained merge of the three data frames on the 'Major' and 'Minor' columns
df = pd.merge(pd.merge(df_sale, df_parc, on=['Major', 'Minor']), df_resb, on=['Major', 'Minor'])
```

```
df.shape
(251300, 151)
```

## In SQL Data Frame
#### Tables
```
('SALES',), ('RESB',), ('PARC',)
``` 
#### Data Frame Shape After Join
```
q = """SELECT*FROM SALES AS SA
       JOIN PARC AS PA
       ON SA.Major = PA.Major
       AND SA.Minor = PA.Minor
       JOIN RESB AS RE
       ON PA.Major = RE.Major
       AND PA.Minor = RE.Minor
       """
df = pd.DataFrame(fn.fetch(cur, q))
df.columns = [i[0] for i in cur.description]
```

```
df.shape
(251300, 156)
```

## Questions:

1. A lot of the cohort either did data cleaning on individual data frames and then tried to merge them later, or merged the data frames two at a time. Was it a mistake to join all three tables into a main data frame first? It seemed like the most logical way to proceed.

2. Since the smallest table (RESB) has 181510 rows, and the tables are being (INNER) JOINED, why is the shape of the data frame 251300? I thought JOIN grabs the intersection of the tables based on certain criteria. Why isn't the shape  <= 181510?

3. Pathing issues in the repo regarding the function.py module, DB_Creator notebook, KingDB.db file. Things break if the files are not in the same directory as the main notebook. What are the fixes?

4. I placed a `.gitignore` file in the `/notebooks/exploratory` directory because the KingDB.db file is 176mb. Is it acceptable to have multiple .gitignore file in the repo? How do you deal with the pathing issues if you only have one `.gitignore` in the maid directory? On a side note, if your data files are large, how do you deal with that on github?

5. After creating a new `king_co` environment, should I just use the python3 kernal?