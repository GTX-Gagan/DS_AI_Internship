import pandas as pd
products = pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])
print(products)
products['Laptop'] = 650
print(products)
print(products[:2])

