import pandas as pd

def optimize_pricing():
    orders = pd.read_csv("./data/orders.csv")
    products = pd.read_csv("./data/products.csv")
    
    # Calculate total quantity sold per product
    demand = orders.groupby('product_id')['quantity'].sum().reset_index()
    demand.columns = ['product_id', 'total_sold']
    
    df = pd.merge(products, demand, on='product_id')
    
    # Rule-based price adjustment
    def adjust_price(row):
        if row['total_sold'] > 3:
            return round(row['price'] * 1.10, 2)  # increase 10%
        elif row['total_sold'] < 2:
            return round(row['price'] * 0.90, 2)  # decrease 10%
        else:
            return row['price']  # keep same

    df['adjusted_price'] = df.apply(adjust_price, axis=1)
    
    print(df[['product_id', 'price', 'total_sold', 'adjusted_price']])
    df.to_csv("./data/optimized_prices.csv", index=False)

if __name__ == "__main__":
    optimize_pricing()
