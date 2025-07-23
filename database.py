import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Exp1.csv')

#ktore kolumhy do modelu
columns_to_use = ["ap", "vc", "feed", "Ra"]
df = df[columns_to_use].copy()

# zamiana typu danych w kolumnach?
for col in columns_to_use:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# usuwanie?
df = df.dropna()

# wyszukiwanie outlierow
for col in ["ap", "vc", "feed", "Ra"]:
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot – {col}")
    plt.show()

# skalowanie danych?
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[["ap", "vc", "feed"]])

# nowy df
df_scaled = pd.DataFrame(X_scaled, columns=["ap_scaled", "vc_scaled", "feed_scaled"])
df_scaled["Ra"] = df["Ra"].values

# zapis
conn = sqlite3.connect('SurfaceEXP1.db')  # dodaj rozszerzenie .db (zalecane)
df_scaled.to_sql('SurfaceEXP1', conn, if_exists='replace', index=False)
conn.close()
