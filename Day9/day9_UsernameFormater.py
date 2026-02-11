import pandas as pd 
username = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(username)
data = username.str.strip()
print(data)
lowercase_username= data.str.lower()
print(lowercase_username)
contains_A= lowercase_username.str.contains('a')
print(contains_A)