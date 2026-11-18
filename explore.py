#self-reflection: 1.A boolean filter asks a yes or no question about every row, checks each row against the condition, and keeps only the rows that pass  2.The single brackets return a series, the double brackets return a DataFrame. This distinction matters when you need several columns like in exercise 7  3.The most compelling reason I'd give is that your steps are written down as code so you can re-run them exactly.

print("--Exercise 1--")
import pandas as pd; df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--Exercise 2--")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("--Exercise 3--")
df.sort_values('revenue', ascending=False).head(5)
print(df.sort_values('revenue', ascending=False).head(5))

print("--Exercise 4--")
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())

print("--Exercise 5--")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())

print("--Exercise 6--")
print(df['region'].unique())
print(df['region'].value_counts())

print("--Exercise 7--")
subset = df[['region', 'product', 'revenue']]
print(subset.shape)

print("--Exercise 8--")
df.to_csv('data/explored.csv', index=False)