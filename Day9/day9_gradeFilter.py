import pandas as pd
grade=pd.Series([85, None, 92, 45, None, 78, 55])
data=grade.isnull()
print(data)
data1=grade.fillna(0)
print(data1)
data2=grade[grade>60]
print(data2)