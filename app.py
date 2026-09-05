import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("CSV Data Explorer + Predictor")
st.write("Upload any CSV file, explore it, and predict values using ML.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of your data")
    st.dataframe(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    st.subheader("Visualize a column")
    column = st.selectbox("Choose a numeric column", numeric_cols)
    if column:
        st.bar_chart(df[column])

    st.subheader("🔮 Predict a value using ML")
    st.write("Pick an input column (X) and a target column (Y) to predict.")

    x_col = st.selectbox("Input column (X)", numeric_cols, key="x")
    y_col = st.selectbox("Target column to predict (Y)", numeric_cols, key="y")

    if x_col and y_col and x_col != y_col:
        X = df[[x_col]]
        y = df[y_col]

        model = LinearRegression()
        model.fit(X, y)

        st.write(f"Model trained: predicting **{y_col}** from **{x_col}**")

        user_input = st.number_input(f"Enter a value for {x_col}", value=float(X[x_col].mean()))

        prediction = model.predict([[user_input]])
        st.success(f"Predicted {y_col}: {prediction[0]:.2f}")