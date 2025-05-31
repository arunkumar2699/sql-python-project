import requests
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data['rates'].items(), columns=['Currency', 'Rate'])
print(df.head())