import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np
import pandas as pd
df=pd.read_csv("Weather.csv")
print(df.head())
print(df.tail())
print(df.info())
sb.barplot(x=df["humidity"],y=df["temperature"],hue=df['weather_type'])
mp.show()
sb.jointplot(x=df["humidity"],y=df["temperature"],kind="hex")
mp.show()
sb.jointplot(x=df["humidity"],y=df["temperature"],kind="kde")
mp.show()
sb.pairplot(df[["humidity","temperature","air_pollution_index"]])
mp.show()
