import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as mp
print(sb.get_dataset_names())
df=sb.load_dataset("penguins")
print(df.head(10))
print(df.tail(10))
print(df.isnull().sum())
print(df.corr)
corr = df.corr(numeric_only=True)
df.hist(figsize=(12,8))
mp.show()
print(df.columns)
sb.heatmap(corr, cmap='Wistia', annot=True)
mp.show()
sb.countplot(data=df, x='sex', palette='summer' )
mp.show()