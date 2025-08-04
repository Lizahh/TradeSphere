import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

def build_recommender():
    df = pd.read_csv("analytics/data/orders.csv")
    
    # Create dummy user-product rating matrix
    df['rating'] = df['quantity'] + 2  # Fake rating from quantity
    
    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)
    
    trainset, testset = train_test_split(data, test_size=0.2)
    
    model = SVD()
    model.fit(trainset)
    
    predictions = model.test(testset)
    
    # Predict for user 1 all unrated items
    all_products = df['product_id'].unique()
    rated_products = df[df['user_id'] == 1]['product_id'].tolist()
    unrated_products = [pid for pid in all_products if pid not in rated_products]
    
    recommended = []
    for pid in unrated_products:
        pred = model.predict(1, pid)
        recommended.append((pid, pred.est))
    
    recommended.sort(key=lambda x: x[1], reverse=True)
    
    print("Recommended Products for User 1:")
    for pid, score in recommended:
        print(f"Product {pid} → Score: {score:.2f}")

if __name__ == "__main__":
    build_recommender()
