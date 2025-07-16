import pandas as pd
import sqlite3

df = pd.read_csv('Exp1.csv')

conn = sqlite3.connect('SurfaceEXP1')
df.to_sql('SurfaceEXP1', conn, if_exists='replace', index=False)
df_set = pd.read_sql_query('SELECT * FROM SurfaceEXP1', conn)

print(df_set)

conn.close()