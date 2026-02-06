import streamlit as st
import pandas as pd

st.title("Nassau Candy Profit Dashboard")

df = pd.read_csv("Nassau Candy Distributor.csv")

division = st.sidebar.selectbox("Select Division", df["Division"].unique())

filtered = df[df["Division"] == division]

st.subheader("Profit by Product")
st.bar_chart(filtered.groupby("Product Name")["Gross Profit"].sum())

st.subheader("Sales vs Profit")
st.scatter_chart(filtered[["Sales","Gross Profit"]])

st.dataframe(filtered)
