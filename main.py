import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
# Get Data Regarding World Population Population in 000s so 5,000,000 is 5000
url = 'https://drive.google.com/file/d/1m9xOT5kcrdLiDxC4sa7Y53XLMTEvaVZL/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)

# Organize Data
df = pd.DataFrame(data, columns=["Name", "2022", "2010", "2000", "1990", "1980"])
df = df.assign(Pop_Change=df["2022"] - df["1980"])
# Print the Data
print(df)

# Create Top 7 Growth Countries
top_7_growth = df.nlargest(n=7, columns=["Pop_Change"])

# Create Bottom 5 Decline Population Countries
top_5_decline = df.nsmallest(n=5, columns=["Pop_Change"])


#Print the Data
print("Growth")
print(top_7_growth)
print("Decline")
print(top_5_decline)

# Plot Styles
plt.style.use('dark_background')

# create subplot with having two side plots
fig1, axes = plt.subplots(nrows=1, ncols=2, figsize=(22, 10))
# Plot First Panda
top_7_growth.plot(ax=axes[0], subplots=True, x="Name", y=["Pop_Change"], kind="bar", color='g')
# Plot Second Panda
top_5_decline.plot(ax=axes[1], subplots=True, x="Name", y=["Pop_Change"], kind="bar", color='r')

# Tried Changing Labels for the Plot

# axes[0].legend[top_7_growth], ["Population Growth"]
# axes[1].legend[top_5_decline], ["Population Decline"]
# top_5_decline.set_label("Population Decrease")

# Show Plot
plt.show()

# Code to Test Plotting works

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

# Texting Various Items
# df = pd.DataFrame(data, columns=["Name", "2022", "1980", "Pop_Change"])
# Largest Countries
# top_10_country = df.nlargest(n=10, columns=["2022", "1980"])
# print(top_10_country)

# Testing Less than Data
# less_than_5m = df[df["1990"] < 5000]
# print(less_than_5m)
# less_than_5m.plot()
# plt.show()