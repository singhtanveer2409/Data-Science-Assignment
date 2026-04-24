# Data-Science-Assignment
## Name: TANVEER PRAKASH SINGH 
## PRN: 1272250158

# 💻 Laptop Price Predictor

A machine learning web app that predicts laptop prices (in Euros) based on key specifications like brand, processor, RAM, storage, and OS — built with **scikit-learn** and **Streamlit**.

---

## 📸 Demo

> Select your laptop specs → Click Predict → Get an estimated price instantly.
<img width="1783" height="1079" alt="image" src="https://github.com/user-attachments/assets/3a18c964-45c5-4093-bfc8-bc379ea53d05" />
---

## 📁 Project Structure

```
laptop-price-predictor/
│
├── laptop_price_model.ipynb   # Data preprocessing, model training & saving
├── app.py              # Streamlit web app
├── laptop_model.pkl           # Trained KNN model (generated after running notebook)
├── laptop_price.csv # Dataset (download from Kaggle)
└── README.md
```

---

## 📊 Dataset

**Source:** [Laptop Price Dataset – Kaggle](https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset)

**Size:** ~1,300 laptops | **Target:** `Price (Euro)`

| Column | Description |
|---|---|
| `Company` | Brand (Dell, HP, Lenovo, Apple, etc.) |
| `CPU_Type` | Processor (Core i5, Ryzen 7, etc.) |
| `RAM (GB)` | RAM in GB |
| `Memory` | Storage (e.g. `256GB SSD`, `128GB SSD + 1TB HDD`) |
| `OpSys` | Operating System |
| `Price (Euro)` | Target variable |

---

## ⚙️ Features Used for Prediction

| Feature | Type | Example |
|---|---|---|
| Brand | Categorical | Dell, Apple, MSI |
| Processor | Categorical | Core i5, Ryzen 7 |
| RAM | Numerical | 4, 8, 16, 32 GB |
| Storage (GB) | Numerical | 256, 512, 1000 GB |
| Storage Type | Categorical | SSD, HDD, SSD+HDD |
| OS | Categorical | Windows, macOS, Linux |

> **Note:** The `Memory` column is parsed automatically — complex values like `128GB SSD + 1TB HDD` are split into storage size and type.

---

## 🤖 Models Compared

| Model | Score (R²) |
|---|---|
| Linear Regression | Low |
| **KNN (k=3)** | **Best ✅** |
| KNN (k=5) | Good |
| SVM (RBF kernel) | Moderate |

KNN with k=3 was selected as the final model based on training score.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor
```

### 2. Install dependencies
```bash
pip install pandas scikit-learn streamlit
```

### 3. Download the dataset
Download from [Kaggle](https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset), extract the ZIP, and place `laptop_price - dataset.csv` in the project folder.

### 4. Train the model
Open and run all cells in `laptop_price_model.ipynb`. This generates `laptop_model.pkl`.

### 5. Run the app
```bash
streamlit run laptop_app.py
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **pandas** — data loading and feature engineering
- **scikit-learn** — model training (KNN, Linear Regression, SVR)
- **pickle** — model serialization
- **Streamlit** — web app UI

---

## 📌 Inspired By

This project follows the same workflow as a **Car Price Predictor** mini project — applying the same ML pipeline to a new domain with richer feature engineering.

---

## 📄 License

This project is for educational purposes. Dataset credit: [ironwolf404 on Kaggle](https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset).

