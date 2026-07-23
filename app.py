import streamlit as st
import pandas as pd
import pickle

# Load Dataset
df = pd.read_csv("laptops.csv")

# Load Saved Files
model = pickle.load(open("laptops.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Page Configuration
st.set_page_config(
    page_title="Know Your Laptop Price",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("💻 Laptop Price Predictor")
st.write(
    "Predict the price of a laptop using a trained Linear Regression model."
)

# Sidebar
st.sidebar.title("💻 Laptop Price Predictor")

st.sidebar.header("👨‍💻 Developer")
st.sidebar.write("Bharat K. Talekar")

st.sidebar.header("🤖 Model")
st.sidebar.write("Linear Regression")

st.sidebar.header("📊 Model Performance")
st.sidebar.write("R² Score : 86.90%")

st.sidebar.header("📁 Dataset")
st.sidebar.write("Laptop Price Dataset")

# Input Section
st.header("📝 Enter Laptop Details")

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Select Brand", sorted(df["Brand"].unique()))

    cpu = st.selectbox("Select CPU", sorted(df["CPU"].unique()))

    ram = st.selectbox("Select RAM (GB)", sorted(df["RAM"].unique()))

    storage = st.selectbox("Select Storage (GB)", sorted(df["Storage"].unique()))

    gpu = st.selectbox(
        "Select GPU",
        sorted(df["GPU"].dropna().unique())
    )

with col2:

    status = st.selectbox(
        "Select Status",
        sorted(df["Status"].unique())
    )

    storage_type = st.selectbox(
        "Storage Type",
        sorted(df["Storage type"].dropna().unique())
    )

    screen = st.number_input(
        "Screen Size (Inches)",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1
    )

    touch = st.selectbox(
        "Touch Screen",
        sorted(df["Touch"].unique())
    )

    laptop_model = st.selectbox(
        "Select Model",
        sorted(df["Model"].dropna().unique())
    )

# Predict Button
predict_button = st.button("🔍 Predict Price")

if predict_button:

    input_data = pd.DataFrame({
        "Brand": [brand],
        "Model": [laptop_model],
        "Status": [status],
        "CPU": [cpu],
        "RAM": [ram],
        "Storage": [storage],
        "Storage type": [storage_type],
        "GPU": [gpu],
        "Screen": [screen],
        "Touch": [touch]
    })

    # One-Hot Encoding
    input_encoded = pd.get_dummies(input_data)

    # Match Training Columns
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    # Scale Input
    input_scaled = scaler.transform(input_encoded)

    # Prediction
    prediction = model.predict(input_scaled)

    # Display Result
    st.success(f"💰 Estimated Laptop Price: ₹ {prediction[0]:,.2f}")