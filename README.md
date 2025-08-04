# 🛍️ TradeSphere: AI-based E-commerce Optimization Platform

**TradeSphere** is a robust, modular e-commerce intelligence platform built with Django and Python, seamlessly integrating AI-driven components such as personalized recommendation systems, dynamic pricing optimization, and customer segmentation strategies. This project is tailored to mimic real-world e-commerce ecosystems and serves as a launchpad for intelligent decision-making in retail platforms.

---

## Project Highlights

- **Product Recommendation System**: Personalized product suggestions powered by collaborative filtering (using the Surprise library).
- **Dynamic Pricing Engine**: Price optimization based on real-time demand signals (e.g., sales volume).
- **Customer Segmentation**: Identifies clusters of users using unsupervised learning (KMeans), enabling targeted marketing.
- **Admin Dashboard**: A minimal interface to simulate business operations — trigger AI modules, visualize outcomes.
- **Plug & Play Architecture**: All ML pipelines are decoupled and modular (in `/analytics/`), making it scalable and customizable.

---

## Structure

tradesphere/

│

├── core/ # Django app

│ ├── models.py

│ ├── views.py

│ ├── urls.py

│ ├── templates/

│ └── static/

│

├── analytics/ # All ML pipelines

│ ├── recommender.py # Surprise-based product recommender

│ ├── segmentation.py # KMeans-based customer clustering

│ └── pricing_model.py # Dynamic pricing logic

│

├── db.sqlite3 # Sample database

├── manage.py

├── requirements.txt

└── README.md


---

## AI Modules Overview

### 1. Recommendation System

- **Approach**: Item-based collaborative filtering
- **Library**: [`Surprise`](https://surprise.readthedocs.io/)
- **Goal**: Recommend top-N products to users based on past behavior
- **How it Works**:
    - Data matrix of (user, item, rating)
    - Train with `KNNBasic` or `SVD`
    - Fetch top recommendations for User ID

 _Trigger: Admin clicks "Run Recommendation"_  
 _Output: Top-N products shown on dashboard_

---

### 2. Dynamic Pricing Optimization

- **Approach**: Rule-based price adjustment
- **Logic**: Adjust prices based on product demand (sales count)
    - High demand → increase price
    - Low demand → discount
- **Goal**: Maximize revenue & maintain inventory balance

 _Trigger: "Optimize Pricing"_  
 _Output: New prices computed and shown per product_

---

### 3. Customer Segmentation

- **Approach**: KMeans clustering
- **Features**: Recency, Frequency, Monetary value (RFM-style)
- **Goal**: Group customers into meaningful marketing segments

 _Trigger: "Segment Customers"_  
 _Output: Cluster IDs per user with label inference_

---

## 📊 Sample Dataset & Simulation

For testing purposes, sample data is bundled in the `analytics/data/` folder or embedded in Python files.  

If you wish to test on **real or external datasets**, consider:

-  **User Purchase Logs**: [Retail Dataset - UCI Machine Learning](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

_You can replace the dummy data with these sources using CSV import logic inside `/analytics/` scripts._

---

## How To Run

### 1. Clone & Set up Environment

```bash
git clone https://github.com/yourusername/tradesphere.git
cd tradesphere
python -m venv venv
venv\Scripts\activate    # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
```

### 2. Migrate & Run Server
```bash
python manage.py migrate
python manage.py runserver
```
### Features Showcase
| Module                | Trigger Location | Output                                |
| --------------------- | ---------------- | ------------------------------------- |
| Product Recommender   | Dashboard Button | Shows top products for User ID 1      |
| Dynamic Pricing       | Dashboard Button | Updates product prices live           |
| Customer Segmentation | Dashboard Button | Clusters users & shows segment labels |

# Frontend UI Note
Currently, the frontend is kept minimal (Django templates + Bootstrap) for clarity. However, the backend logic is structured to allow easy integration with:

* ReactJS / Next.js (via Django REST API)

* Mobile apps (Flutter, React Native)

* BI tools (via CSV/JSON export from ML scripts)

Let us know if you’d like a more enhanced frontend version, we’re open to PRs!

# Sample Screenshot

<img width="1920" height="3696" alt="image" src="https://github.com/user-attachments/assets/e2128da9-2e40-4b01-b196-0719ffbe2032" />

# 👩‍💻 Author & Maintainer
Ms. Aliza Mustafa

ML Engineer | Data Enthusiast | AI Explorer

📫 (https://www.linkedin.com/in/aliza-mustafa-ml-engineer/)
