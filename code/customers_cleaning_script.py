import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 1000)

df = pd.read_csv("C:/Users/wicro/Desktop/Portfolio projects/Ecommerce/data/customers.csv")



df['marketing_channel'] = df['marketing_channel'].replace({np.nan: 'unknown'})
df['account_creation_method'] = df['account_creation_method'].replace({np.nan: 'unknown'})



df.to_csv('customers_improved.csv', index=False)


