import os
import pandas as pd
from django.shortcuts import render, redirect
from django.conf import settings

# Path helpers
BASE_DIR = settings.BASE_DIR
DATA_DIR = os.path.join(BASE_DIR, 'analytics', 'data')

def home(request):
    df = pd.read_csv(os.path.join(DATA_DIR, "optimized_prices.csv"))
    products = df.to_dict(orient='records')
    return render(request, 'home.html', {'products': products})


def run_recommender(request):
    # Load data
    df = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))

    # Simulated rating
    df['rating'] = df['quantity'] + 2

    from surprise import Dataset, Reader, SVD
    from surprise.model_selection import train_test_split

    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)

    model = SVD()
    model.fit(trainset)

    all_products = df['product_id'].unique()
    rated_products = df[df['user_id'] == 1]['product_id'].tolist()
    unrated_products = [pid for pid in all_products if pid not in rated_products]

    recommended = []
    for pid in unrated_products:
        pred = model.predict(1, pid)
        recommended.append((pid, pred.est))

    recommended.sort(key=lambda x: x[1], reverse=True)
    top_recommendations = recommended[:3]

    return render(request, 'recommendations.html', {'recommendations': top_recommendations})


def run_segmentation(request):
    from sklearn.cluster import KMeans
    users = pd.read_csv(os.path.join(DATA_DIR, 'users.csv'))
    orders = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))

    order_counts = orders.groupby('user_id').size().reset_index(name='order_count')
    df = pd.merge(users, order_counts, on='user_id')
    features = df[['age', 'order_count']]

    kmeans = KMeans(n_clusters=3, random_state=42)
    df['segment'] = kmeans.fit_predict(features)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(df['age'], df['order_count'], c=df['segment'], cmap='viridis')
    plt.xlabel('Age')
    plt.ylabel('Order Count')
    plt.title('Customer Segmentation')
    output_path = os.path.join(BASE_DIR, 'core', 'static', 'customer_segments.png')
    plt.savefig(output_path)
    plt.close()

    return redirect('home')


def run_pricing(request):
    products = pd.read_csv(os.path.join(DATA_DIR, 'products.csv'))
    orders = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))

    demand = orders.groupby('product_id')['quantity'].sum().reset_index()
    demand.columns = ['product_id', 'total_sold']
    df = pd.merge(products, demand, on='product_id')

    def adjust_price(row):
        if row['total_sold'] > 3:
            return round(row['price'] * 1.10, 2)
        elif row['total_sold'] < 2:
            return round(row['price'] * 0.90, 2)
        else:
            return row['price']

    df['adjusted_price'] = df.apply(adjust_price, axis=1)
    df.to_csv(os.path.join(DATA_DIR, 'optimized_prices.csv'), index=False)

    return redirect('home')
