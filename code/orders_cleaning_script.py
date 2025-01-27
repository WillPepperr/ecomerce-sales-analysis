import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 1000)

df = pd.read_csv("C:/Users/wicro/Desktop/Portfolio projects/Ecommerce/data/orders.csv")

#removes typo in monitor name
df['product_name'] = df['product_name'].replace({'27in"" 4k gaming monitor': '27in 4K gaming monitor'})

#drop rows with null data
df = df.dropna()

#drop rows with sale price $0.00
df = df[df['usd_price'] != 0]

df.to_csv('improved_orders.csv', index=False)



