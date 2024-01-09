import pandas as pd

ecom_sales = pd.read_csv('dados/ecom_sales.csv')
ecom_sales = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales (R$)')
# print(ecom_sales.head())
# print(ecom_sales.tail())
print(ecom_sales)
