import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import certifi
import openpyxl
from faker import Faker
import requests
import json
from matplotlib import pyplot as plt
# Get Data Regarding World Population
url = 'https://drive.google.com/file/d/1m9xOT5kcrdLiDxC4sa7Y53XLMTEvaVZL/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)
# print(data.dtypes)
# print(data.columns)
# Organize Data
df = pd.DataFrame(data, columns=["Name", "2022", "2010", "2000", "1990", "1980", "Rank"])
df = df.assign(Pop_Change=df["2022"] - df["1980"])
# df = pd.DataFrame(data, columns=["Name", "2022", "1980", "Pop_Change"])
# Largest Countries
# top_10_country = df.nlargest(n=10, columns=["2022", "1980"])
# print(top_10_country)

# Testing Less than Data
# less_than_5m = df[df["1990"] < 5000]
# print(less_than_5m)
# less_than_5m.plot()
# plt.show()


print(df)
top_7_growth = df.nlargest(n=7, columns=["Pop_Change"])
top_5_decline = df.nsmallest(n=5, columns=["Pop_Change"])
print(top_7_growth)
print("Decline")
print(top_5_decline)

# Plot Styles
plt.style.use('dark_background')
top_7_growth.plot(x="Name", y=["Pop_Change", "1980", "2022"], kind="bar")

plt.show()

#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()
#df.plot()
#plt.show()
# from matplotlib import pyplot as plt
#df.plot(x='Name', y=['Rank'], kind="line", figsize=(12, 12))

# print(data)
#print(df);
#mp.show()
