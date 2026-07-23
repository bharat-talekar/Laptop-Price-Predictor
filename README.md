# 💻 Laptop Price Prediction

A Machine Learning web application built using **Python**, **Scikit-learn**, and **Streamlit** that predicts the price of a laptop based on its specifications.

## 📌 Project Overview

This project uses a **Linear Regression** model to estimate laptop prices. Users can enter laptop details through a simple Streamlit interface, and the model predicts the expected price instantly.

---

## 🚀 Features

* User-friendly Streamlit interface
* Real-time laptop price prediction
* Machine Learning model using Linear Regression
* Data preprocessing with feature scaling and one-hot encoding
* Fast and accurate predictions

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Pickle

---

## 📂 Project Structure

```text
Laptop_Price_Prediction/
│
├── app.py
├── laptops.csv
├── laptops.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses a laptop dataset containing information such as:

* Brand
* Processor
* RAM
* Storage
* Screen Size
* Condition
* Price

The target variable is:

**Price**

---

## 🤖 Machine Learning Workflow

1. Load the dataset
2. Clean and preprocess the data
3. Encode categorical features
4. Scale numerical features
5. Train a Linear Regression model
6. Save the trained model using Pickle
7. Build the Streamlit web application
8. Predict laptop prices from user input

---

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/your-username/Laptop-Price-Prediction.git
```

### Move into the project folder

```bash
cd Laptop-Price-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📈 Model Performance

* **Algorithm:** Linear Regression
* **R² Score:** 0.869
* **MAE:** 234.15
* **RMSE:** 347.54

---

## 🖥️ Application Inputs

The application accepts:

* Brand
* Processor
* RAM
* Storage
* Screen Size
* Condition

After clicking the **Predict Price** button, the estimated laptop price is displayed.

---

## 📷 Output

The application predicts the expected laptop price based on the selected specifications through an interactive Streamlit interface.

---

## 👨‍💻 Developer

**Bharat K. Talekar**

Diploma in Computer Engineering

Machine Learning & AI Intern

---

## 📜 License

This project is developed for educational and internship purposes.
