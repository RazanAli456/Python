import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
df=pd.read_csv("USA_Housing.csv")
print(df.head())#printing the first 5 rows
print(df.tail())#printing the last 5 rows
print(df.info())#telling information
#The seaborn.pairplot()
#function is a powerful data visualization tool in Python
#used to plot pairwise relationships between multiple numerical variables in a dataset.
sb.pairplot(df)
plt.show()
sb.heatmap(df.corr())
plt.show()