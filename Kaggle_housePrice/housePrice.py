import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df_house = pd.read_csv("C:/Users/1000219787/pythonML/Kaggle_housePrice/train.csv", index_col = False)

# display dataset
# print(df_house.head())

#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

print(df_house.head(3))
print(df_house.shape)
columns = df_house.columns.tolist() # let's see the column names
print(columns)

# check null data
print(df_house.isnull().any())
print(df_house.columns[df_house.isnull().any()].tolist) # let's see column name which has null
print(df_house.isnull().sum())

#%%
# Data processing
# drop column which has a lot of missing data
df_house = df_house.drop(["Id", "Alley", "FireplaceQu", "PoolQC", "Fence", "MiscFeature"], axis = 1)
print(df_house.head())

# Or fill missing value with column's mean
# df.column_name = df.column_name.fillna(df.mean()["column_name"])
df_house.GarageYrBlt = df_house.GarageYrBlt.fillna(df_house.mean()["GarageYrBlt"])

# Or drop ervery column that has missing vaue *** NOT RECOMMEND ***
# df = df.dropna(axis = 0)

#%% Splitting Train/Test Set
# use numpy library and train_test_split from sklearn library
# Categorical and numeric columns use different ways

x = df_house.SalePrice.copy().values

df_house_categorical_data = df_house.select_dtypes(exclude = ["int64", "float64"])
df_house_categorical_data = pd.get_dummies(df_house_categorical_data) # use .get_dummies() to convert catagorical variable into dummy variables
df_house_categorical_data.reset_index(drop = False, inplace = True)
df_house_categorical_data.head(3)