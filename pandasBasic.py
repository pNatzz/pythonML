import pandas as pd
from pathlib import Path

sourcedir = Path("C:/Users/1000219787/pythonML")

df = pd.read_csv(sourcedir/'pm-24-jan-2021.csv')
print(df.head())
print(df.tail())
headTail = pd.concat([df.head(), df.tail()], ignore_index = True)