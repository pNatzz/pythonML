import pandas as pd

df_titanic = pd.read_csv("C:/Users/1000219787/pythonML/Kaggle_tinanic/train.csv")

#%% Preview data
print(df_titanic.head(3))
print(df_titanic.tail(3))
print(df_titanic.columns)
print(df_titanic.columns.tolist())
print(df_titanic.info())
print(df_titanic.dtypes)
print(df_titanic.select_dtypes(include = ["int64", "float"]).head(3))
print(df_titanic.select_dtypes(include = ["int64", "float"]).columns)
print(df_titanic.select_dtypes(include = ["int64", "float"]).columns.tolist())
print(df_titanic.select_dtypes(exclude = ["int64", "float"]).head(3))

df1_titanic = df_titanic.sort_values(by = "Name")
print(df1_titanic.head(3))

df2_titanic = df_titanic.sort_values(by = ["Sex", "Fare"]).head(2)
print(df2_titanic)

name = df_titanic["Name"]
print(type("name"))
print(name.head(10))

