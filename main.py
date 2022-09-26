import pandas as pd
import numpy as np
import matplotlib as mp

# matplotlib.use("QtAgg")
import certifi
import openpyxl
from faker import Faker
import requests
import json

# Get Data Regarding World Population
url = 'https://drive.google.com/file/d/1m9xOT5kcrdLiDxC4sa7Y53XLMTEvaVZL/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)
# print(data.dtypes)
# print(data.columns)
# Organize Data
df = pd.DataFrame(data, columns=["Name", "2022", "2010", "2000", "1990", "Rank"])

# from matplotlib import pyplot as plt
df.plot(x='Name', y=['Rank'], kind="line", figsize=(12, 12))

# print(data)
print(df)
mp.show()
