import requests, json
import pandas as pd
url = 'https://api.github.com/repositories'
data = requests.get(url)
result = json.loads(data.text)
print(result)
df = pd.DataFrame(result, columns=['name','full_name'])
print(df)