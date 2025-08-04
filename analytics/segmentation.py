import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_customers():
    users = pd.read_csv("./data/users.csv")
    orders = pd.read_csv("./data/orders.csv")
    print("Orders columns:", orders.columns)  # <-- Add this line

    # Count number of orders per user
    order_counts = orders.groupby('user_id').size().reset_index(name='order_count')

    # Merge with users
    df = pd.merge(users, order_counts, on='user_id')
    
    # Feature engineering
    features = df[['age', 'order_count']]
    
    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['segment'] = kmeans.fit_predict(features)
    
    print(df[['user_id', 'age', 'order_count', 'segment']])
    
    # Optional: visualize
    plt.scatter(df['age'], df['order_count'], c=df['segment'], cmap='viridis')
    plt.xlabel('Age')
    plt.ylabel('Order Count')
    plt.title('Customer Segmentation')
    plt.savefig("./data/customer_segments.png")
    plt.show()

if __name__ == "__main__":
    segment_customers()
