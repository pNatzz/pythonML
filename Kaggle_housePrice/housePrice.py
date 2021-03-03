import pandas as pd

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
print(df_house)