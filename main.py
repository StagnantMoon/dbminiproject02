import pandas as pd
import certifi
import openpyxl
from faker import Faker
import requests
import json
# Get Data Regarding World Population
url= 'https://drive.google.com/file/d/1m9xOT5kcrdLiDxC4sa7Y53XLMTEvaVZL/view?usp=sharing'
url= 'https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

print(df)
