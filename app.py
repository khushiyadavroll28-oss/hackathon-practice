import streamlit as st
import pandas as pd

st.title("CSV Data Explorer")
st.write("Upload any CSV file and see instant insights.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of your data")
    st.dataframe(df.head())
    
    st.subheader("Basic Statistics")
    st.write(df.describe())
    
    st.subheader("Pick a column to visualize")
    column = st.selectbox("Choose a numeric column", df.select_dtypes(include="number").columns)
    
    if column:
        st.bar_chart(df[column])