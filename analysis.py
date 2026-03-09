import pandas as pd

df = pd.read_csv("train.csv")
print(df.head())
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

print(df.dtypes)
print("Rows before:", len(df))

df = df.drop_duplicates()

print("Rows after:", len(df))

total_sales = df['Sales'].sum()
print("Total Sales Revenue:", total_sales)

monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
print(monthly_sales)

top_products = (
    df.groupby('Product Name')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)

region_sales = (
    df.groupby('Region')['Sales']
      .sum()
      .sort_values(ascending=False)
)

print(region_sales)

category_sales = (
    df.groupby('Category')['Sales']
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)