import pandas as pd

df_titanic = pd.read_csv("C:/Users/1000219787/pythonML/Kaggle_tinanic/train.csv")

print(df_titanic.head(3))
print(df_titanic.tail(3))
print(df_titanic.columns)
print(df_titanic.dtypes)
print(df_titanic.info())
